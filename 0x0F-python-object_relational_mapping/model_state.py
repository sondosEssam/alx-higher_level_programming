#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class State(Base):
    """
    class
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
