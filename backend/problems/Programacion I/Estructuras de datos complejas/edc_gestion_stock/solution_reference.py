def main():
    """Gestiona el stock de productos"""
    # Stock inicial
    stock = {"Manzanas": 10, "Peras": 5, "Bananas": 8}
    
    # Leer producto y cantidad
    producto = input()
    cantidad = int(input())
    
    # Agregar o actualizar stock
    if producto in stock:
        stock[producto] += cantidad
        print(f"Stock actualizado de {producto}: {stock[producto]}")
    else:
        stock[producto] = cantidad
        print(f"Producto {producto} agregado con stock: {cantidad}")

if __name__ == "__main__":
    main()
