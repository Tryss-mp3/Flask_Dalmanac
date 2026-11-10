from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from functools import wraps
from repo import jogo_repository, marco_repository, atividade_repository, estatistica_repository
from srvcs import jogo_service

jogo_bp = Blueprint("jogo", __name__)

                                                                        
def login_obrigatorio(funcao):
    @wraps(funcao)
    def verificar_login(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Faça login para acessar sua biblioteca.", "erro")
            return redirect(url_for("usuario.login"))
        return funcao(*args, **kwargs)
    return verificar_login

@jogo_bp.route("/inicio")
@login_obrigatorio
def inicio():
    jogos = jogo_repository.listar_por_usuario(
        session["usuario_id"],
        request.args.get("status"),
        request.args.get("genero"),
        request.args.get("plataforma")
    )
    return render_template("inicio.html", jogos=jogos)

@jogo_bp.route("/jogos/adicionar", methods=["GET", "POST"])
@login_obrigatorio
def adicionar():
    if request.method == "POST":
        jogo, erro = jogo_service.adicionar_jogo(request.form, session["usuario_id"])
        if erro:
            flash(erro, "erro")
        else:
            flash("Jogo adicionado à biblioteca.", "sucesso")
            return redirect(url_for("jogo.inicio"))

    return render_template("formulario_jogo.html", jogo=None)

@jogo_bp.route("/jogos/<int:jogo_id>")
@login_obrigatorio
def detalhes(jogo_id):
    jogo = jogo_repository.buscar_por_id_e_usuario(jogo_id, session["usuario_id"])
    if not jogo:
        flash("Jogo não encontrado.", "erro")
        return redirect(url_for("jogo.inicio"))

    marcos = marco_repository.listar_por_jogo(jogo.id)
    atividades = atividade_repository.listar_por_jogo(jogo.id)
    estatisticas = estatistica_repository.listar_por_jogo(jogo.id)

                                                          
    mostrar_ocultos = request.args.get("revelar") == "sim"
    return render_template(
        "detalhes_jogo.html",
        jogo=jogo,
        marcos=marcos,
        atividades=atividades,
        estatisticas=estatisticas,
        mostrar_ocultos=mostrar_ocultos
    )

@jogo_bp.route("/jogos/<int:jogo_id>/editar", methods=["GET", "POST"])
@login_obrigatorio
def editar(jogo_id):
    jogo = jogo_repository.buscar_por_id_e_usuario(jogo_id, session["usuario_id"])
    if not jogo:
        flash("Jogo não encontrado.", "erro")
        return redirect(url_for("jogo.inicio"))

    if request.method == "POST":
        erro = jogo_service.atualizar_jogo(jogo, request.form)
        if erro:
            flash(erro, "erro")
        else:
            flash("Jogo atualizado.", "sucesso")
            return redirect(url_for("jogo.detalhes", jogo_id=jogo.id))

    return render_template("formulario_jogo.html", jogo=jogo)

@jogo_bp.route("/jogos/<int:jogo_id>/progresso", methods=["POST"])
@login_obrigatorio
def progresso(jogo_id):
    jogo = jogo_repository.buscar_por_id_e_usuario(jogo_id, session["usuario_id"])
    if not jogo:
        flash("Jogo não encontrado.", "erro")
        return redirect(url_for("jogo.inicio"))

    erro = jogo_service.atualizar_progresso(
        jogo, request.form.get("tempo_jogado"), request.form.get("progresso")
    )
    flash(erro or "Progresso atualizado.", "erro" if erro else "sucesso")
    return redirect(url_for("jogo.detalhes", jogo_id=jogo.id))

@jogo_bp.route("/jogos/<int:jogo_id>/excluir", methods=["POST"])
@login_obrigatorio
def excluir(jogo_id):
    jogo = jogo_repository.buscar_por_id_e_usuario(jogo_id, session["usuario_id"])
    if jogo:
        jogo_repository.excluir(jogo)
        flash("Jogo removido.", "sucesso")
    return redirect(url_for("jogo.inicio"))

@jogo_bp.route("/jogos/<int:jogo_id>/estatisticas", methods=["POST"])
@login_obrigatorio
def estatistica(jogo_id):
    jogo = jogo_repository.buscar_por_id_e_usuario(jogo_id, session["usuario_id"])
    if not jogo:
        flash("Jogo não encontrado.", "erro")
        return redirect(url_for("jogo.inicio"))

    erro = jogo_service.adicionar_estatistica(
        jogo.id, request.form.get("nome", ""), request.form.get("valor", "")
    )
    flash(erro or "Estatística cadastrada.", "erro" if erro else "sucesso")
    return redirect(url_for("jogo.detalhes", jogo_id=jogo.id))