# Problema: Contar bloques de pirámide recursivamente

## 🎯 Objetivo
Escribir una función recursiva que calcule el total de bloques necesarios para construir una pirámide donde el nivel más bajo tiene n bloques, el siguiente n-1, y así sucesivamente hasta llegar a 1 bloque en la cima.

## 📥 Entrada
El programa recibirá **exactamente un valor** desde la entrada estándar:
- **Tipo de dato**: Número entero positivo (n ≥ 1)
- **Cómo leerlo**: Usar `input()` y convertir con `int()`
- **Ejemplos de valores válidos**: `1`, `2`, `4`, `10`

```python
n = int(input())  # Lee y convierte a entero
```

**Concepto clave - Pirámide de bloques**: Una pirámide con n bloques en la base tiene:
- Nivel 1 (base): n bloques
- Nivel 2: n-1 bloques
- Nivel 3: n-2 bloques
- ...
- Último nivel: 1 bloque

Total de bloques = n + (n-1) + (n-2) + ... + 2 + 1

**Ejemplos**:
- n=1: Pirámide con 1 nivel → 1 bloque total
- n=2: Pirámide con 2 niveles → 2 + 1 = 3 bloques total
- n=4: Pirámide con 4 niveles → 4 + 3 + 2 + 1 = 10 bloques total

**Definición recursiva**:
- contar_bloques(0) = 0 (caso base)
- contar_bloques(1) = 1 (caso base alternativo)
- contar_bloques(n) = n + contar_bloques(n - 1) (caso recursivo)

## 📤 Salida Esperada
El programa debe imprimir **una línea** con el total de bloques necesarios.

Formato:
```
Para una piramide de N niveles se necesitan T bloques
```

Donde:
- N es el número de bloques en la base (número de niveles)
- T es el total de bloques necesarios

## 📋 Ejemplos de Ejecución

**Ejemplo 1**
```
Entrada: 1
Salida: Para una piramide de 1 niveles se necesitan 1 bloques
```
**Explicación**: Solo 1 nivel con 1 bloque → 1 total

**Ejemplo 2**
```
Entrada: 2
Salida: Para una piramide de 2 niveles se necesitan 3 bloques
```
**Explicación**: 2 + 1 = 3 bloques

**Ejemplo 3**
```
Entrada: 4
Salida: Para una piramide de 4 niveles se necesitan 10 bloques
```
**Explicación**: 4 + 3 + 2 + 1 = 10 bloques

**Ejemplo 4**
```
Entrada: 5
Salida: Para una piramide de 5 niveles se necesitan 15 bloques
```
**Explicación**: 5 + 4 + 3 + 2 + 1 = 15 bloques

**Ejemplo 5**
```
Entrada: 10
Salida: Para una piramide de 10 niveles se necesitan 55 bloques
```

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. Debe existir una función llamada `contar_bloques(n)` que sea **recursiva**
2. La función principal DEBE llamarse exactamente `main`
3. La función `main` NO debe recibir parámetros
4. Debe incluir `if __name__ == "__main__": main()` al final

### ✅ Implementación recursiva:
1. La función `contar_bloques` DEBE usar recursividad
2. NO se permite usar la fórmula n*(n+1)/2 directamente
3. NO se permite usar bucles dentro de `contar_bloques`
4. NO se puede usar sum() con range()

### ✅ Salida de datos:
1. Usar el formato exacto especificado
2. Sin tildes en "piramide"
3. Incluir tanto n como el total de bloques

## 💡 Pistas de Implementación

**Pista 1 - Estructura de la función recursiva**:
```python
def contar_bloques(n):
    if n == 0:  # Caso base
        return 0
    else:  # Caso recursivo
        return n + contar_bloques(n - 1)
```

**Pista 2 - Uso en main**:
```python
def main():
    n = int(input())
    total = contar_bloques(n)
    print(f"Para una piramide de {n} niveles se necesitan {total} bloques")
```

**Pista 3 - Razonamiento recursivo**:
Para calcular contar_bloques(4):
- contar_bloques(4) = 4 + contar_bloques(3)
- contar_bloques(3) = 3 + contar_bloques(2)
- contar_bloques(2) = 2 + contar_bloques(1)
- contar_bloques(1) = 1 + contar_bloques(0)
- contar_bloques(0) = 0 (caso base)
- Resultado: 4 + 3 + 2 + 1 + 0 = 10

**Pista 4 - Visualización**:
```
Pirámide con n=4:
Nivel 4:    #           (1 bloque)
Nivel 3:   # #          (2 bloques)
Nivel 2:  # # #         (3 bloques)
Nivel 1: # # # #        (4 bloques)
Total: 1 + 2 + 3 + 4 = 10 bloques
```

## ⚠️ Errores Comunes a Evitar

**Error 1: Usar la fórmula matemática directa**
```python
# ❌ INCORRECTO - No es recursivo
def contar_bloques(n):
    return n * (n + 1) // 2
```

**Error 2: Usar bucles**
```python
# ❌ INCORRECTO - No es recursivo
def contar_bloques(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```

**Error 3: Usar sum() con range()**
```python
# ❌ INCORRECTO - No es recursivo
def contar_bloques(n):
    return sum(range(1, n + 1))
```

**Error 4: Formato de salida incorrecto**
```python
# ❌ INCORRECTO
print(f"Total de bloques: {total}")
print(f"Se necesitan {total} bloques")
```
