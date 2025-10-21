from pydantic import BaseModel
from typing import Literal

class ResponseModelVizuneBar(BaseModel):
    chart: Literal['bar']
    x_lab: str
    y_lab: str
    
class ResponseModelVizuneLine(BaseModel):
    chart: Literal['line']
    x_lab: str
    y_lab: str
    smooth: bool

class ChartResponseOptionSchemas(BaseModel):
    chart_type: Literal['bar', 'line']
    bar_config: ResponseModelVizuneBar | None = None
    line_config: ResponseModelVizuneLine | None = None