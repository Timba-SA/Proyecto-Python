def celsius_a_fahrenheit(celsius):
    """Convierte temperatura de Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    print(celsius_a_fahrenheit(0))    # 32.0
    print(celsius_a_fahrenheit(100))  # 212.0
    print(celsius_a_fahrenheit(25))   # 77.0
