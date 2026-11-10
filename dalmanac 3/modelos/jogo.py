from banco import bd

class Jogo(bd.Model):
    __tablename__ = "jogos"

    id = bd.Column(bd.Integer, primary_key=True)
    titulo = bd.Column(bd.String(120), nullable=False)
    genero = bd.Column(bd.String(60), nullable=False)
    plataforma = bd.Column(bd.String(60), nullable=False)
    status = bd.Column(bd.String(30), nullable=False, default="Quero jogar")
    tempo_jogado = bd.Column(bd.Float, nullable=False, default=0)
    progresso = bd.Column(bd.Integer, nullable=False, default=0)
    descricao = bd.Column(bd.Text)
    usuario_id = bd.Column(bd.Integer, bd.ForeignKey("usuarios.id"), nullable=False)

    marcos = bd.relationship("Marco", backref="jogo", cascade="all, delete-orphan")
    atividades = bd.relationship("Atividade", backref="jogo", cascade="all, delete-orphan")
    estatisticas = bd.relationship("Estatistica", backref="jogo", cascade="all, delete-orphan")
