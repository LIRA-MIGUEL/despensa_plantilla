class Productos:
    def __init__(self):
        self.productos = {}

    def borrarProducto(self, sku:str, nombre:str, unidad:str) -> bool:
        if sku in self.productos:
            del self.productos[sku]
        if nombre in self.productos:
            del self.productos[nombre]
        if unidad in self.productos:
            del self.productos[unidad]
        else:
            return False
        return True  # Agregar un retorno de True si se logra borrar
print("borrar producto")
productos = Productos()

sku = input("SKU: ")
nombre = input("Nombre: ")
unidad = input("Unidad: ")

# Llamar a la función borrarProducto de la instancia productos y guardar el resultado en una variable
borrarProducto = productos.borrarProducto(sku, nombre, unidad)

# Usar la variable borrarProducto en la comprobación if
if borrarProducto:
    print(f"BORRAR: SKU: {sku}, Nombre: {nombre}, Unidad: {unidad}")