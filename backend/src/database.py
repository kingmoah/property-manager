from sqlachemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = None
SessionLocal = None

def initialize_database(database_irl:str):
    global engine
    global Sessionocal

    engine = create_engine(
        database_url, pool_pre_ping
    )

    SessionLocal = sessionmaker(
        autocommit= False,
        autoFlash=False,
        bind=engine
    )
