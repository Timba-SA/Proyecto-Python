# Problema: Potencia recursiva

## 🎯 Objetivo
Crear una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula n^m = n × n^(m-1).

## 📥 Entrada
El programa recibirá **dos valores** desde la entrada estándar en líneas separadas:
- **Primera línea**: base (número entero)
- **Segunda línea**: exponente (número entero no negativo, exponente ≥ 0)

```python
base = int(input())
exponente = int(input())
```

**Concepto clave - Potencia**: La potencia de un número es el resultado de multiplicar ese número por sí mismo un cierto número de veces.
- 2^0 = 1
- 2^1 = 2
- 2^2 = 2 × 2 = 4
- 2^3 = 2 × 2 × 2 = 8
- 3^4 = 3 × 3 × 3 × 3 = 81

**Definición recursiva**:
- potencia(n, 0) = 1 (caso base)
- potencia(n, m) = n × potencia(n, m-1) (caso recursivo)

## 📤 Salida Esperada
El programa debe imprimir **una línea** con el resultado de elevar la base al exponente.

Formato:
```
El resultado de BASE elevado a EXPONENTE es RESULTADO
```

## 📋 Ejemplos de Ejecución

**Ejemplo 1**
```
Entrada:
2
3
Salida: El resultado de 2 elevado a 3 es 8
```
**Explicación**: 2^3 = 2 × 2 × 2 = 8

**Ejemplo 2**
```
Entrada:
5
0
Salida: El resultado de 5 elevado a 0 es 1
```
**Explicación**: Cualquier número elevado a 0 es 1.

**Ejemplo 3**
```
Entrada:
3
4
Salida: El resultado de 3 elevado a 4 es 81
```
**Explicación**: 3^4 = 3 × 3 × 3 × 3 = 81

**Ejemplo 4**
```
Entrada:
10
2
Salida: El resultado de 10 elevado a 2 es 100
```

**Ejemplo 5**
```
Entrada:
2
10
Salida: El resultado de 2 elevado a 10 es 1024
```

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. Debe existir una función llamada `potencia(base, exponente)` que sea **recursiva**
2. La función principal DEBE llamarse exactamente `main`
3. La función `main` NO debe recibir parámetros
4. Debe incluir `if __name__ == "__main__": main()` al final

### ✅ Implementación recursiva:
1. La función `potencia` DEBE usar recursividad (llamarse a sí misma)
2. NO se permite usar el operador `**` ni `pow()`
3. NO se permite usar bucles dentro de `potencia`
4. El caso base es cuando exponente == 0, devuelve 1

### ✅ Salida de datos:
1. Usar `print()` con el formato exacto
2. Incluir la base, el exponente y el resultado en el mensaje
3. Sin espacios extras ni caracteres adicionales

## 💡 Pistas de Implementación

**Pista 1 - Estructura de la función recursiva**:
```python
def potencia(base, exponente):
    if exponente == 0:  # Caso base
        return 1
    else:  # Caso recursivo
        return base * potencia(base, exponente - 1)
```

**Pista 2 - Uso en main**:
```python
def main():
    base = int(input())
    exponente = int(input())
    resultado = potencia(base, exponente)
    print(f"El resultado de {base} elevado a {exponente} es {resultado}")
```

**Pista 3 - Razonamiento recursivo**:
Para calcular 2^3:
- potencia(2, 3) = 2 × potencia(2, 2)
- potencia(2, 2) = 2 × potencia(2, 1)
- potencia(2, 1) = 2 × potencia(2, 0)
- potencia(2, 0) = 1 (caso base)
- Entonces: 2 × (2 × (2 × 1)) = 8

## ⚠️ Errores Comunes a Evitar

**Error 1: Usar el operador de potencia**
```python
# ❌ INCORRECTO - Usa el operador **
def potencia(base, exponente):
    return base ** exponente
```

**Error 2: No definir el caso base**
```python
# ❌ INCORRECTO - Recursión infinita
def potencia(base, exponente):
    return base * potencia(base, exponente - 1)
```

**Error 3: Formato de salida incorrecto**
```python
# ❌ INCORRECTO
print(f"{base}^{exponente} = {resultado}")
print(f"Resultado: {resultado}")
```

**Error 4: Usar bucles en lugar de recursión**
```python
# ❌ INCORRECTO - No es recursivo
def potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado
```
