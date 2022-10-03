#!/usr/bin/python3
""" retrieves all cities and states """

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    from model_city import City

    # open a connection
    engine = create_engine('mysql+mysqldb://'
                           '{0.argv[1]}:{0.argv[2]}@localhost/{0.argv[3]}'
                           .format(sys))

    # send city schema to create or update table in db
    Base.metadata.create_all(engine)
    # use connection
    Session = sessionmaker(bind=engine)
    session = Session()  # session instance

    # using join to retrieve city and state
    sn = State.name
    si = State.id
    cs = City.state_id
    for city, state in session.query(City, sn).join(State, si == cs):
        print("{1}: ({0.id}) {0.name}".format(city, state))
