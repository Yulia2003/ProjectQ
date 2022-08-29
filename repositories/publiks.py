from typing import List, Optional
import datetime
from models.publiks import Publik, PublikIn
from db.publiks import publiks
from .base import BaseRepository

class PublikRepository(BaseRepository):

    async def create(self, user_id: int, j: PublikIn) -> Publik:
        publik = Publik(
            id=0,
            user_id=user_id,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            title=j.title,
            description=j.description,
            reader=j.reader,
            admin=j.admin,
            moderator=j.moderator,
        )
        values = {**publik.dict()}
        values.pop("id", None)
        query = publiks.insert().values(**values)
        publik.id = await self.database.execute(query=query)
        return publik

    async def update(self, id: int, user_id: int, j: PublikIn) -> Publik:
        publik = Publik(
            id=id,
            user_id=user_id,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            title=j.title,
            description=j.description,
            reader=j.reader,
            admin=j.admin,
            moderator=j.moderator,
        )
        values = {**publik.dict()}
        values.pop("id", None)
        values.pop("created_at", None)
        query = publiks.update().where(publiks.c.id==id).values(**values)
        await self.database.execute(query=query)
        return publik

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Publik]:
        query = publiks.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)
    
    async def delete(self, id: int):
        query = publiks.delete().where(publiks.c.id==id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[Publik]:
        query = publiks.select().where(publiks.c.id==id)
        publik = await self.database.fetch_one(query=query)
        if publik is None:
            return None
        return Publik.parse_obj(publik)