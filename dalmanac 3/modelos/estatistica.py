from banco import bd

class Estatistica(bd.Model):
    __tablename__ = "estatisticas"

    id = bd.Column(bd.Integer, primary_key=True)
    nome = bd.Column(bd.String(100), nullable=False)
    valor = bd.Column(bd.String(150), nullable=False)
    jogo_id = bd.Column(bd.Integer, bd.ForeignKey("jogos.id"), nullable=False)
