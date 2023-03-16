class Productos:

    def listarProductos(self)->bool:
        return False
        
    def insertarProductos(self, sku:str, nombre:str, unidad:str) ->bool:
        print(f"INSERTAR: SKU:{sku}, Nombre:{nombre}, Unidad:{unidad}")
        return True

    def actualizarProductos(self)->bool:
        sku = input("SKU: ")
        nombre = input("Nombre: ")
        unidad = input("Unidad: ")
        print(f"ACTUALIZAR: SKU:{sku}, Nombre:{nombre}, Unidad:{unidad}")

productos = Productos()

sku = input("SKU: ")
nombre = input("Nombre: ")
unidad = input("Unidad: ")
productos.insertarProductos(sku, nombre, unidad)

productos.actualizarProductos()

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

productos = Productos()

sku = input("SKU: ")
nombre = input("Nombre: ")
unidad = input("Unidad: ")

# Llamar a la función borrarProducto de la instancia productos y guardar el resultado en una variable
borrarProducto = productos.borrarProducto(sku, nombre, unidad)

# Usar la variable borrarProducto en la comprobación if
if borrarProducto:
    print(f"BORRAR: SKU: {sku}, Nombre: {nombre}, Unidad: {unidad}")