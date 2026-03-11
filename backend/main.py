from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from simulation import step_simulation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/simulate")

def simulate():

    frame,reward = step_simulation()

    return {
        "frame":frame,
        "reward":reward
    }