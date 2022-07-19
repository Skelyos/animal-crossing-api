from fastapi import APIRouter, status

from app.schemas import item

from ..core.database import mongo_database

router = APIRouter()

collection_name = 'items'

@router.get("/all", tags=["items"], status_code=status.HTTP_200_OK)
def get_all_item():
    collection = mongo_database[collection_name]
    found_items_cursor = list(collection.find())
    found_items: list[item.Item] = [item.Item(**found_item_cursor) for found_item_cursor in found_items_cursor]

    return found_items


@router.get("/category", tags=["items"], status_code=status.HTTP_200_OK)
def get_item_by_category(search_category: str):
    collection = mongo_database[collection_name]
    found_items_cursor = list(collection.find({'category': search_category.lower()}))
    found_items: list[item.Item] = [item.Item(**found_item_cursor) for found_item_cursor in found_items_cursor]

    return found_items


@router.get("/name", tags=["items"], status_code=status.HTTP_200_OK)
def get_item_by_name(search_name: str):
    collection = mongo_database[collection_name]    
    found_items_cursor = list(collection.find({"$id": {"$search": search_name.lower()}}))
    found_items: list[item.Item] = [item.Item(**found_item_cursor) for found_item_cursor in found_items_cursor]
    return found_items

