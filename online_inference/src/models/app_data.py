from typing import List, Union
from pydantic import BaseModel, conlist


class HeartModel(BaseModel):
    data: List[conlist(Union[float, str, None])]
    features: List[str]


class HeartResponse(BaseModel):
    target: int
