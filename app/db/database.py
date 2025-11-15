from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models import Base


SQLALCHEMY_DATABASE_URL = "sqlite:///./repayment.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from app.db.models import RepaymentRecord
from sqlalchemy.orm import Session

def get_all_records(db: Session):
    return db.query(RepaymentRecord).order_by(RepaymentRecord.id.desc()).all()

DATABASE_URL = "sqlite:///repayment.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

