from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()
URL_DEV = os.getenv('URL_DEV')
print("URL:", URL_DEV)
origins = [
    URL_DEV
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/max-accuracy")
async def max_engine(entry: list[dict]):
    return(entry)
                   