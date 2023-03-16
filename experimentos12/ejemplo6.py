class Producto:
    
    def __init__(self):
        self.productos = {}

    def insertarProducto(self, sku: str, nombre: str, unidad: str) -> None:
        self.productos[sku] = {"nombre": nombre, "unidad": unidad}

    def borrarProducto(self, sku: str) -> bool:
        if sku in self.productos:
            del self.productos[sku]
            print(f"El producto con SKU {sku} ha sido borrado.")
            return True
        else:
            print(f"No se encontró ningún producto con SKU {sku}.")
            return False

producto = Producto()

# Insertar un producto
sku = input("SKU: ")
nombre = input("Nombre: ")
unidad = input("Unidad: ")
producto.insertarProducto(sku, nombre, unidad)

sku = input("SKU del producto que desea borrar: ")
borrado = producto.borrarProducto(sku)