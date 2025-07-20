class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"
    
p1 = Producto("Notebook", 850600)
p1.aplicar_descuento(15)
print(p1)