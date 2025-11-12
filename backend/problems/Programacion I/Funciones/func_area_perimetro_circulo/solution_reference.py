import math

def calcular_area_circulo(radio):
    """Calcula el área de un círculo"""
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """Calcula el perímetro de un círculo"""
    return 2 * math.pi * radio

if __name__ == "__main__":
    r = 5
    print(f"Área: {calcular_area_circulo(r):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(r):.2f}")
