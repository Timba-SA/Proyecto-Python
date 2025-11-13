# Problema: Calcular Promedio de 3 Números

## 🎯 Objetivo
Crear una función que calcule el promedio de tres números.

## 📥 Entrada
La función recibe: `a`, `b`, `c` (tres números)

## 📤 Salida
Devuelve el promedio de los tres números

## 📋 Fórmula
promedio = (a + b + c) / 3

## 💡 Ejemplo
```python
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

if __name__ == "__main__":
    print(calcular_promedio(8, 9, 10))  # 9.0
    print(calcular_promedio(5, 7, 9))   # 7.0
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
