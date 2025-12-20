from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import models
from database import SessionLocal, engine
from crud import user_create, user_get, check_email, check_username, user_update
from schemas import UserCreate, User, UserUpdate, UserResponse
from utilis import create_access_token, verify_password, verify_token
from sqlalchemy.orm import Session
from database import engine
from sqlalchemy import text

app = FastAPI()


try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("DB connected:", result.fetchone())
except Exception as e:
    print("DB connection failed:", e)


# Create tables
@app.on_event("startup")
def startup_event():
    try:
        models.Base.metadata.create_all(bind=engine)
        print("Tables created successfully")
    except Exception as e:
        print("Database connection failed:", e)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Current user dependency
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    username = payload.get("sub")
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user

# Root
@app.get("/")
def root():
    return {"message": "login to /docs for api documentation"}

# Register
@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_create(db, user)
    token = create_access_token(data={"sub": db_user.username})
    return {
        "id": db_user.id,
        "first_name": db_user.first_name,
        "last_name": db_user.last_name,
        "username": db_user.username,
        "email": db_user.email,
        "access_token": token,
        "token_type": "bearer"
    }

# Login
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if db_user and verify_password(form_data.password, db_user.password_hash):
        token = create_access_token(data={"sub": db_user.username})
        return {"access_token": token, "token_type": "bearer", "user_id": db_user.id}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

# Email check
@app.get("/users/emails/{user_email}")
def user_email(user_email: str, db: Session = Depends(get_db)):
    return {"emailPresent": bool(check_email(db, user_email))}

# Username check
@app.get("/users/usernames/{user_username}")
def user_username(user_username: str, db: Session = Depends(get_db)):
    return {"usernamePresent": bool(check_username(db, user_username))}

# Get user details
@app.get("/users/{user_id}", response_model=User)
def user_get_details(user_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    user = user_get(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update user
@app.put("/users/{user_id}", response_model=User)
def edit_user(user_id: int, user: UserUpdate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
    return user_update(db, user_id, user)
