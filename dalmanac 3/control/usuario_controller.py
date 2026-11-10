from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from srvcs import usuario_service

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/")
def pagina_inicial():
    if "usuario_id" in session:
        return redirect(url_for("jogo.inicio"))
    return redirect(url_for("usuario.login"))

@usuario_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        usuario, erro = usuario_service.cadastrar_usuario(
            request.form.get("nome", ""),
            request.form.get("email", "").lower().strip(),
            request.form.get("senha", "")
        )

        if erro:
            flash(erro, "erro")
        else:
            flash("Conta criada. Faça login para continuar.", "sucesso")
            return redirect(url_for("usuario.login"))

    return render_template("cadastro.html")

@usuario_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = usuario_service.verificar_login(
            request.form.get("email", "").lower().strip(),
            request.form.get("senha", "")
        )

        if usuario:
            session["usuario_id"] = usuario.id
            session["usuario_nome"] = usuario.nome
            return redirect(url_for("jogo.inicio"))

        flash("E-mail ou senha incorretos.", "erro")

    return render_template("login.html")

@usuario_bp.route("/sair")
def sair():
    session.clear()
    return redirect(url_for("usuario.login"))




