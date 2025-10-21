from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import pandas as pd
from src.lib.types import TypeInference
from src.lib.vizune import VizuneAI
import numpy as np

te = TypeInference()

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
    df = pd.DataFrame(entry)
    df, metadata = te.infer(df)
    input_df = df.replace({np.nan: None})
    
    vai = VizuneAI(input_df)
    res = vai.vizune()
    return res.output_text
 