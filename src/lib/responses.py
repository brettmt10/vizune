from pydantic import BaseModel
from typing import Literal, Union

class ResponseModelVizuneBar(BaseModel):
    chart: Literal['bar']
    x_lab: str
    y_lab: str
    
class ResponseModelVizuneLine(BaseModel):
    chart: Literal['line']
    x_lab: str
    y_lab: str
    smooth: bool
    
ChartResponseOptions = Union[
    ResponseModelVizuneBar,
    ResponseModelVizuneLine
]