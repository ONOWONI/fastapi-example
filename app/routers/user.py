from .. import models, schema, utils
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import engine, get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/users",
    tags= ["Users"]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.UserResponse)
def create_user(user: schema.UserCreate, db: Session =Depends(get_db)):
    user_check = db.query(models.User).filter(models.User.email == user.email).first()
    if user_check:
        raise HTTPException(status_code=status.HTTP_226_IM_USED, detail='Email already used Before')
    hashed_password = utils.hashe(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model=schema.UserResponse)
def get_user(id:int, db: Session =Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id: {id} does not exist')
    return user