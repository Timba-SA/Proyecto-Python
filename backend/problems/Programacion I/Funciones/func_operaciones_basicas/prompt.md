# Problema: Operaciones Básicas

## 🎯 Objetivo
Crear una función que realice las 4 operaciones básicas con dos números.

## 📥 Entrada
La función recibe: `a` y `b` (dos números)

## 📤 Salida
Devuelve una tupla con: `(suma, resta, multiplicacion, division)`

## 💡 Ejemplo
```python
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

if __name__ == "__main__":
    resultado = operaciones_basicas(10, 2)
    print(resultado)  # (12, 8, 20, 5.0)
```
