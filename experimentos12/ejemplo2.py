class Producto: 
    
    def borrarProducto(self, sku: str) -> bool:
        if sku in self.productos:
            del self.productos[sku]
            print(f"El producto con SKU {sku} ha sido borrado.")
            return True
        else:
            print(f"No se encontró ningún producto con SKU {sku}.")
            return False
productos = Producto()

# Insertar un producto
sku = input("SKU: ")
nombre = input("Nombre: ")
unidad = input("Unidad: ")
productos.insertarProducto(sku, nombre, unidad)
sku = input("SKU del producto que desea borrar: ")
borrado = productos.borrarProducto(sku)
