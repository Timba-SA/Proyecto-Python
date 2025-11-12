import random

def main():
    """Juego de adivinanza de número aleatorio"""
    numero_secreto = random.randint(0, 9)
    intentos = 0
    
    while True:
        intento = int(input())
        intentos += 1
        
        if intento == numero_secreto:
            print(intentos)
            break

if __name__ == "__main__":
    main()
