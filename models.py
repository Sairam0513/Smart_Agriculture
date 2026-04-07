from pydantic import BaseModel
from typing import Dict

class Observation(BaseModel):
    data: Dict

class Action(BaseModel):
    decision: str

class Reward(BaseModel):
    value: float
