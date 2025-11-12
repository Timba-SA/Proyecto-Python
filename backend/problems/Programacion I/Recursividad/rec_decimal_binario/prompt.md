# Problema: Conversión decimal a binario recursiva

## 🎯 Objetivo
Crear una función recursiva que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

## 📥 Entrada
El programa recibirá **exactamente un valor** desde la entrada estándar:
- **Tipo de dato**: Número entero positivo (n > 0)
- **Cómo leerlo**: Usar `input()` y convertir con `int()`
- **Ejemplos de valores válidos**: `10`, `5`, `1`, `255`

```python
n = int(input())  # Lee y convierte a entero
```

**Concepto clave - Sistema Binario**: El sistema binario usa solo dos dígitos: 0 y 1 (base 2).

**Algoritmo de conversión**:
1. Dividir el número por 2
2. Guardar el resto (0 o 1)
3. Repetir con el cociente hasta que llegue a 0
4. Los restos leídos de abajo hacia arriba forman el número binario

**Ejemplo**: Convertir 10 a binario
```
10 ÷ 2 = 5    resto: 0
 5 ÷ 2 = 2    resto: 1
 2 ÷ 2 = 1    resto: 0
 1 ÷ 2 = 0    resto: 1
Restos de abajo hacia arriba: 1010
```

## 📤 Salida Esperada
El programa debe imprimir **una línea** con la representación binaria del número.

Formato:
```
La representación binaria de N es B
```

Donde:
- N es el número decimal ingresado
- B es su representación en binario

## 📋 Ejemplos de Ejecución

**Ejemplo 1**
```
Entrada: 10
Salida: La representación binaria de 10 es 1010
```
**Explicación**: 10 en decimal = 1010 en binario

**Ejemplo 2**
```
Entrada: 5
Salida: La representación binaria de 5 es 101
```
**Explicación**: 5 en decimal = 101 en binario

**Ejemplo 3**
```
Entrada: 1
Salida: La representación binaria de 1 es 1
```

**Ejemplo 4**
```
Entrada: 8
Salida: La representación binaria de 8 es 1000
```

**Ejemplo 5**
```
Entrada: 255
Salida: La representación binaria de 255 es 11111111
```

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. Debe existir una función llamada `decimal_a_binario(n)` que sea **recursiva**
2. La función principal DEBE llamarse exactamente `main`
3. La función `main` NO debe recibir parámetros
4. Debe incluir `if __name__ == "__main__": main()` al final

### ✅ Implementación recursiva:
1. La función `decimal_a_binario` DEBE usar recursividad
2. NO se permite usar `bin()` ni format() con 'b'
3. NO se permite usar bucles dentro de `decimal_a_binario`
4. El caso base es cuando n == 0, devuelve cadena vacía
5. Debe devolver una cadena (string) con el binario

### ✅ Operaciones permitidas:
1. División entera: `n // 2` (cociente)
2. Módulo: `n % 2` (resto)
3. Concatenación de strings

## 💡 Pistas de Implementación

**Pista 1 - Estructura de la función recursiva**:
```python
def decimal_a_binario(n):
    if n == 0:  # Caso base
        return ""
    else:  # Caso recursivo
        return decimal_a_binario(n // 2) + str(n % 2)
```

**Pista 2 - Caso especial para el número 0**:
Si el usuario ingresa 0, el resultado debería ser "0", pero la función recursiva devuelve "". Puedes manejarlo en main:
```python
if n == 0:
    binario = "0"
else:
    binario = decimal_a_binario(n)
```

**Pista 3 - Razonamiento recursivo**:
Para convertir 10 a binario:
- decimal_a_binario(10) = decimal_a_binario(5) + "0"
- decimal_a_binario(5) = decimal_a_binario(2) + "1"
- decimal_a_binario(2) = decimal_a_binario(1) + "0"
- decimal_a_binario(1) = decimal_a_binario(0) + "1"
- decimal_a_binario(0) = "" (caso base)
- Resultado: "" + "1" + "0" + "1" + "0" = "1010"

## ⚠️ Errores Comunes a Evitar

**Error 1: Usar la función bin()**
```python
# ❌ INCORRECTO - Usa función incorporada
def decimal_a_binario(n):
    return bin(n)[2:]  # No permitido
```

**Error 2: Orden incorrecto de concatenación**
```python
# ❌ INCORRECTO - Orden invertido
def decimal_a_binario(n):
    if n == 0:
        return ""
    return str(n % 2) + decimal_a_binario(n // 2)  # Genera el binario al revés
```

**Error 3: No manejar el caso n=0 en main**
```python
# ❌ INCORRECTO - No maneja 0 correctamente
binario = decimal_a_binario(n)  # Para n=0 devuelve "", debería ser "0"
```

**Error 4: Usar bucles**
```python
# ❌ INCORRECTO - No es recursivo
def decimal_a_binario(n):
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario
```
