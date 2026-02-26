# Vamos a crear tres clases  
# Guardar -- añadir usuario, editar usuario  
# Login – metodo(email y contraseña) --> email: user@gmail.com, pass: 1234  
# Usuario -- debe poder añadir un usuario y hacer login



class Guardar:
    def __init__(self):
        self.usuarios = {}   

    def añadir_usuario(self, email, contraseña):
        if email in self.usuarios:
            return "El usuario ya existe"
        self.usuarios[email] = contraseña
        return "Usuario añadido correctamente"

    def editar_usuario(self, email, nueva_contraseña):
        if email not in self.usuarios:
            return "El usuario no existe"
        self.usuarios[email] = nueva_contraseña
        return "Contraseña actualizada"
        

class Login:
    def login(self, email, contraseña):
        if email == "user@gmail.com" and contraseña == "1234":
            return True
        return False


class Usuario(Guardar, Login):
    def __init__(self):
        super().__init__()

    def crear_y_login(self, email, contraseña):
        self.añadir_usuario(email, contraseña)
        return self.login(email, contraseña)



usu = Usuario()

print(usu.añadir_usuario("user@gmail.com", "1234"))
print(usu.login("user@gmail.com", "1234"))

