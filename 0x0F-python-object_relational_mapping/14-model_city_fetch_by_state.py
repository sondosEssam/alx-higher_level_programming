#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv as a
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{a[1]}:{a[2]}@localhost/{a[3]}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    for obh in (session.query(State.name, City.id, City.name)
                .filter(State.id == City.state_id)):
        print(f"{obh[0]}: ({obh[2]}) {obh[1]}")
