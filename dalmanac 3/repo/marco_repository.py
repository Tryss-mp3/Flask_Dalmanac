from banco import bd
from modelos.marco import Marco

def listar_por_jogo(jogo_id):
    return Marco.query.filter_by(jogo_id=jogo_id).all()

def buscar_por_id(marco_id):
    return Marco.query.get(marco_id)

def salvar(marco):
    bd.session.add(marco)
    bd.session.commit()
    return marco

def excluir(marco):
    bd.session.delete(marco)
    bd.session.commit()
