from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Entry(BaseModel):
    name: str
    accuracy: float

@app.post("/max-accuracy")
async def max_engine(entry: Entry):
    content = entry.model_dump()    
    return content