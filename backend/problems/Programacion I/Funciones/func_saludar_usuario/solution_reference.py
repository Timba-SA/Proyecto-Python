def saludar_usuario(nombre):
    """Devuelve un saludo personalizado"""
    return f"Hola {nombre}!"

if __name__ == "__main__":
    saludo = saludar_usuario("Marcos")
    print(saludo)
