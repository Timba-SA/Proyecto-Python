# Problema: Calcular IMC (Índice de Masa Corporal)

## 🎯 Objetivo
Crear una función que calcule el IMC de una persona.

## 📥 Entrada
La función recibe:
- `peso` (número en kg)
- `altura` (número en metros)

## 📤 Salida
Devuelve el IMC redondeado a 2 decimales

## 📋 Fórmula
IMC = peso / (altura²)

## 💡 Ejemplo
```python
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

if __name__ == "__main__":
    print(calcular_imc(70, 1.75))  # 22.86
```
