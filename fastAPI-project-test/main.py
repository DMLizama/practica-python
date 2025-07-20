from producto import Producto

ARCHIVO = "productos.txt"

def cargar_productos():
    try:
        with open(ARCHIVO, "r") as f:
            return [Producto.from_line(linea) for linea in f]
    except FileNotFoundError:
        return []

def guardar_productos(productos):
    with open(ARCHIVO, "w") as f:
        for p in productos:
            f.write(p.to_line() + "\n")

def mostrar_productos(productos):
    if not productos:
        print("No hay productos.")
        return
    for p in productos:
        print(p)

def agregar_producto(productos):
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    productos.append(Producto(codigo, nombre, precio))
    print("Producto agregado.")

def eliminar_producto(productos):
    codigo = input("Código del producto a eliminar: ")
    productos[:] = [p for p in productos if p.codigo != codigo]
    print("Producto eliminado si existía.")

def modificar_producto(productos):
    codigo = input("Código del producto a modificar: ")
    for p in productos:
        if p.codigo == codigo:
            nuevo_nombre = input(f"Nuevo nombre ({p.nombre}): ") or p.nombre
            nuevo_precio = input(f"Nuevo precio ({p.precio}): ")
            p.nombre = nuevo_nombre
            if nuevo_precio:
                p.precio = float(nuevo_precio)
            print("Producto modificado.")
            return
        print("Producto no encontrado.")

def menu():
    productos = cargar_productos()

    while(True):
        print("\n--- Gestor de Productos ---")
        print("1. Listar productos.")
        print("2. Agregar producto.")
        print("3. Eliminar producto.")
        print("4. Modificar producto.")
        print("5. Guardar y salir.")
        
        opcion = input("Elegí una opcion: ")

        match opcion:
            case "1":
                mostrar_productos(productos)
            case "2":
                agregar_producto(productos)
            case "3":
                eliminar_producto(productos)
            case "4":
                modificar_producto(productos)
            case "5":
                guardar_productos(productos)
                print("¡Guardado! Hasta luego.")
                break
            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    menu()