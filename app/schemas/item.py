from bson import ObjectId
from pydantic import BaseModel, Field
from app.schemas.pyobjectid import PyObjectId

class Item(BaseModel):
    mongodb_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    id: str
    name: str
    category: str
    games: object

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}