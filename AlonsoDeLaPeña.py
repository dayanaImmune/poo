# tres clase: Guardar -- añadir un usuario y editar un usuario
# Usuario -- debe registrarse y hacer login
# Login -- metodo(email y contraseña) --> Que el email sea user@gmail.com. pass: 1234

class Guardar:
    def añadir(self):
        print("Usuario añadido con éxito")
    def editar(self):
        print("Usuario modificado con éxito")


class Login:
    def login(self):
        if(self.email=="user@gmail.com" and self.contraseña=="1234"):
            print("Iniciado sesion con éxito")
        else:
            print("Contraseña o correo incorrecto")

class Usuario(Login,Guardar):
    def __init__(self,email,contraseña):
        self.email=email
        self.contraseña=contraseña

usuario1=Usuario("usuario@gmail.com","usuario")
usuario2=Usuario("user@gmail.com","1234")

usuario1.añadir()
usuario2.editar()
usuario1.login()
usuario2.login()

