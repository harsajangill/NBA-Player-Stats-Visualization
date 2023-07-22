from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URI_WRITER, DATABASE_URI_READER

engine_writer = create_engine(DATABASE_URI_WRITER)
engine_reader = create_engine(DATABASE_URI_READER)
SessionWriter = sessionmaker(bind=engine_writer)
SessionReader = sessionmaker(bind=engine_reader)
Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'
    __table_args__ = {'schema': 'nba_player_stats'}
    id = Column(Integer, primary_key=True)
    dataset = Column(String(255))
    game_id = Column(String(255))
    date = Column(String(255))
    player_id = Column(String(255))
    player_name = Column(String(255))
    position = Column(String(255))
    own_team = Column(String(255))
    opponent_team = Column(String(255))
    fg = Column(Float)
    fga = Column(Float)
    _3p = Column(Float)
    _3pa = Column(Float)
    ft = Column(Float)
    fta = Column(Float)
    or_ = Column(Float)
    dr = Column(Float)
    tot = Column(Float)
    a = Column(Float)
    pf = Column(Float)
    st = Column(Float)
    to = Column(Float)
    bl = Column(Float)
    pts = Column(Float)
