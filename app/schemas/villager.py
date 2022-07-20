from bson import ObjectId
from pydantic import BaseModel, Field
from app.schemas.pyobjectid import PyObjectId

class Villager(BaseModel):
    mongodb_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    gender: str
    species: str
    birthday: str = None
    name: str
    games: object

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}