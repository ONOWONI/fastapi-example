from app import oauth2
from .. import models, schema, utils
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import engine, get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/vote",
    tags= ["Vote"]
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schema.Vote, db: Session =Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Does not exist')

    vote_query = db.query(models.Post).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    votes = vote_query.first()
    if (vote.dir==1):
        if votes:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='cant vote again')
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"status": "Completed"}
    else:
        if not votes:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='not found')

        vote_query.delete(synchronize_session=False)
        db.commit()
    return {"liked": "Or is it"}