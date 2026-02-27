
class Guardar:
    def __int__(self):
        self.usuarios = {}

    def añadir_usuario(self, email, contraseña):
        if email in self.usuarios:
            return "El usuario ya existe"
        self.usuarios[email] = contraseña
        return "El usuario se ha añadido con éxito"
    
    def editar_usuario(self, email, nueva_contraseña):
        if email not in self.usuarios:
            return "El usuario no existe"
        self.usuarios[email] = nueva_contraseña
        return "Contraseña actualizada con éxito"
    
