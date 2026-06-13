from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    url = "sqlite:///database_v01.db",
    connect_args = {"check_same_thread" : False}
)

SessionLoal = sessionmaker(
    bind = engine,
    autoflush = False,
    autocommit = False
)

Base = declarative_base()