from app.schemas import villager
from fastapi import APIRouter, status
from ..core.database import mongo_database

router = APIRouter()

collection_name = 'villagers'

@router.get("/all", tags=["villagers"], status_code=status.HTTP_200_OK)
def get_all_villagers(page_size: int = 250, page_number: int = 1):
    collection = mongo_database[collection_name]
    skip_value  = page_size * page_number

    total_villagers = collection.count_documents({})
    found_villagers_cursor = collection.find().limit(page_size).skip(skip_value)

    found_villagers: list[villager.Villager] = [villager.Villager(**found_item_cursor) for found_item_cursor in found_villagers_cursor]
    villager_out_object: villager.VillagerOut = villager.VillagerOut(villagers=found_villagers, total=total_villagers, page=page_number, page_size=page_size)
    return villager_out_object


@router.get("/species", tags=["villagers"], status_code=status.HTTP_200_OK)
def get_villagers_by_category(search_species: str):
    collection = mongo_database[collection_name]
    found_villagers_cursor = list(collection.find({'species': search_species.lower()}))
    found_villagers: list[villager.Villager] = [villager.Villager(**found_item_cursor) for found_item_cursor in found_villagers_cursor]
    return found_villagers


@router.get("/gender", tags=["villagers"], status_code=status.HTTP_200_OK)
def get_item_by_gender(search_gender: str):
    collection = mongo_database[collection_name]
    found_villagers_cursor = list(collection.find({'gender': search_gender.lower()}))
    found_villagers: list[villager.Villager] = [villager.Villager(**found_item_cursor) for found_item_cursor in found_villagers_cursor]
    return found_villagers


@router.get("/search", tags=["villagers"], status_code=status.HTTP_200_OK)
def get_item_by_name(search_text: str):
    collection = mongo_database[collection_name]
    found_villagers_cursor = list(collection.find({"$text": {"$search": search_text}}))
    found_villagers: list[villager.Villager] = [villager.Villager(**found_item_cursor) for found_item_cursor in found_villagers_cursor]
    return found_villagers
