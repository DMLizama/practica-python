#1. Crear una lista de productos con precios y calcular el total
productos = [
    {"nombre": "pan","precio": 1500},
    {"nombre": "leche","precio": 4800},
    {"nombre": "manteca","precio": 3500}
]

total = sum(p["precio"] for p in productos)
print("Total:", total)