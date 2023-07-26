# Creamos la clase principal. #

class Clientes:
    
    def __init__(self, nombre, apellido, dni, telefono, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.mail = mail
        self.compras = []

    # Le damos la Bienvenida a nuestro cliente. #

    def saludar(self):
        print()
        print(f"¡Bienvenido {self.apellido}, {self.nombre} a nuestra pagina de compras!")

    # Asignamos una lista de compras. #

    def comprasRealizadas(self, compra):
        self.compras.append(compra)

    # Redefinimos el objeto a la hora de imprimir. #

    def __str__(self):
        print()
        return f"Datos del cliente:\nApellido: {self.apellido}\nNombre: {self.nombre}\nDNI: {self.dni}\nTelefono: {self.telefono}\nCorreo: {self.mail}"