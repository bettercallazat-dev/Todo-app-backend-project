from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

setings = get_settings()
engine = create_engine(setings.DATABASE_URL)
Sessionlocal = sessionmaker(bind=engine)


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
