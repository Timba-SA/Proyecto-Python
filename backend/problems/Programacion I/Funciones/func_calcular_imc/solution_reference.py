def calcular_imc(peso, altura):
    """Calcula el IMC de una persona"""
    imc = peso / (altura ** 2)
    return round(imc, 2)

if __name__ == "__main__":
    print(calcular_imc(70, 1.75))  # 22.86
    print(calcular_imc(85, 1.80))  # 26.23
