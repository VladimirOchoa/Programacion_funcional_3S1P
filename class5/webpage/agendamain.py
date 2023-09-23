from dataclasses import dataclass

@dataclass ##Anotacion, decoradores
class User:  ## Clase
    ## Propiedades
    id: str
    name: str
    age: int
    
    def show_data(self):
        return f"ID: {self.id}\nNmobre: {self.name}\nEdad: {self.age}"
        
    
if __name__=="___main__":
    usuario1 = User("1", "Hugo", 25)
    usuario2 = User("2", "Paco", 25)
    usuario3 = User("3", "Luis", 25)
    usuario4 = User("4", "Vladi", 25)
    
    usuarios = [usuario1, usuario2, usuario3, usuario4]
    
    for usuario in usuarios:
        print(usuario.show_data())