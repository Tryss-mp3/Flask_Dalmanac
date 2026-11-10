from modelos.usuario import Usuario

def buscar_por_email(email):
    return Usuario.query.filter_by(email=email).first()

def buscar_por_id(usuario_id):
    return Usuario.query.get(usuario_id)

def salvar(usuario):
    from banco import bd
    bd.session.add(usuario)
    bd.session.commit()
    return usuario
