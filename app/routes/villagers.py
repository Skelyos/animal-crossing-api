from fastapi import APIRouter, status

router = APIRouter()


@router.get("/", tags=["villagers"], status_code=status.HTTP_200_OK)
def get_villager():
    return 'villager'
