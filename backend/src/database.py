from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = None
SessionLocal = None


def initialize_database(database_url: str):
    global engine
    global SessionLocal

    engine = create_engine(
        database_url,
        pool_pre_ping=True
    )

    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )