from banco import bd
from modelos.jogo import Jogo

def listar_por_usuario(usuario_id, status=None, genero=None, plataforma=None):
    consulta = Jogo.query.filter_by(usuario_id=usuario_id)

    if status:
        consulta = consulta.filter_by(status=status)
    if genero:
        consulta = consulta.filter_by(genero=genero)
    if plataforma:
        consulta = consulta.filter_by(plataforma=plataforma)

    return consulta.order_by(Jogo.titulo).all()

def buscar_por_id_e_usuario(jogo_id, usuario_id):
    return Jogo.query.filter_by(id=jogo_id, usuario_id=usuario_id).first()

def salvar(jogo):
    bd.session.add(jogo)
    bd.session.commit()
    return jogo

def excluir(jogo):
    bd.session.delete(jogo)
    bd.session.commit()
