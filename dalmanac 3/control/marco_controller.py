from flask import Blueprint, request, redirect, url_for, session, flash
from control.jogo_controller import login_obrigatorio
from repo import jogo_repository, marco_repository
from srvcs import marco_service

marco_bp = Blueprint("marco", __name__)

@marco_bp.route("/jogos/<int:jogo_id>/marcos", methods=["POST"])
@login_obrigatorio
def adicionar(jogo_id):
    jogo = jogo_repository.buscar_por_id_e_usuario(jogo_id, session["usuario_id"])
    if not jogo:
        flash("Jogo não encontrado.", "erro")
        return redirect(url_for("jogo.inicio"))

    erro = marco_service.adicionar_marco(
        jogo.id,
        request.form.get("titulo", ""),
        request.form.get("descricao", "")
    )
    flash(erro or "Marco cadastrado.", "erro" if erro else "sucesso")
    return redirect(url_for("jogo.detalhes", jogo_id=jogo.id))

@marco_bp.route("/marcos/<int:marco_id>/alternar", methods=["POST"])
@login_obrigatorio
def alternar(marco_id):
    marco = marco_repository.buscar_por_id(marco_id)

    if not marco:
        flash("Marco não encontrado.", "erro")
        return redirect(url_for("jogo.inicio"))

    jogo = jogo_repository.buscar_por_id_e_usuario(marco.jogo_id, session["usuario_id"])
    if not jogo:
        flash("Você não tem acesso a este marco.", "erro")
        return redirect(url_for("jogo.inicio"))

    marco_service.alternar_conclusao(marco)
    return redirect(url_for("jogo.detalhes", jogo_id=jogo.id))