import math

def main():
    """Calcula área y perímetro de un círculo"""
    radio = float(input())
    
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    
    print(area)
    print(perimetro)

if __name__ == "__main__":
    main()
