# Problema: Área y Perímetro del Círculo

## 🎯 Objetivo
Crear dos funciones para calcular el área y perímetro de un círculo.

## 📥 Entrada
Ambas funciones reciben: `radio` (número)

## 📤 Salida
- `calcular_area_circulo(radio)` devuelve el área
- `calcular_perimetro_circulo(radio)` devuelve el perímetro

## 📋 Fórmulas
- Área = π × radio²
- Perímetro = 2 × π × radio

## 💡 Solución
```python
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

if __name__ == "__main__":
    r = 5
    print(f"Área: {calcular_area_circulo(r):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(r):.2f}")
```
