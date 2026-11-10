from banco import bd
from datetime import datetime

class Atividade(bd.Model):
    __tablename__ = "atividades"

    id = bd.Column(bd.Integer, primary_key=True)
    descricao = bd.Column(bd.String(250), nullable=False)
    data_criacao = bd.Column(bd.DateTime, default=datetime.now, nullable=False)
    jogo_id = bd.Column(bd.Integer, bd.ForeignKey("jogos.id"), nullable=False)

