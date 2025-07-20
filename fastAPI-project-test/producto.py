class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"[{self.codigo}],{self.nombre} - ${self.precio:.2f}"
    
    def to_line(self):
        return f"{self.codigo},{self.nombre},{self.precio}"
    
@staticmethod
def from_line(linea):
    partes = linea.strip().split(",")
    return Producto(partes[0], partes [1], float(partes[2]))