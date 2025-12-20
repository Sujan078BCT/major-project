from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Use MySQL connector
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'mysql+mysqlconnector://root:1234@localhost:3306/nutrifit'
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
