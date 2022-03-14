
from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import (String, Boolean, Column, DateTime, ForeignKey,
                        Index, Integer, Sequence, Text, Unicode, func,
                        )
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship

from db import Base


class Journals(Base):
    __tablename__ = 'journals'


    Journals_id = Sequence('Journals_id', metadata=Base.metadata)
    id = Column(Integer,Journals_id, primary_key=True, index=True)
    name = Column(String(300), nullable=False , collation='th_TH')

class Register(Base):
    __tablename__ = 'register'
    Register_id = Sequence('Register_id', metadata=Base.metadata)
    id = Column(Integer,Register_id, index=True ,primary_key=True  )
    round_id = Column(Integer, unique=True , nullable=False)
    trainee_id = Column(Integer, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), server_default=func.now(),
                        server_onupdate=FetchedValue(), onupdate=func.now())

    journals = relationship('journals')

class Rounds(Base):
    __tablename__ = 'rounds'

    Rounds_id = Sequence('Rounds_id', metadata=Base.metadata)
    id = Column(Integer,Rounds_id, index=True ,primary_key=True )
    label = Column(String(255), nullable=False ,  collation='th_TH')
    batch = Column(Integer, nullable=False )
    location = Column(String(300), nullable=False ,  collation='th_TH')
    map = Column(String(30), nullable=False ,  collation='th_TH')
    max_trainee = Column(Integer,nullable=False, default=10)
    close = Column(Integer, nullable=False, default=0)
    display = Column(Integer, nullable=False, default=1)
    datetime = Column(DateTime(timezone=True), server_default=func.now())
    datetime_end = Column(DateTime(timezone=True), server_default=func.now())


    journals = relationship('journals')

class Trainee_info(Base):
    __tablename__ = 'trainee_info'
    trainee_info = Sequence('trainee_info', metadata=Base.metadata)
    id = Column(Integer ,trainee_info, index=True , primary_key=True )
    full_name = Column(String(255), nullable=False , collation='th_TH')
    telephone = Column(String(50), nullable=False , collation='th_TH')
    email = Column(String(100), nullable=False , collation='th_TH')
    bill_info = Column(Text, nullable=False , collation='th_TH') 
    trainee = Column(Integer, nullable=False)
    journal_id = Column(Integer, nullable=False)
    trainee_list = Column(Text, nullable=False , collation='th_TH')
    tax_id = Column(String(16), default=0, nullable=True , collation='th_TH')
    sent_bill = Column(Integer, default=0, nullable=False)
    status = Column(Integer,default=0)

    journals = relationship('journals')




class Trainee_infoBase(BaseModel):
    
    full_name: Optional[str]
    telephone: Optional[str]
    email: Optional[str]
    
    tax_id : Optional[str]
    
    
    

    class Config:
        orm_model = True

class RegisterUpdate(BaseModel):
    id: int 
    full_name: Optional[str] = None

    telephone: Optional[str] = None
    email: Optional[str] = None
    
    tax_id : Optional[str] = None


    class Config:
        orm_model = True


class RegisterID(Trainee_infoBase):
    id: int
    round_id: int
    trainee_id: int
    created_at: datetime = None
    updated_at: datetime = None
   

    class Config:
        orm_model = True

class RoundsBase(BaseModel):
    id: int
    label: str
    batch: str
    location: str
    map: str
    max_trainee: str
    close: str
    display: str
    

    class Config:
        orm_model = True


