
# administrador.py
class AdministradorUsuarios:
    def __init__(self):
        self.usuarios = {"admin": "admin_pass"}  # Usuario admin por defecto

    def registrar_usuario(self, username, password):
        if username in self.usuarios:
            return False  # El usuario ya existe
        else:
            self.usuarios[username] = password
            return True  # Registro exitoso

    def autenticar_usuario(self, username, password):
        if username not in self.usuarios:
            return None  # Usuario no registrado
        return self.usuarios.get(username) == password
