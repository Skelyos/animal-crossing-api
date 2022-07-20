from app.schemas import villager
from fastapi import APIRouter, status
from ..core.database import mongo_database

router = APIRouter()

collection_name = 'villagers'

@router.get("/all", tags=["villagers"], status_code=status.HTTP_200_OK)
def get_all_villagers():
    collection = mongo_database[collection_name]
    found_items_cursor = list(collection.find())
    found_items: list[villager.Villager] = [villager.Villager(**found_item_cursor) for found_item_cursor in found_items_cursor]
    return found_items


@router.get("/species", tags=["villagers"], status_code=status.HTTP_200_OK)
def get_villagers_by_category(search_species: str):
    collection = mongo_database[collection_name]
    found_items_cursor = list(collection.find({'species': search_species.lower()}))
    found_items: list[villager.Villager] = [villager.Villager(**found_item_cursor) for found_item_cursor in found_items_cursor]
    return found_items


@router.get("/gender", tags=["villagers"], status_code=status.HTTP_200_OK)
def get_item_by_gender(search_gender: str):
    collection = mongo_database[collection_name]
    found_items_cursor = list(collection.find({'gender': search_gender.lower()}))
    found_items: list[villager.Villager] = [villager.Villager(**found_item_cursor) for found_item_cursor in found_items_cursor]
    return found_items


@router.get("/search", tags=["villagers"], status_code=status.HTTP_200_OK)
def get_item_by_name(search_text: str):
    collection = mongo_database[collection_name]
    found_items_cursor = list(collection.find({"$text": {"$search": search_text}}))
    found_items: list[villager.Villager] = [villager.Villager(**found_item_cursor) for found_item_cursor in found_items_cursor]
    return found_items
