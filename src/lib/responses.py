from pydantic import BaseModel
from enum import Enum
from typing import Literal

class ResponseModelVizuneBar(BaseModel):
    chart: Literal['bar']
    x_lab: str
    y_lab: str

    
    
    