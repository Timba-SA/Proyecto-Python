def main():
    """Calcula el Índice de Masa Corporal (IMC)"""
    altura = float(input())
    peso = float(input())
    
    imc = peso / (altura ** 2)
    print(f"{imc:.2f}")

if __name__ == "__main__":
    main()
