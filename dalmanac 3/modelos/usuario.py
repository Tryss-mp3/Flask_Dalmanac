from banco import bd

class Usuario(bd.Model):
    __tablename__ = "usuarios"

    id = bd.Column(bd.Integer, primary_key=True)
    nome = bd.Column(bd.String(100), nullable=False)
    email = bd.Column(bd.String(120), unique=True, nullable=False)
    senha = bd.Column(bd.String(255), nullable=False)

                                           
    jogos = bd.relationship("Jogo", backref="usuario", cascade="all, delete-orphan")
