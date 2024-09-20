

from fastapi import FastAPI, HTTPException
from uagents import Agent, Context
from pydantic import BaseModel
from typing import List, Dict, Any
import uvicorn
import requests
import threading
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

class Slot:
    def __init__(self, slot_id: int, available: bool):
        self.slot_id = slot_id
        self.available = available

class SlotRequest(BaseModel):
    slot_id: int

app = FastAPI()

# Shared slots
shared_slots = [Slot(slot_id=i, available=True) for i in range(1, 11)]

class CentralAgent(Agent):
    def __init__(self):
        super().__init__(name="Central Agent", port=8000)
        self.slots = shared_slots
        self.display_info()

    def display_info(self):
        print(f"Agent Name: {self.name}")
        print(f"Port: {self._port}")
        print("Managed Slots:")
        for slot in self.slots:
            status = "Available" if slot.available else "Occupied"
            print(f"  - Slot ID: {slot.slot_id}, Status: {status}")
        print("\n")

    async def available_slots(self, ctx: Context) -> List[Dict[str, int]]:
        return [{"slot_id": slot.slot_id} for slot in self.slots if slot.available]

    async def occupy_slot(self, ctx: Context, slot_id: int) -> Dict[str, str]:
        for slot in self.slots:
            if slot.slot_id == slot_id and slot.available:
                slot.available = False
                return {"status": "occupied", "slot_id": slot_id}
        return {"status": "not available", "slot_id": slot_id}

    async def release_slot(self, ctx: Context, slot_id: int) -> Dict[str, str]:
        for slot in self.slots:
            if slot.slot_id == slot_id and not slot.available:
                slot.available = True
                return {"status": "released", "slot_id": slot_id}
        return {"status": "not occupied", "slot_id": slot_id}

class DriverAgent(Agent):
    def __init__(self):
        super().__init__(name="Driver Agent", port=8001)
        self.display_info()

    def display_info(self):
        print(f"Agent Name: {self.name}")
        print(f"Port: {self._port}\n")

    async def find_slots(self, ctx: Context) -> List[Dict[str, int]]:
        return await central_agent.available_slots(ctx)

    async def occupy_slot(self, ctx: Context, slot_id: int) -> Dict[str, Any]:
        return await central_agent.occupy_slot(ctx, slot_id)

    async def release_slot(self, ctx: Context, slot_id: int) -> Dict[str, Any]:
        return await central_agent.release_slot(ctx, slot_id)

# Instantiate agents
central_agent = CentralAgent()
driver_agent = DriverAgent()

@app.get("/available_slots")
async def get_available_slots(role: str):
    if role not in ["Driver", "Parking Agent", "Central Agent"]:
        raise HTTPException(status_code=403, detail="Permission denied")
    return await central_agent.available_slots(None)

@app.post("/occupy_slot")
async def occupy_slot(slot_request: SlotRequest, role: str):
    if role != "Driver":
        raise HTTPException(status_code=403, detail="Only drivers can occupy slots")
    result = await central_agent.occupy_slot(None, slot_request.slot_id)
    if result["status"] == "not available":
        raise HTTPException(status_code=404, detail="Slot not available")
    return result

@app.post("/release_slot")
async def release_slot(slot_request: SlotRequest, role: str):
    if role != "Driver":
        raise HTTPException(status_code=403, detail="Only drivers can release slots")
    result = await central_agent.release_slot(None, slot_request.slot_id)
    if result["status"] == "not occupied":
        raise HTTPException(status_code=404, detail="Slot not occupied")
    return result

# Terminal Interface
console = Console()

def terminal_interface():
    while True:
        console.print("\n[bold cyan]Parking System Menu:[/bold cyan]")
        console.print("[1] View Available Slots")
        console.print("[2] Occupy a Slot (Driver only)")
        console.print("[3] Release a Slot (Driver only)")
        console.print("[4] Exit")
        
        role = Prompt.ask("Enter your role (Driver/Parking Agent/Central Agent)", choices=["Driver", "Parking Agent", "Central Agent"])
        
        choice = Prompt.ask("Choose an option (1-4)", choices=["1", "2", "3", "4"])
        
        if choice == "1":
            response = requests.get("http://127.0.0.1:8000/available_slots", params={"role": role})
            available_slots = response.json()
            table = Table(title="Available Slots")
            table.add_column("Slot ID", justify="center", style="cyan")
            for slot in available_slots:
                table.add_row(str(slot['slot_id']))
            console.print(table)
        
        elif choice == "2":
            if role != "Driver":
                console.print("[red]Only drivers can occupy slots.[/red]")
                continue
            try:
                slot_id = int(Prompt.ask("Enter the slot ID to occupy"))
                response = requests.post("http://127.0.0.1:8000/occupy_slot", json={"slot_id": slot_id}, params={"role": role})
                if response.status_code == 200:
                    console.print(f"[green]Slot {slot_id} has been occupied.[/green]")
                else:
                    console.print("[red]Error:[/red]", response.json().get("detail", "Slot not available."))
            except ValueError:
                console.print("[red]Invalid input. Please enter a valid slot ID.[/red]")
        
        elif choice == "3":
            if role != "Driver":
                console.print("[red]Only drivers can release slots.[/red]")
                continue
            try:
                slot_id = int(Prompt.ask("Enter the slot ID to release"))
                response = requests.post("http://127.0.0.1:8000/release_slot", json={"slot_id": slot_id}, params={"role": role})
                if response.status_code == 200:
                    console.print(f"[green]Slot {slot_id} has been released.[/green]")
                else:
                    console.print("[red]Error:[/red]", response.json().get("detail", "Slot not occupied."))
            except ValueError:
                console.print("[red]Invalid input. Please enter a valid slot ID.[/red]")
        
        elif choice == "4":
            console.print("[yellow]Exiting...[/yellow]")
            break
        
        else:
            console.print("[red]Invalid choice. Please try again.[/red]")
            
if __name__ == "__main__":
    # Start the FastAPI server in a separate thread
    
    # Run the terminal interface
    terminal_interface()
    threading.Thread(target=lambda: uvicorn.run(app, host="0.0.0.0", port=8000)).start()
