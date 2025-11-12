# Problema: Convertir Celsius a Fahrenheit

## 🎯 Objetivo
Crear una función que convierta temperatura de Celsius a Fahrenheit.

## 📥 Entrada
La función recibe: `celsius` (número)

## 📤 Salida
Devuelve la temperatura en Fahrenheit

## 📋 Fórmula
Fahrenheit = (Celsius × 9/5) + 32

## 💡 Ejemplo
```python
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    print(celsius_a_fahrenheit(0))    # 32.0
    print(celsius_a_fahrenheit(100))  # 212.0
```
