from packages.module_1 import *

# Creamos el objeto cliente. #

cliente1 = Clientes("Matias", "Kehler", 36881274, 1144048636, "matias.kehler@gmail.com") # Editable #

# Agregamos productos a nuestra lista. #

cliente1.comprasRealizadas("Gabinete")      # Editable #
cliente1.comprasRealizadas("Monitor")       # Editable #
cliente1.comprasRealizadas("Teclado")       # Editable #
cliente1.comprasRealizadas("Mouse")         # Editable #
cliente1.comprasRealizadas("Auriculares")   # Editable #

# Ejecutamos el programa. #

cliente1.saludar()
print(cliente1)
print()
print("Su elecciones hasta el momento: \n" + str(cliente1.compras))
print()