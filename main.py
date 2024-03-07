from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
import re
from models import get_engine, Usuario, Token
from secrets import token_hex

app = FastAPI()

def conecta_banco():
    engine = get_engine()
    Session = sessionmaker(engine)
    return Session()

def valida_senha(senha):
    regex_senha = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@!])[\w@!]{6,}$"

    if re.match(regex_senha, senha):
        return True
    else:
        return False

@app.post('/cadastro')
def cadastro(nome:str, usuario:str, senha:str):
    session = conecta_banco()
    existe_usuario = session.query(Usuario).filter_by(usuario=usuario, senha=senha).all()
    if len(existe_usuario) == 0:
        if valida_senha(senha):
            x = Usuario(nome=nome, usuario=usuario, senha=senha)
            session.add(x)
            session.commit()
            return {'status': 'Usuário cadastrado com sucesso!'}
        else:
            return {'status': 'Cadastre uma senha mais forte.'}
    elif len(existe_usuario) > 0:
        return {'status': 'Usuário já cadastrado'}


@app.post('/login')
def login(usuario:str, senha:str):
    session = conecta_banco()
    existe_usuario = session.query(Usuario).filter_by(usuario=usuario, senha=senha).first()
    if not existe_usuario:
        return {'status': 'Usuário inexistente'}

    while True:
        token = token_hex(50)
        existe_token = session.query(Token).filter_by(token=token).all()

        if len(existe_token) == 0:
            existe_pessoa = session.query(Token).filter_by(id_usuario=existe_usuario.id).first()
            if not existe_pessoa:
                novo_token = Token(id_usuario=existe_usuario.id, token=token)
                session.add(novo_token)

            elif existe_pessoa:
                existe_pessoa.token = token

            session.commit()
            break

    return token
