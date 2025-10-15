from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Entry(BaseModel):
    name: str
    accuracy: float
    color: str

@app.post("/max-accuracy")
async def max_engine(entry: list[Entry]):
    return entry