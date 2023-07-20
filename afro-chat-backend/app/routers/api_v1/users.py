from fastapi import APIRouter,Request,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.user import User

users_router = APIRouter(
            prefix="/items",
            tags=["items"],
            responses={404: {"description": "Not found"}},
    )


@users_router.get("/")
async def read_items(
        request:Request,
        session : AsyncSession = Depends(get_db)
    ):

    logger = request.state.logger
    logger.debug("this is debugger")
    return [{"username": "Rick"}, {"username": "Morty"}]
