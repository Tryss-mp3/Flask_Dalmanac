from werkzeug.security import generate_password_hash, check_password_hash
from modelos.usuario import Usuario
from repo import usuario_repository

def cadastrar_usuario(nome, email, senha):
    if not nome or not email or not senha:
        return None, "Preencha todos os campos."

    if usuario_repository.buscar_por_email(email):
        return None, "Este e-mail já está cadastrado."

    senha_criptografada = generate_password_hash(senha)
    usuario = Usuario(nome=nome, email=email, senha=senha_criptografada)
    usuario_repository.salvar(usuario)
    return usuario, None

def verificar_login(email, senha):
    usuario = usuario_repository.buscar_por_email(email)

    if usuario and check_password_hash(usuario.senha, senha):
        return usuario

    return None
