# Vamos a crear tres clases 
# Guardar = deberia añadir un usuario y editar un usuario 
# Login = metodo que necesite el email y contraseña y validar el email es el correcto / email: user@gmail.com/ contraseña: 1234
# Usuario = debe poder añadir un usuario y hacer login

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
    

class Login:
    def login(self, email, contraseña):
        if email not in self.usuarios:
            return "Email no registrado"
        if self.usuarios[email] != contraseña:
            return "Contraseña incorrecta"
        return "Login realizado con éxito"
    
class Usuario(Guardar, Login):
    def __init__(self):
        super().__int__()

app = Usuario()

print(app.añadir_usuario("user@gmail.com", "1234"))
print(app.login("user@gmail.com", "1234"))

print(app.editar_usuario("user@gmail.com", "abcd"))
print(app.login("user@gmail.com", "abcd"))

# cambios de la rama