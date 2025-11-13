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


## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. La función DEBE llamarse exactamente `main`
2. La función NO debe recibir parámetros
3. Debe incluir `if __name__ == "__main__": main()` al final (ya provisto)

### ✅ Lectura de datos:
1. Usar `input()` para leer la entrada
2. Convertir al tipo de dato apropiado: `int()`, `float()`, `str()`
3. NO imprimir prompts (mensajes que pidan datos)

### ✅ Salida de datos:
1. Usar `print()` con el formato exacto especificado
2. Sin espacios extras, sin caracteres adicionales
3. Respetar mayúsculas y minúsculas exactamente como se indica
