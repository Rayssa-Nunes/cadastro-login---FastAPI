from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    USUARIO = os.getenv('USUARIO')
    SENHA = os.getenv('SENHA')
    BANCO = os.getenv('BANCO')
    HOST = 'localhost'
    PORT = 5432

    return create_engine(f'postgresql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}', echo=True)

engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    usuario = Column(String)
    senha = Column(String)


class Token(Base):
    __tablename__ = 'token'
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String)
    data = Column(DateTime, default=datetime.now())
    id_usuario = Column(Integer, ForeignKey('usuario.id'))



Base.metadata.create_all(engine)


