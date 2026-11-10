from banco import bd
from modelos.estatistica import Estatistica

def listar_por_jogo(jogo_id):
    return Estatistica.query.filter_by(jogo_id=jogo_id).all()

def salvar(estatistica):
    bd.session.add(estatistica)
    bd.session.commit()
    return estatistica

def excluir(estatistica):
    bd.session.delete(estatistica)
    bd.session.commit()
