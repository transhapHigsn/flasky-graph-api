from sqlalchemy import create_engine as ca
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = ca("postgresql+psycopg2://postgres:postgres@localhost:5432/demo")
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Representation(Base):
    __tablename__ = 'graphs'

    id = Column(Integer, primary_key = True)
    nodes = Column(String, nullable=False)
    edges = Column(String, nullable=False)

    def __init__(self, nodes, edges, id):
        self.id = id
        self.nodes = nodes
        self.edges = edges

Base.metadata.create_all(engine)
#session = sessionmaker()
