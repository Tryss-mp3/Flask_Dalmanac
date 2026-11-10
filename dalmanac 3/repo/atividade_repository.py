from banco import bd
from modelos.atividade import Atividade

def listar_por_jogo(jogo_id):
    return Atividade.query.filter_by(jogo_id=jogo_id).order_by(
        Atividade.data_criacao.desc()
    ).all()

def salvar(atividade):
    bd.session.add(atividade)
    bd.session.commit()
    return atividade
