# Problema: Suma de dígitos recursiva

## 🎯 Objetivo
Escribir una función recursiva que reciba un número entero positivo y devuelva la suma de todos sus dígitos, usando solo operaciones matemáticas (sin convertir a string).

## 📥 Entrada
El programa recibirá **exactamente un valor** desde la entrada estándar:
- **Tipo de dato**: Número entero positivo (n ≥ 0)
- **Cómo leerlo**: Usar `input()` y convertir con `int()`
- **Ejemplos de valores válidos**: `1234`, `9`, `305`, `0`

```python
n = int(input())  # Lee y convierte a entero
```

**Concepto clave - Suma de dígitos**: Sumar cada dígito individual de un número.
- 1234 → 1 + 2 + 3 + 4 = 10
- 9 → 9
- 305 → 3 + 0 + 5 = 8

**Operaciones clave**:
- `n % 10`: obtiene el último dígito (ej: 1234 % 10 = 4)
- `n // 10`: obtiene el número sin el último dígito (ej: 1234 // 10 = 123)

**Definición recursiva**:
- suma_digitos(0) = 0 (caso base)
- suma_digitos(n) = (n % 10) + suma_digitos(n // 10) (caso recursivo)

## 📤 Salida Esperada
El programa debe imprimir **una línea** con la suma de los dígitos.

Formato:
```
La suma de los digitos de N es S
```

Donde:
- N es el número ingresado
- S es la suma de sus dígitos

## 📋 Ejemplos de Ejecución

**Ejemplo 1**
```
Entrada: 1234
Salida: La suma de los digitos de 1234 es 10
```
**Explicación**: 1 + 2 + 3 + 4 = 10

**Ejemplo 2**
```
Entrada: 9
Salida: La suma de los digitos de 9 es 9
```

**Ejemplo 3**
```
Entrada: 305
Salida: La suma de los digitos de 305 es 8
```
**Explicación**: 3 + 0 + 5 = 8

**Ejemplo 4**
```
Entrada: 0
Salida: La suma de los digitos de 0 es 0
```

**Ejemplo 5**
```
Entrada: 9999
Salida: La suma de los digitos de 9999 es 36
```

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. Debe existir una función llamada `suma_digitos(n)` que sea **recursiva**
2. La función principal DEBE llamarse exactamente `main`
3. La función `main` NO debe recibir parámetros
4. Debe incluir `if __name__ == "__main__": main()` al final

### ✅ Implementación recursiva:
1. La función `suma_digitos` DEBE usar recursividad
2. NO se puede convertir el número a string
3. NO se permite usar bucles dentro de `suma_digitos`
4. Solo operaciones matemáticas: `%`, `//`, `+`

### ✅ Salida de datos:
1. Usar el formato exacto especificado
2. Sin tildes en "digitos"
3. Incluir el número original y la suma

## 💡 Pistas de Implementación

**Pista 1 - Estructura de la función recursiva**:
```python
def suma_digitos(n):
    if n == 0:  # Caso base
        return 0
    else:  # Caso recursivo
        return (n % 10) + suma_digitos(n // 10)
```

**Pista 2 - Uso en main**:
```python
def main():
    n = int(input())
    suma = suma_digitos(n)
    print(f"La suma de los digitos de {n} es {suma}")
```

**Pista 3 - Razonamiento recursivo**:
Para calcular suma_digitos(1234):
- suma_digitos(1234) = 4 + suma_digitos(123)
- suma_digitos(123) = 3 + suma_digitos(12)
- suma_digitos(12) = 2 + suma_digitos(1)
- suma_digitos(1) = 1 + suma_digitos(0)
- suma_digitos(0) = 0 (caso base)
- Resultado: 4 + 3 + 2 + 1 + 0 = 10

**Pista 4 - Cómo funcionan % y //**:
```python
1234 % 10  # = 4 (último dígito)
1234 // 10 # = 123 (número sin último dígito)

123 % 10   # = 3
123 // 10  # = 12

12 % 10    # = 2
12 // 10   # = 1

1 % 10     # = 1
1 // 10    # = 0
```

## ⚠️ Errores Comunes a Evitar

**Error 1: Convertir a string**
```python
# ❌ INCORRECTO - No se puede usar str()
def suma_digitos(n):
    return sum(int(d) for d in str(n))
```

**Error 2: Olvidar el caso base**
```python
# ❌ INCORRECTO - Recursión infinita
def suma_digitos(n):
    return (n % 10) + suma_digitos(n // 10)
```

**Error 3: Usar bucles**
```python
# ❌ INCORRECTO - No es recursivo
def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma
```

**Error 4: Formato de salida incorrecto**
```python
# ❌ INCORRECTO
print(f"Suma: {suma}")
print(f"La suma es {suma}")
```
