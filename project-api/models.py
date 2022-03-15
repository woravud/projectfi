

from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import (String, Boolean, Column, DateTime, ForeignKey,
                        Index, Integer, Sequence, Text, Unicode,func,
                        text )
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship

from db import Base


class Journals(Base):
    __tablename__ = 'journals'


    Journals_id_seq = Sequence('Journals_id_seq', metadata=Base.metadata)
    id = Column(Integer,Journals_id_seq, primary_key=True, index=True)
    name = Column(String(300,collation='th_TH'), nullable=False )

    @declared_attr
    def trainee_info_id(cls):
        return Column(Integer, ForeignKey("trainee_info.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False, unique=False, index=True)

class Register(Base):
    __tablename__ = 'register'
    Register_id_seq = Sequence('Register_id_seq', metadata=Base.metadata)
    id = Column(Integer,Register_id_seq, index=True ,primary_key=True  )
    round_id = Column(Integer, unique=True , nullable=False)
    trainee_id = Column(Integer, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), server_default=func.now(),
                        server_onupdate=FetchedValue(), onupdate=func.now())

    
    @declared_attr
    def trainee_info_id(cls):
        return Column(Integer, ForeignKey("trainee_info.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False, unique=False, index=True)
class Rounds(Base):
    __tablename__ = 'rounds'

    Rounds_id = Sequence('Rounds_id', metadata=Base.metadata)
    id = Column(Integer,Rounds_id, index=True ,primary_key=True )
    label = Column(String(255,collation='th_TH'), nullable=False ,  )
    batch = Column(Integer, nullable=False )
    location = Column(String(300,collation='th_TH'), nullable=False ,  )
    map = Column(String(30,collation='th_TH'), nullable=False  )
    max_trainee = Column(Integer,nullable=False, default=10)
    close = Column(Integer, nullable=False, default=0)
    display = Column(Integer, nullable=False, default=1)
    datetime = Column(DateTime(timezone=True), server_default=func.now())
    datetime_end = Column(DateTime(timezone=True), server_default=func.now())


    @declared_attr
    def trainee_info_id(cls):
        return Column(Integer, ForeignKey("trainee_info.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False, unique=False, index=True)

class Trainee_info(Base):
    __tablename__  = 'trainee_info'
    
    trainee_info_seq = Sequence('trainee_info_seq', metadata=Base.metadata)
    id = Column(Integer ,trainee_info_seq, index=True , primary_key=True )
    full_name = Column(String(255,collation='th_TH'), nullable=False )
    telephone = Column(String(50,collation='th_TH'), nullable=False )
    email = Column(String(100,collation='th_TH'), nullable=False )
    bill_info = Column(Text, nullable=False ) 
    trainee = Column(Integer, nullable=False)
    journal_id = Column(Integer, nullable=False)
    trainee_list = Column(Text, nullable=False )
    tax_id = Column(String(16,collation='th_TH'), nullable=True)
    sent_bill = Column(Integer, default=0, nullable=False)
    status = Column(Integer,default=0)
    disabled = Column(Boolean, nullable=True, server_default=text("False"))

trainee_info = relationship('journals')   




class Trainee_infobase(BaseModel):
    status  :Optional[int]
    full_name: Optional[str]
    telephone: Optional[str]
    email: Optional[str]
    bill_info: Optional[str]
    trainee : Optional[int]
    trainee_list :Optional[str] 
    sent_bill :Optional[int]
    
    journal_id: Optional[int]
    tax_id : Optional[str]
    
    
    

    class Config:
        orm_model = True

class RegisterUpdate(BaseModel):
    id: int 
    full_name: Optional[str] = None
    journal_id: Optional[int] = None
    telephone: Optional[str] = None
    email: Optional[str] = None
    bill_info: Optional[str] = None
    trainee : Optional[int] = None
    tax_id : Optional[str] = None
    disabled: Optional[bool] = False
    trainee_list :Optional[str] = None
    status  :Optional[int] = None
    sent_bill :Optional[int] = None


    class Config:
        orm_model = True


class RegisterID(Trainee_infobase):
    id: int
    
    created_at: datetime = None 
    
    updated_at: datetime  = None
   

    class Config:
        orm_model = True

class Roundsbase(BaseModel):
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


