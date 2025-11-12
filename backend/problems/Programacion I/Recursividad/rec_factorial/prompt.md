# Problema: Factorial recursivo

## 🎯 Objetivo
Crear una función recursiva que calcule el factorial de un número y luego utilizarla para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

## 📥 Entrada
El programa recibirá **exactamente un valor** desde la entrada estándar:
- **Tipo de dato**: Número entero positivo (n ≥ 1)
- **Cómo leerlo**: Usar `input()` y convertir con `int()`
- **Ejemplos de valores válidos**: `5`, `10`, `1`, `7`

```python
n = int(input())  # Lee y convierte a entero
```

**Concepto clave - Factorial**: El factorial de un número n (escrito como n!) es el producto de todos los números enteros positivos desde 1 hasta n.
- 1! = 1
- 2! = 2 × 1 = 2
- 3! = 3 × 2 × 1 = 6
- 4! = 4 × 3 × 2 × 1 = 24
- 5! = 5 × 4 × 3 × 2 × 1 = 120

**Definición recursiva**:
- factorial(0) = 1 (caso base)
- factorial(1) = 1 (caso base)
- factorial(n) = n × factorial(n-1) (caso recursivo)

## 📤 Salida Esperada
El programa debe imprimir **n líneas**, cada una mostrando el factorial de los números desde 1 hasta n.

Formato de cada línea:
```
El factorial de X es Y
```

Donde:
- X es el número (1, 2, 3, ..., n)
- Y es el factorial de ese número

## 📋 Ejemplos de Ejecución

**Ejemplo 1**
```
Entrada: 5
Salida:
El factorial de 1 es 1
El factorial de 2 es 2
El factorial de 3 es 6
El factorial de 4 es 24
El factorial de 5 es 120
```

**Ejemplo 2**
```
Entrada: 3
Salida:
El factorial de 1 es 1
El factorial de 2 es 2
El factorial de 3 es 6
```

**Ejemplo 3**
```
Entrada: 1
Salida:
El factorial de 1 es 1
```

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. Debe existir una función llamada `factorial(n)` que sea **recursiva**
2. La función principal DEBE llamarse exactamente `main`
3. La función `main` NO debe recibir parámetros
4. Debe incluir `if __name__ == "__main__": main()` al final

### ✅ Implementación recursiva:
1. La función `factorial` DEBE usar recursividad (llamarse a sí misma)
2. NO se permite usar bucles dentro de `factorial`
3. Debe tener caso(s) base para evitar recursión infinita
4. El caso base es cuando n == 0 o n == 1, devuelve 1

### ✅ Salida de datos:
1. Usar `print()` con el formato exacto: `f"El factorial de {i} es {resultado}"`
2. Una línea por cada número desde 1 hasta n
3. Sin espacios extras ni caracteres adicionales

## 💡 Pistas de Implementación

**Pista 1 - Estructura de la función recursiva**:
```python
def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:  # Caso recursivo
        return n * factorial(n - 1)
```

**Pista 2 - Uso en main**:
```python
def main():
    n = int(input())
    for i in range(1, n + 1):
        resultado = factorial(i)
        print(f"El factorial de {i} es {resultado}")
```

**Pista 3 - Razonamiento recursivo**:
Para calcular factorial(5):
- factorial(5) = 5 × factorial(4)
- factorial(4) = 4 × factorial(3)
- factorial(3) = 3 × factorial(2)
- factorial(2) = 2 × factorial(1)
- factorial(1) = 1 (caso base)
- Entonces: 5 × 4 × 3 × 2 × 1 = 120

## ⚠️ Errores Comunes a Evitar

**Error 1: No definir el caso base**
```python
# ❌ INCORRECTO - Recursión infinita
def factorial(n):
    return n * factorial(n - 1)  # Nunca se detiene
```

**Error 2: Usar bucles en lugar de recursión**
```python
# ❌ INCORRECTO - No es recursivo
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
```

**Error 3: Formato de salida incorrecto**
```python
# ❌ INCORRECTO
print(f"{i}! = {resultado}")  # Formato diferente
print(f"Factorial de {i}: {resultado}")  # Formato diferente
```

**Error 4: No iterar desde 1 hasta n**
```python
# ❌ INCORRECTO - Solo muestra el factorial de n
print(f"El factorial de {n} es {factorial(n)}")
```
