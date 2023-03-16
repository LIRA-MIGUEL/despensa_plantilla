class Productos:

    def __init__(self):
        self.productos = {}

    def listarProductos(self)->bool:
        print(self.productos)
        return True
        
    def insertarProductos(self, sku:str, nombre:str, unidad:str) ->bool:
        print(f"INSERTAR: SKU:{sku}, Nombre:{nombre}, Unidad:{unidad}")
        self.productos[sku] = {"nombre": nombre, "unidad": unidad}
        return True

    def borrarProducto(self, sku:str, nombre:str, unidad:str) -> bool:
        if sku in self.productos:
            del self.productos[sku]
        if nombre in self.productos:
            del self.productos[nombre]
        if unidad in self.productos:
            del self.productos[unidad]
        if sku not in self.productos and nombre not in self.productos and unidad not in self.productos 
            return False
        return True

productos = Productos()

sku = input("SKU: ")
nombre = input("Nombre: ")
unidad = input("Unidad: ")
productos.insertarProductos(sku, nombre, unidad)

productos.listarProductos()

sku = input("SKU: ")
nombre = input("Nombre: ")
unidad = input("Unidad: ")

# Llamar a la función borrarProducto de la instancia productos y guardar el resultado en una variable
borrarProducto = productos.borrarProducto(sku, nombre, unidad)

# Usar la variable borrarProducto en la comprobación if
if borrarProducto:
    print(f"BORRAR: SKU: {sku}, Nombre: {nombre}, Unidad: {unidad}")
