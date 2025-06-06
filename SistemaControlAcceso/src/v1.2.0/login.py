# Versión 1.2.0 - 2025-04-18
def autenticar(usuario, contrasena):
    try:
        with open('usuarios.txt') as f:
            for linea in f:
                u, c = linea.strip().split(',')
                if usuario == u and contrasena == c:
                    return True
        return False
    except FileNotFoundError:
        return False
