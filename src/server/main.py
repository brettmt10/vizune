from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import pandas as pd
from src.lib.types import TypeInference
import numpy as np

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

@app.post("/summary")
async def summarize(entry: list[dict]):
    te = TypeInference()
    df = pd.DataFrame(entry)
    for col in df:
        df[col] = te.infer(df, col)
    return df.replace({np.nan: None})