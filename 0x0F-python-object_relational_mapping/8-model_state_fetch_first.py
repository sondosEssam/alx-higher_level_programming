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
    sataes = session.query(State).first()
    if sataes is not None:
        print(f"{sataes.id}: {sataes.name}")
    else:
        print("Nothing")
