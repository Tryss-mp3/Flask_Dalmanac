from flask import Flask
from config import Config
from banco import bd

                                                      
from control.usuario_controller import usuario_bp
from control.jogo_controller import jogo_bp
from control.marco_controller import marco_bp

def criar_app():
    app = Flask(__name__, static_folder="css")
    app.config.from_object(Config)

                                    
    bd.init_app(app)

                                           
    app.register_blueprint(usuario_bp)
    app.register_blueprint(jogo_bp)
    app.register_blueprint(marco_bp)

                                                    
    with app.app_context():
        from modelos.usuario import Usuario
        from modelos.jogo import Jogo
        from modelos.marco import Marco
        from modelos.atividade import Atividade
        from modelos.estatistica import Estatistica

        bd.create_all()

    return app

app = criar_app()

if __name__ == "__main__":
    app.run(debug=True)
