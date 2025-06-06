# Versión 1.1.0 - 2025-04-10
def autenticar(usuario, contrasena):
    usuarios = {'admin': '1234', 'invitado': 'abcd'}
    return usuarios.get(usuario) == contrasena
