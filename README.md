# Autonomous Driving Simulation Web Application

## Overview

This project demonstrates a simple **Autonomous Driving Simulation system** built using **Artificial Intelligence and Web Technologies**.
The system integrates a **Python backend** that runs a driving simulation environment with an **Angular frontend** that interacts with the simulation through REST APIs.

The backend uses the **Gymnasium CarRacing environment** to simulate autonomous vehicle behavior, while the frontend provides a web interface to trigger and monitor the simulation.

This project demonstrates concepts such as:

* Reinforcement learning environments
* Backend API development
* Frontend–backend communication
* Image processing
* Full-stack AI application architecture

---

## System Architecture

```
Angular Frontend
       │
       │ HTTP API Request
       ▼
Python FastAPI Backend
       │
       │ Simulation Step
       ▼
Gymnasium CarRacing Environment
```

---

## Technologies Used

### Backend

* Python
* FastAPI
* Gymnasium (CarRacing simulation)
* OpenCV
* NumPy
* PyTorch (optional model structure)

### Frontend

* Angular
* TypeScript
* HTML / CSS
* Angular HTTP Client

### Tools

* Node.js
* Angular CLI
* Uvicorn
* Git / GitHub

---

## Project Structure

```
autonomous-driving-web
│
├── backend
│   ├── main.py
│   ├── simulation.py
│   ├── model.py
│   └── requirements.txt
│
└── frontend
    └── src
        └── app
            ├── simulation
            │   ├── simulation.component.ts
            │   ├── simulation.component.html
            │   └── simulation.component.css
            │
            └── services
                └── simulation.service.ts
```

---

## Backend Setup

Navigate to the backend directory:

```
cd backend
```

Install required dependencies:

```
pip install fastapi uvicorn numpy opencv-python torch "gymnasium[box2d]"
```

Run the backend server:

```
uvicorn main:app --reload
```

The API server will start at:

```
http://127.0.0.1:8000
```

Test endpoint:

```
http://127.0.0.1:8000/simulate
```

---

## Frontend Setup

Navigate to the frontend directory:

```
cd frontend
```

Install dependencies:

```
npm install
```

Run Angular development server:

```
ng serve
```

Open the application in the browser:

```
http://localhost:4200
```

---

## API Endpoint

### GET /simulate

Runs one step of the autonomous driving simulation.

**Response Example**

```
{
  "frame": [...],
  "reward": 3.2
}
```

**Parameters**

| Field  | Description                   |
| ------ | ----------------------------- |
| frame  | Simulation frame data         |
| reward | Reward value from environment |

---

## How the Simulation Works

1. The Angular frontend sends a request to the backend.
2. The backend runs one step of the CarRacing simulation.
3. The simulation returns:

   * environment frame
   * reward value
4. The backend sends this data to the frontend via REST API.
