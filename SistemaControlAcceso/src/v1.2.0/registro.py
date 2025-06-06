# Versión 1.2.0 - 2025-04-18
def registrar_usuario(usuario, contrasena):
    with open('usuarios.txt', 'a') as f:
        f.write(f'{usuario},{contrasena}\n')
