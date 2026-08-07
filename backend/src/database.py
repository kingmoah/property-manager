from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


class Database:

    def __init__(self, database_url):

        self.engine = create_engine(
            database_url,
            pool_pre_ping=True
        )

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False
        )

    @contextmanager
    def session(self):

        session = self.SessionLocal()

        try:
            yield session
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()