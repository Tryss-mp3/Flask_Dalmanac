from banco import bd

class Marco(bd.Model):
    __tablename__ = "marcos"

    id = bd.Column(bd.Integer, primary_key=True)
    titulo = bd.Column(bd.String(120), nullable=False)
    descricao = bd.Column(bd.Text)
    concluido = bd.Column(bd.Boolean, default=False, nullable=False)
    jogo_id = bd.Column(bd.Integer, bd.ForeignKey("jogos.id"), nullable=False)
