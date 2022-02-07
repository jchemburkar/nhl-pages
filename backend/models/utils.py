''' utils for maintaining database with sqlalchemy '''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database

DATABASE = "nhl"
URL = f"mysql+pymysql://root:beans@mysql:3306/{DATABASE}"

# add `nhl` database by default if it doesn't exist
if not database_exists(URL):
    # TODO: make this a logging statement
    print("Creating `nhl` database")
    create_database(URL)

ENGINE = create_engine('mysql+pymysql://root:beans@mysql:3306', echo=False)
BASE = declarative_base(bind=ENGINE)



def get_session():
    '''
    gets a sqlalchemy session -- useful for interfacing with the database
    Docs: https://docs.sqlalchemy.org/en/13/orm/session.html
    '''
    return Session(bind=ENGINE)
