import asyncio
from fastapi import FastAPI, HTTPException
from uagents import Agent, Context
from pydantic import BaseModel
from typing import List, Dict, Any
import uvicorn
import threading
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import signal
import sys

class Slot:
    def __init__(self, slot_id: int, available: bool):
        self.slot_id = slot_id
        self.available = available

class SlotRequest(BaseModel):
    slot_id: int

app = FastAPI()

# Shared slots (creating slots 1 to 11)
shared_slots = [Slot(slot_id=i, available=True) for i in range(1, 12)]

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

# Instantiate agents
central_agent = CentralAgent()

# Terminal Interface
console = Console()

def display_slots_table(slots):
    table = Table(title="Available Slots")
    table.add_column("Slot ID", justify="center", style="cyan")
    table.add_column("Status", justify="center", style="magenta")

    for slot in slots:
        status = "Available" if slot.available else "Occupied"
        table.add_row(str(slot.slot_id), status)

    console.print(table)

async def terminal_interface():
    while True:
        console.print("\n[bold cyan]Parking System Menu:[/bold cyan]")
        console.print("[1] View Available Slots")
        console.print("[2] Occupy a Slot (Central Agent)")
        console.print("[3] Release a Slot (Central Agent)")
        console.print("[4] Exit")

        choice = Prompt.ask("Choose an option (1-4)", choices=["1", "2", "3", "4"])

        try:
            if choice == "1":
                available_slots = await central_agent.available_slots(None)
                display_slots_table([Slot(slot_id=slot['slot_id'], available=True) for slot in available_slots])

            elif choice == "2":
                slot_id = int(Prompt.ask("Enter the slot ID to occupy"))
                result = await central_agent.occupy_slot(None, slot_id)
                if result["status"] == "occupied":
                    console.print(f"[green]Slot {slot_id} has been occupied.[/green]")
                else:
                    console.print("[red]Error:[/red] Slot not available.")

            elif choice == "3":
                slot_id = int(Prompt.ask("Enter the slot ID to release"))
                result = await central_agent.release_slot(None, slot_id)
                if result["status"] == "released":
                    console.print(f"[green]Slot {slot_id} has been released.[/green]")
                else:
                    console.print("[red]Error:[/red] Slot not occupied.")

            elif choice == "4":
                console.print("[yellow]Exiting...[/yellow]")
                

        except (ValueError, KeyboardInterrupt) as e:
            console.print(f"[red]Error:[/red] {str(e)}. Exiting...")
            break

def signal_handler(sig, frame):
    console.print("[red]Exiting...[/red]")
    sys.exit(0)

if __name__ == "__main__":
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)

    # Start the FastAPI server in a separate thread
    threading.Thread(target=lambda: uvicorn.run(app, host="127.0.0.1", port=8000)).start()
    asyncio.run(terminal_interface())  # Run the terminal interface using asyncio
