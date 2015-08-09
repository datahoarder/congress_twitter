# An early attempt at using SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import Integer, String
from settings import PACKAGED_DIR

engine = create_engine('sqlite:///' + PACKAGED_DIR)
