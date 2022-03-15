from typing import Union

from fastapi import APIRouter, HTTPException, status
from sqlalchemy import delete, insert, select, update


from db import db
from models import RegisterID, Trainee_infobase, Trainee_info,RegisterUpdate

router = APIRouter()


@router.post("/", response_model=int, status_code=status.HTTP_201_CREATED)
async def create_trainee_info(trainee_info_dict: Trainee_infobase):
    sql = insert(Trainee_info).values(trainee_info_dict.dict())
    try:
        return await db.execute(sql)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e))


@router.get("/", response_model=RegisterID)
async def get_Trainee_info (id: int = None, disabled: bool = False ):
    """
        # รายละเอียด
        
        * ถ้าไม่มี `id` จะได้ผลลัพธ์เป็น `Array` ของ `Object` Blog ทั้งหมด
        * ถ้ามี `id` จะได้ผลลัพธ์เป็น `Object` ของ Blog
        
    """
    sql = select(Trainee_info).where(Trainee_info.disabled == disabled)

    if id is not None:
        sql = sql.where(Trainee_info.id == id)
  
        

    try:
       return await db.fetch_one(sql) if id else await db.fetch_all(sql)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e))
        
        
@router.put("/", response_model=None)
async def update_blog(registerupdate: RegisterUpdate):
    sql = update(Trainee_info).where(Trainee_info.id == registerupdate.id).values(registerupdate.dict())
    try:
        return await db.execute(sql)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e))
        
@router.delete("/", response_model=None)
async def delete_register(id: int):
    sql = delete(Trainee_info).where(Trainee_info.id == id)
    try:
        return await db.execute(sql)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e))
