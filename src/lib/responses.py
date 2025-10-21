from pydantic import BaseModel
from enum import Enum

class ChartOptions(str, Enum):
    BAR = "bar"
    LINE = "line"
    
class ResponseModelVizuneBar(BaseModel):
    chart: ChartOptions
    x_lab: str
    y_lab: str
    
    