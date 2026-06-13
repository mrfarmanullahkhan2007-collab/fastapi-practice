from app.database import SessionLoal

def get_db():
    db = SessionLoal()
    print ("Before Yield.")
    yield db
    print ("After Yield.")
    db.close()