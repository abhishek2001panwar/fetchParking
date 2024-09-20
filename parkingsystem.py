

from fastapi import FastAPI, HTTPException
from uagents import Agent, Context
from pydantic import BaseModel
from typing import List, Dict, Any
import uvicorn

class Slot:
    def __init__(self, slot_id: int, available: bool):
        self.slot_id = slot_id
        self.available = available

class SlotRequest(BaseModel):
    slot_id: int

app = FastAPI()

class CentralAgent(Agent):
    def __init__(self):
        super().__init__(name="Central Agent", port=8000)
        self.slots = [Slot(slot_id=i, available=True) for i in range(1, 11)]
        self.display_info()

    def display_info(self):
        print(f"Agent Name: {self.name}")
        print(f"Port: {self._port}")  # Access the private port attribute
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

class DriverAgent(Agent):
    def __init__(self):
        super().__init__(name="Driver Agent", port=8001)
        self.display_info()

    def display_info(self):
        print(f"Agent Name: {self.name}")
        print(f"Port: {self._port}\n")  # Access the private port attribute

    async def find_slots(self, ctx: Context) -> List[Dict[str, int]]:
        return await central_agent.available_slots(ctx)

    async def occupy_slot(self, ctx: Context, slot_id: int) -> Dict[str, Any]:
        return await central_agent.occupy_slot(ctx, slot_id)

class ParkingAgent(Agent):
    def __init__(self):
        super().__init__(name="Parking Agent", port=8002)
        self.available_slots = [Slot(slot_id=i, available=True) for i in range(1, 11)]
        self.display_info()

    def display_info(self):
        print(f"Agent Name: {self.name}")
        print(f"Port: {self._port}")  # Access the private port attribute
        print("Available Slots:")
        for slot in self.available_slots:
            status = "Available" if slot.available else "Occupied"
            print(f"  - Slot ID: {slot.slot_id}, Status: {status}")
        print("\n")

# Instantiate agents
central_agent = CentralAgent()
driver_agent = DriverAgent()
parking_agent = ParkingAgent()

@app.get("/available_slots")
async def get_available_slots():
    return await central_agent.available_slots(None)

@app.post("/occupy_slot")
async def occupy_slot(slot_request: SlotRequest):
    result = await central_agent.occupy_slot(None, slot_request.slot_id , message="Slot occupied")
    if result["status"] == "not available":
        raise HTTPException(status_code=404, detail="Slot not available")
    return result

@app.get("/driver/available_slots")
async def get_driver_available_slots():
    return await driver_agent.find_slots(None)

@app.post("/driver/occupy_slot")
async def occupy_driver_slot(slot_request: SlotRequest):
    result = await driver_agent.occupy_slot(None, slot_request.slot_id)
    if result["status"] == "not available":
        raise HTTPException(status_code=404, detail="Slot not available")
    return result

@app.get("/parking/available_slots")
async def get_parking_available_slots():
    return [{"slot_id": slot.slot_id for slot in parking_agent.available_slots if slot.available}]

@app.post("/parking/occupy_slot")
async def occupy_parking_slot(slot_request: SlotRequest):
    result = await parking_agent.occupy_slot(None, slot_request.slot_id)
    if result["status"] == "not available":
        raise HTTPException(status_code=404, detail="Slot not available")
    return result

if __name__ == "__main__":
    print("Starting Parking System API...\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)

