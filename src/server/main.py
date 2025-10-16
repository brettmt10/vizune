from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import pandas as pd

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

@app.post("/generic")
async def generic_comp(entry: list[dict]):
    df = pd.DataFrame(entry)
    dtypes_dict = {col: str(dtype) for col, dtype in df.dtypes.items()}
    return dtypes_dict