from pydantic import BaseModel, PositiveInt


class Data(BaseModel):
    id: PositiveInt
    value: str
