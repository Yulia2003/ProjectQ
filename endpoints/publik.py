from typing import List
from models.publiks import Publik, PublikIn
from models.user import User
from repositories.publiks import PublikRepository
from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_publik_repository, get_current_user

router = APIRouter()

@router.get("/", response_model=List[Publik])
async def read_publiks(
    limit: int = 100,
    skip: int = 0,
    publiks: PublikRepository = Depends(get_publik_repository)):
    return await publiks.get_all(limit=limit, skip=skip)

@router.post("/", response_model=Publik)
async def create_publik(
    j: PublikIn, 
    publiks: PublikRepository = Depends(get_publik_repository),
    current_user: User = Depends(get_current_user)):
    return await publiks.create(user_id=current_user.id, j=j)

@router.put("/", response_model=Publik)
async def update_publik(
    id: int,
    j: PublikIn, 
    publiks: PublikRepository = Depends(get_publik_repository),
    current_user: User = Depends(get_current_user)):
    publik = await publiks.get_by_id(id=id)
    if publik is None or publik.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publik not found")
    return await publiks.update(id=id, user_id=current_user.id, j=j)

@router.delete("/")
async def delete_publik(id: int,
    publiks: PublikRepository = Depends(get_publik_repository),
    current_user: User = Depends(get_current_user)):
    publik = await publiks.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publik not found")
    if publik is None or publik.user_id != current_user.id:
        raise not_found_exception
    result = await publiks.delete(id=id)
    return {"status": True}