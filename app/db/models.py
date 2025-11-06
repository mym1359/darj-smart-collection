from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RepaymentRecord(Base):
    __tablename__ = "repayment_records"

    id = Column(Integer, primary_key=True, index=True)
    delay_days = Column(Integer)
    contact_count = Column(Integer)
    promise_given = Column(Boolean)
    promise_kept = Column(Boolean)
    recommended_action = Column(String)