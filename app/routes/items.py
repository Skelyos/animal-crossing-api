from app.schemas import item
from fastapi import APIRouter, status
from ..core.database import mongo_database

router = APIRouter()

collection_name = 'items'

@router.get("/all", tags=["items"], status_code=status.HTTP_200_OK)
def get_all_item(page_size: int = 250, page_number: int = 1):
    collection = mongo_database[collection_name]
    skip_value  = page_size * page_number

    total_villagers = collection.count_documents({})
    found_items_cursor = collection.find().limit(page_size).skip(skip_value)

    found_items_list = list(found_items_cursor)
    found_items: list[item.Item] = [item.Item(**found_item) for found_item in found_items_list]
    item_out_object: item.ItemOut = item.ItemOut(items=found_items, total=total_villagers, page=page_number, page_size=page_size)

    return item_out_object


@router.get("/category", tags=["items"], status_code=status.HTTP_200_OK)
def get_item_by_category(search_category: str):
    collection = mongo_database[collection_name]
    found_items_cursor = collection.find({'category': search_category.lower()})
    found_items_list = list(found_items_cursor)
    found_items: list[item.Item] = [item.Item(**found_item) for found_item in found_items_list]
    return found_items


@router.get("/search", tags=["items"], status_code=status.HTTP_200_OK)
def get_item_by_search(search_text: str):
    collection = mongo_database[collection_name]
    found_items_cursor = collection.find({"$text": {"$search": search_text}})
    found_items_list = list(found_items_cursor)
    found_items: list[item.Item] = [item.Item(**found_item) for found_item in found_items_list]
    return found_items

