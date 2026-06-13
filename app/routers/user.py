from fastapi import APIRouter, Depends, HTTPException
from app.models.user import User
from app.schemas.user import UserSchema
from app.dependencies import get_db

router = APIRouter(prefix="/user")

@router.get("")
def view(db = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.get("/search")
def search(name: str = "",db = Depends(get_db)):
    users = db.query(User).filter(User.id.contains(name)).all()
    return users

@router.post("")
def store(request: UserSchema, db = Depends(get_db)):
    exesting_user = db.query(User).filter(User.email == request.email).first()

    if exesting_user:
        raise HTTPException(status_code=422, details= "Email already exist.")
    
    user = User(
        name = request.name,
        email = request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

@router.put("/{user_id}")
def update(user_id: int, data: UserSchema, db = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code= 404,details= "ID not Found.")
    
    exesting_user = db.query(User).filter(
        User.email == data.email,
        User.id != user_id
    ).first()
    
    if exesting_user:
        raise HTTPException(status= 404, deails= "email does't exists.")
    
    user.name = data.name
    user.email = data.email

    db.commit()
    db.refresh(user)
    
    return user

@router.delete("/{user_id}")
def delete(user_id: int, db = Depends(get_db)):
    user = db.query(User).filter (User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="ID does't exists")
    
    db.delete(user)
    db.commit()
    
    return user
