from modelos.marco import Marco
from repo import marco_repository
from srvcs.jogo_service import registrar_atividade

def adicionar_marco(jogo_id, titulo, descricao):
    if not titulo.strip():
        return "Informe o título do marco."

    marco = Marco(
        jogo_id=jogo_id,
        titulo=titulo.strip(),
        descricao=descricao.strip(),
        concluido=False
    )
    marco_repository.salvar(marco)
    registrar_atividade(jogo_id, "Novo marco cadastrado.")
    return None

def alternar_conclusao(marco):
    marco.concluido = not marco.concluido
    marco_repository.salvar(marco)
    registrar_atividade(marco.jogo_id, "Status de um marco atualizado.")
