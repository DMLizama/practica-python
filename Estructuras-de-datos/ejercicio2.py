#2. Contar cuántas veces aparece cada Letra en una cadena
cadena = "python se la recontra banca un montón"
contador = {}

for letra in cadena:
    if letra != " ":
        contador[letra] = contador.get(letra, 0)+ 1
print(contador)