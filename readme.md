# FetchParking App

This project implements a parking system using the [`uagents`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A5%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition") library and FastAPI. It consists of three agents: [`CentralAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A18%2C%22character%22%3A6%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition"), [`DriverAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A43%2C%22character%22%3A6%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition"), and [`ParkingAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A58%2C%22character%22%3A6%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition"), each managing different aspects of the parking system.
 The [`uagents`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A5%7D%7D%5D%2C%226c02a26f-db18-4796-b4f3-f0dcf5aff799%22%5D "Go to definition") library is used to create agents that can communicate with each other. In your code, you have three agents: [`CentralAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A18%2C%22character%22%3A6%7D%7D%5D%2C%226c02a26f-db18-4796-b4f3-f0dcf5aff799%22%5D "Go to definition"), [`DriverAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A43%2C%22character%22%3A6%7D%7D%5D%2C%226c02a26f-db18-4796-b4f3-f0dcf5aff799%22%5D "Go to definition"), and [`ParkingAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A58%2C%22character%22%3A6%7D%7D%5D%2C%226c02a26f-db18-4796-b4f3-f0dcf5aff799%22%5D "Go to definition"). Here's how they are used:

1. **CentralAgent**:
    - Manages a list of parking slots.
    - Provides methods to check available slots and occupy a slot.
    - Displays information about the agent and the slots it manages.

2. **DriverAgent**:
    - Interacts with the [`CentralAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A18%2C%22character%22%3A6%7D%7D%5D%2C%226c02a26f-db18-4796-b4f3-f0dcf5aff799%22%5D "Go to definition") to find available slots and occupy a slot.
    - Displays information about the agent.

3. **ParkingAgent**:
    - Manages its own list of available slots.
    - Displays information about the agent and the slots it manages.

### Key Components

1. **Agent Initialization**:
    Each agent is initialized with a name and a port number. For example:
    ```python
    class CentralAgent(Agent):
        def __init__(self):
            super().__init__(name="Central Agent", port=8000)
            self.slots = [Slot(slot_id=i, available=True) for i in range(1, 11)]
            self.display_info()
    ```

2. **Agent Communication**:
    Agents communicate with each other using asynchronous methods. For example, [`DriverAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A43%2C%22character%22%3A6%7D%7D%5D%2C%226c02a26f-db18-4796-b4f3-f0dcf5aff799%22%5D "Go to definition") calls [`CentralAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A18%2C%22character%22%3A6%7D%7D%5D%2C%226c02a26f-db18-4796-b4f3-f0dcf5aff799%22%5D "Go to definition")'s methods to find and occupy slots:
    ```python
    async def find_slots(self, ctx: Context) -> List[Dict[str, int]]:
        return await central_agent.available_slots(ctx)

    async def occupy_slot(self, ctx: Context, slot_id: int) -> Dict[str, Any]:
        return await central_agent.occupy_slot(ctx, slot_id)
    ```

3. **FastAPI Endpoints**:
    The FastAPI application exposes endpoints that interact with the agents. For example:
    ```python
    @app.get("/available_slots")
    async def get_available_slots():
        return await central_agent.available_slots(None)

    @app.post("/occupy_slot")
    async def occupy_slot(slot_request: SlotRequest):
        result = await central_agent.occupy_slot(None, slot_request.slot_id)
        if result["status"] == "not available":
            raise HTTPException(status_code=404, detail="Slot not available")
        return result
    ```

### Summary
- **CentralAgent** manages parking slots and provides methods to check and occupy slots.
- **DriverAgent** interacts with [`CentralAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A18%2C%22character%22%3A6%7D%7D%5D%2C%226c02a26f-db18-4796-b4f3-f0dcf5aff799%22%5D "Go to definition") to find and occupy slots.
- **ParkingAgent** manages its own slots and displays information.
- FastAPI endpoints allow external interaction with these agents.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/abhishek2001panwar/fetchParking
    cd fetchParking
    ```

2. Install the required dependencies:
    ```sh
    pip install fastapi uvicorn uagents pydantic httpie
    ```



### API Endpoints

#### Central Agent Endpoints

- **Get Available Slots**
    ```http
    GET /available_slots
    ```
    Returns a list of available slots managed by the [`CentralAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A18%2C%22character%22%3A6%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition").

- **Occupy Slot**
    ```http
    POST /occupy_slot
    ```
    Request Body:
    ```json
    {
        "slot_id": <slot_id>
    }
    ```
    Occupies a slot with the given [`slot_id`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A9%2C%22character%22%3A23%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition").

#### Driver Agent Endpoints

- **Get Available Slots**
    ```http
    GET /driver/available_slots
    ```
    Returns a list of available slots as seen by the [`DriverAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A43%2C%22character%22%3A6%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition").

- **Occupy Slot**
    ```http
    POST /driver/occupy_slot
    ```
    Request Body:
    ```json
    {
        "slot_id": <slot_id>
    }
    ```
    Occupies a slot with the given [`slot_id`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A9%2C%22character%22%3A23%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition") through the [`DriverAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A43%2C%22character%22%3A6%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition").

#### Parking Agent Endpoints

- **Get Available Slots**
    ```http
    GET /parking/available_slots
    ```
    Returns a list of available slots managed by the [`ParkingAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A58%2C%22character%22%3A6%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition").

- **Occupy Slot**
    ```http
    POST /parking/occupy_slot
    ```
    Request Body:
    ```json
    {
        "slot_id": <slot_id>
    }
    ```
    Occupies a slot with the given [`slot_id`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A9%2C%22character%22%3A23%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition") through the [`ParkingAgent`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FX%3A%2FfetchParking%2Fparkingsystem.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A58%2C%22character%22%3A6%7D%7D%5D%2C%22349d6278-a42c-4f3e-9824-6d121d6773fc%22%5D "Go to definition").


## To run application

Here are the `curl` and `httpie` commands for all the routes in your FastAPI application:

### Using `curl`

1. **Get Available Slots:**
   ```bash
   curl -X GET http://127.0.0.1:8000/available_slots
   ```

2. **Occupy a Slot:**
   ```bash
   curl -X POST http://127.0.0.1:8000/occupy_slot -H "Content-Type: application/json" -d '{"slot_id": 1}'
   ```

3. **Get Driver Available Slots:**
   ```bash
   curl -X GET http://127.0.0.1:8000/driver/available_slots
   ```

4. **Occupy a Slot as a Driver:**
   ```bash
   curl -X POST http://127.0.0.1:8000/driver/occupy_slot -H "Content-Type: application/json" -d '{"slot_id": 1}'
   ```

5. **Get Parking Available Slots:**
   ```bash
   curl -X GET http://127.0.0.1:8000/parking/available_slots
   ```

6. **Occupy a Slot from Parking:**
   ```bash
   curl -X POST http://127.0.0.1:8000/parking/occupy_slot -H "Content-Type: application/json" -d '{"slot_id": 1}'
   ```

### Using `httpie`

1. **Get Available Slots:**
   ```bash
   http GET http://127.0.0.1:8000/available_slots
   ```

2. **Occupy a Slot:**
   ```bash
   http POST http://127.0.0.1:8000/occupy_slot slot_id=1
   ```

3. **Get Driver Available Slots:**
   ```bash
   http GET http://127.0.0.1:8000/driver/available_slots
   ```

4. **Occupy a Slot as a Driver:**
   ```bash
   http POST http://127.0.0.1:8000/driver/occupy_slot slot_id=1
   ```

5. **Get Parking Available Slots:**
   ```bash
   http GET http://127.0.0.1:8000/parking/available_slots
   ```

6. **Occupy a Slot from Parking:**
   ```bash
   http POST http://127.0.0.1:8000/parking/occupy_slot slot_id=1
   ```

You can replace `slot_id=1` with any other slot ID you wish to occupy.

### FastAPI Endpoints

Defines the API endpoints for interacting with the agents.
```python
@app.get("/available_slots")
async def get_available_slots():
    return await central_agent.available_slots(None)

@app.post("/occupy_slot")
async def occupy_slot(slot_request: SlotRequest):
    result = await central_agent.occupy_slot(None, slot_request.slot_id)
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
```

### Code Overview

#### Slot Class

Represents a parking slot.
```python
class Slot:
    def __init__(self, slot_id: int, available: bool):
        self.slot_id = slot_id
        self.available = available
```

#### SlotRequest Class

Defines the request body for occupying a slot.
```python
class SlotRequest(BaseModel):
    slot_id: int
```

#### CentralAgent Class

Manages a list of parking slots and provides methods to check available slots and occupy a slot.
```python
class CentralAgent(Agent):
    def __init__(self):
        super().__init__(name="Central Agent", port=8000)
        self.slots = [Slot(slot_id=i, available=True) for i in range(1, 11)]
        self.display_info()

    async def available_slots(self, ctx: Context) -> List[Dict[str, int]]:
        return [{"slot_id": slot.slot_id} for slot in self.slots if slot.available]

    async def occupy_slot(self, ctx: Context, slot_id: int) -> Dict[str, str]:
        for slot in self.slots:
            if slot.slot_id == slot_id and slot.available:
                slot.available = False
                return {"status": "occupied", "slot_id": slot_id}
        return {"status": "not available", "slot_id": slot_id}
```

#### DriverAgent Class

Interacts with the `CentralAgent` to find and occupy slots.
```python
class DriverAgent(Agent):
    def __init__(self):
        super().__init__(name="Driver Agent", port=8001)
        self.display_info()

    async def find_slots(self, ctx: Context) -> List[Dict[str, int]]:
        return await central_agent.available_slots(ctx)

    async def occupy_slot(self, ctx: Context, slot_id: int) -> Dict[str, Any]:
        return await central_agent.occupy_slot(ctx, slot_id)
```

#### ParkingAgent Class

Manages its own list of available slots.
```python
class ParkingAgent(Agent):
    def __init__(self):
        super().__init__(name="Parking Agent", port=8002)
        self.available_slots = [Slot(slot_id=i, available=True) for i in range(1, 11)]
        self.display_info()
```

#### FastAPI Endpoints

Defines the API endpoints for interacting with the agents.
```python
@app.get("/available_slots")
async def get_available_slots():
    return await central_agent.available_slots(None)

@app.post("/occupy_slot")
async def occupy_slot(slot_request: SlotRequest):
    result = await central_agent.occupy_slot(None, slot_request.slot_id)
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
```

### Running the Application

To start the application, run:
```sh
uvicorn parkingsystem:app --host 0.0.0.0 --port 8000
```

This will start the FastAPI server and make the endpoints available for interaction.
