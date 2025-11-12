def main():
    """Clasifica intensidad de terremoto según escala de Richter"""
    magnitud = float(input())
    
    if magnitud < 3:
        print("Muy leve")
    elif magnitud < 4:
        print("Leve")
    elif magnitud < 5:
        print("Moderado")
    elif magnitud < 6:
        print("Fuerte")
    elif magnitud < 7:
        print("Muy Fuerte")
    else:
        print("Extremo")

if __name__ == "__main__":
    main()
