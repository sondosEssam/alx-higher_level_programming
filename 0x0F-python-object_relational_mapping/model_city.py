#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from model_state import Base, State


class City(Base):
    """
    class
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("State.id"), nullable=False)
