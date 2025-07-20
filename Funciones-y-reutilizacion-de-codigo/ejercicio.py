def calcular_descuento(precio, porcentaje=10):
    return precio - (precio * porcentaje / 100)

print(calcular_descuento(1000)) # 10% por defecto

print(calcular_descuento(1000, 25)) # 25% de descuento