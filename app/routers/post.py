from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional
from .. import models, schema, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get('/', response_model=List[schema.VoteOut])
def get_posts(db: Session =Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ''):
    # cursor.execute(""" SELECT * FROM post""")
    # posts = cursor.fetchall()
    # print(posts)
    posts = db.query(models.Post)

    results = db.query(models.Post, func.count(models.Vote.post_id).label("Votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id)\
                        .filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return results



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.PostResponse)
#''' when using post requests use the body class that was imported from fastapi.params store it in a variable
#    that is of type dict'''
def create_posts(post: schema.PostCreate, db: Session =Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" INSERT INTO post (title, content, published) VALUES (%s, %s, %s) RETURNING *""",(post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    print(current_user.id)
    new_post = models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get('/{id}', response_model=schema.VoteOut)
def get_post(id: int, db: Session =Depends(get_db)):
    # cursor.execute(""" SELECT * FROM post WHERE id = %s""", (str(id)))
    # post = cursor.fetchone()
    # post = db.query(models.Post)
    results = db.query(models.Post, func.count(models.Vote.post_id).label("Votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id)\
                        .filter(models.Post.id == id).first()
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post does not exists")

    return results




@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session =Depends(get_db) , current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" DELETE FROM post WHERE id = %s RETURNING *""", (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You cannot delete this post. You are not authorized to do that')
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}', response_model=schema.PostResponse)
# id:int is the path parameter, posst is the data that is gotten from the user( the pydantic model )
def update_date(id:int, posst:schema.PostCreate, db: Session =Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" UPDATE post SET title= %s, content=%s , published=%s  WHERE id = %s RETURNING *""",\
                    # (post.title, post.content, post.published,str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You cannot update this post. You are not authorized to do that')
    post_query.update(posst.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()



