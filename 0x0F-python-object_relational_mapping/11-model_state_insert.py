#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv as a
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{a[1]}:{a[2]}@localhost/{a[3]}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name="Louisiana"))
    session.commit()
    new_state = session.query(State).filter(State.name == "Louisiana").first()
    print(new_state.id)
