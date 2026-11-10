from modelos.jogo import Jogo
from modelos.atividade import Atividade
from modelos.estatistica import Estatistica
from repo import jogo_repository, atividade_repository, estatistica_repository

STATUS_VALIDOS = ["Quero jogar", "Jogando", "Pausado", "Concluído"]

def adicionar_jogo(dados, usuario_id):
    titulo = dados.get("titulo", "").strip()
    genero = dados.get("genero", "").strip()
    plataforma = dados.get("plataforma", "").strip()
    status = dados.get("status", "Quero jogar")

    if not titulo or not genero or not plataforma:
        return None, "Preencha título, gênero e plataforma."

    if status not in STATUS_VALIDOS:
        return None, "Status inválido."

    jogo = Jogo(
        titulo=titulo,
        genero=genero,
        plataforma=plataforma,
        status=status,
        descricao=dados.get("descricao", "").strip(),
        usuario_id=usuario_id
    )
    jogo_repository.salvar(jogo)
    registrar_atividade(jogo.id, "Jogo adicionado à biblioteca.")
    return jogo, None

def atualizar_jogo(jogo, dados):
    titulo = dados.get("titulo", "").strip()
    genero = dados.get("genero", "").strip()
    plataforma = dados.get("plataforma", "").strip()
    status = dados.get("status", "")

    if not titulo or not genero or not plataforma:
        return "Preencha título, gênero e plataforma."

    if status not in STATUS_VALIDOS:
        return "Status inválido."

    jogo.titulo = titulo
    jogo.genero = genero
    jogo.plataforma = plataforma
    jogo.status = status
    jogo.descricao = dados.get("descricao", "").strip()
    jogo_repository.salvar(jogo)
    registrar_atividade(jogo.id, "Informações do jogo atualizadas.")
    return None

def atualizar_progresso(jogo, tempo, progresso):
    try:
        tempo = float(tempo)
        progresso = int(progresso)
    except (ValueError, TypeError):
        return "Informe números válidos para tempo e progresso."

    if tempo < 0 or progresso < 0 or progresso > 100:
        return "O tempo não pode ser negativo e o progresso deve ficar entre 0 e 100."

    jogo.tempo_jogado = tempo
    jogo.progresso = progresso

    if progresso == 100:
        jogo.status = "Concluído"

    jogo_repository.salvar(jogo)
    registrar_atividade(jogo.id, "Progresso atualizado.")
    return None

def registrar_atividade(jogo_id, descricao):
    atividade = Atividade(jogo_id=jogo_id, descricao=descricao)
    atividade_repository.salvar(atividade)

def adicionar_estatistica(jogo_id, nome, valor):
    if not nome.strip() or not valor.strip():
        return "Preencha o nome e o valor da estatística."

    estatistica = Estatistica(jogo_id=jogo_id, nome=nome.strip(), valor=valor.strip())
    estatistica_repository.salvar(estatistica)
    registrar_atividade(jogo_id, "Nova estatística cadastrada.")
    return None
