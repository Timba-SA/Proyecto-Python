def segundos_a_horas(segundos):
    """Convierte segundos a horas"""
    return segundos / 3600

if __name__ == "__main__":
    print(segundos_a_horas(7200))  # 2.0
    print(segundos_a_horas(3600))  # 1.0
    print(segundos_a_horas(1800))  # 0.5
