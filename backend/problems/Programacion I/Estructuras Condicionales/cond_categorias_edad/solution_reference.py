def categoria_edad(edad):
    """Clasifica persona por edad: Niño/a, Adolescente, Adulto/a joven, Adulto/a"""
    if edad < 12:
        return "Niño/a"
    elif edad < 18:
        return "Adolescente"
    elif edad < 30:
        return "Adulto/a joven"
    else:
        return "Adulto/a"

if __name__ == "__main__":
    pass
