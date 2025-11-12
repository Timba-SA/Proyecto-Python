# Problema: Serie de Fibonacci recursiva

## 🎯 Objetivo
Crear una función recursiva que calcule el valor de la serie de Fibonacci en una posición indicada y luego mostrar la serie completa hasta la posición que el usuario especifique.

## 📥 Entrada
El programa recibirá **exactamente un valor** desde la entrada estándar:
- **Tipo de dato**: Número entero no negativo (n ≥ 0)
- **Cómo leerlo**: Usar `input()` y convertir con `int()`
- **Ejemplos de valores válidos**: `5`, `10`, `0`, `7`

```python
n = int(input())  # Lee y convierte a entero
```

**Concepto clave - Serie de Fibonacci**: La serie de Fibonacci es una secuencia donde cada número es la suma de los dos anteriores.
- fibonacci(0) = 0
- fibonacci(1) = 1
- fibonacci(2) = 0 + 1 = 1
- fibonacci(3) = 1 + 1 = 2
- fibonacci(4) = 1 + 2 = 3
- fibonacci(5) = 2 + 3 = 5
- fibonacci(6) = 3 + 5 = 8

**Definición recursiva**:
- fibonacci(0) = 0 (caso base)
- fibonacci(1) = 1 (caso base)
- fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) (caso recursivo)

## 📤 Salida Esperada
El programa debe imprimir **una línea** con los valores de Fibonacci desde la posición 0 hasta n, separados por comas y espacio.

Formato:
```
0, 1, 1, 2, 3, 5, ...
```

**IMPORTANTE**: Los números deben estar separados por coma seguida de un espacio (", ").

## 📋 Ejemplos de Ejecución

**Ejemplo 1**
```
Entrada: 5
Salida: 0, 1, 1, 2, 3, 5
```
**Explicación**: Serie de Fibonacci desde posición 0 hasta 5.

**Ejemplo 2**
```
Entrada: 7
Salida: 0, 1, 1, 2, 3, 5, 8, 13
```

**Ejemplo 3**
```
Entrada: 0
Salida: 0
```
**Explicación**: Solo la posición 0, que es 0.

**Ejemplo 4**
```
Entrada: 1
Salida: 0, 1
```

**Ejemplo 5**
```
Entrada: 10
Salida: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
```

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. Debe existir una función llamada `fibonacci(n)` que sea **recursiva**
2. La función principal DEBE llamarse exactamente `main`
3. La función `main` NO debe recibir parámetros
4. Debe incluir `if __name__ == "__main__": main()` al final

### ✅ Implementación recursiva:
1. La función `fibonacci` DEBE usar recursividad (llamarse a sí misma)
2. NO se permite usar bucles dentro de `fibonacci`
3. Debe tener dos casos base: fibonacci(0) = 0 y fibonacci(1) = 1
4. El caso recursivo suma los dos valores anteriores

### ✅ Salida de datos:
1. Todos los valores en una sola línea, separados por ", " (coma y espacio)
2. Sin espacios extras al inicio o al final
3. No debe haber coma después del último número

## 💡 Pistas de Implementación

**Pista 1 - Estructura de la función recursiva**:
```python
def fibonacci(n):
    if n == 0:  # Primer caso base
        return 0
    elif n == 1:  # Segundo caso base
        return 1
    else:  # Caso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)
```

**Pista 2 - Generar la serie como lista**:
```python
def main():
    n = int(input())
    serie = []
    for i in range(n + 1):
        serie.append(fibonacci(i))
    print(", ".join(map(str, serie)))
```

**Pista 3 - Razonamiento recursivo**:
Para calcular fibonacci(5):
- fibonacci(5) = fibonacci(4) + fibonacci(3)
- fibonacci(4) = fibonacci(3) + fibonacci(2)
- fibonacci(3) = fibonacci(2) + fibonacci(1)
- fibonacci(2) = fibonacci(1) + fibonacci(0)
- fibonacci(1) = 1 (caso base)
- fibonacci(0) = 0 (caso base)

## ⚠️ Errores Comunes a Evitar

**Error 1: No definir ambos casos base**
```python
# ❌ INCORRECTO - Falta caso base para n=0
def fibonacci(n):
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**Error 2: Formato de salida incorrecto**
```python
# ❌ INCORRECTO - Separación incorrecta
print(" ".join(map(str, serie)))  # Sin comas
print(",".join(map(str, serie)))  # Sin espacio después de coma
```

**Error 3: No incluir la posición 0**
```python
# ❌ INCORRECTO - Empieza desde 1
for i in range(1, n + 1):  # Debe ser range(n + 1)
```

**Error 4: Usar iteración en lugar de recursión**
```python
# ❌ INCORRECTO - No es recursivo
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
```
