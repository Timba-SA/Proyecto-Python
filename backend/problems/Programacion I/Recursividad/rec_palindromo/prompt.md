# Problema: Verificar palíndromo recursivamente

## 🎯 Objetivo
Implementar una función recursiva que reciba una cadena de texto sin espacios ni tildes y devuelva True si es un palíndromo o False si no lo es.

## 📥 Entrada
El programa recibirá **exactamente un valor** desde la entrada estándar:
- **Tipo de dato**: Cadena de texto (string)
- **Características**: Sin espacios, sin tildes, puede tener mayúsculas y minúsculas
- **Cómo leerlo**: Usar `input().lower()` para convertir a minúsculas
- **Ejemplos de valores válidos**: `"neuquen"`, `"Reconocer"`, `"hola"`, `"oso"`

```python
palabra = input().lower()  # Lee y convierte a minúsculas
```

**Concepto clave - Palíndromo**: Un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda.
- Ejemplos de palíndromos: "oso", "reconocer", "neuquen", "anilina"
- Ejemplos NO palíndromos: "hola", "python", "casa"

**Definición recursiva**:
- es_palindromo("") = True (cadena vacía es palíndromo)
- es_palindromo("x") = True (un solo carácter es palíndromo)
- es_palindromo(palabra):
  - Si palabra[0] != palabra[-1]: retorna False
  - Si no: retorna es_palindromo(palabra[1:-1])

## 📤 Salida Esperada
El programa debe imprimir **una línea** indicando si la palabra es o no un palíndromo.

**Si es palíndromo**:
```
La palabra X es un palindromo
```

**Si NO es palíndromo**:
```
La palabra X no es un palindromo
```

Donde X es la palabra ingresada (en minúsculas).

## 📋 Ejemplos de Ejecución

**Ejemplo 1**
```
Entrada: neuquen
Salida: La palabra neuquen es un palindromo
```

**Ejemplo 2**
```
Entrada: Reconocer
Salida: La palabra reconocer es un palindromo
```
**Nota**: Se convierte a minúsculas automáticamente.

**Ejemplo 3**
```
Entrada: hola
Salida: La palabra hola no es un palindromo
```

**Ejemplo 4**
```
Entrada: oso
Salida: La palabra oso es un palindromo
```

**Ejemplo 5**
```
Entrada: anilina
Salida: La palabra anilina es un palindromo
```

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. Debe existir una función llamada `es_palindromo(palabra)` que sea **recursiva**
2. La función principal DEBE llamarse exactamente `main`
3. La función `main` NO debe recibir parámetros
4. Debe incluir `if __name__ == "__main__": main()` al final

### ✅ Implementación recursiva:
1. La función `es_palindromo` DEBE usar recursividad
2. NO se puede usar `[::-1]` ni `reversed()`
3. NO se permite usar bucles dentro de `es_palindromo`
4. Debe devolver True o False (tipo bool)

### ✅ Salida de datos:
1. Convertir la entrada a minúsculas con `.lower()`
2. Usar el formato exacto especificado
3. Sin tildes en "palindromo"

## 💡 Pistas de Implementación

**Pista 1 - Estructura de la función recursiva**:
```python
def es_palindromo(palabra):
    # Caso base: cadena vacía o de 1 carácter
    if len(palabra) <= 1:
        return True
    
    # Si primer y último carácter son diferentes
    if palabra[0] != palabra[-1]:
        return False
    
    # Caso recursivo: verificar el resto de la palabra
    return es_palindromo(palabra[1:-1])
```

**Pista 2 - Uso en main**:
```python
def main():
    palabra = input().lower()
    
    if es_palindromo(palabra):
        print(f"La palabra {palabra} es un palindromo")
    else:
        print(f"La palabra {palabra} no es un palindromo")
```

**Pista 3 - Razonamiento recursivo**:
Para verificar "neuquen":
- es_palindromo("neuquen"): 'n' == 'n' ✓ → es_palindromo("euque")
- es_palindromo("euque"): 'e' == 'e' ✓ → es_palindromo("uqu")
- es_palindromo("uqu"): 'u' == 'u' ✓ → es_palindromo("q")
- es_palindromo("q"): longitud 1 → True

## ⚠️ Errores Comunes a Evitar

**Error 1: Usar [::-1] para invertir**
```python
# ❌ INCORRECTO - No permitido
def es_palindromo(palabra):
    return palabra == palabra[::-1]
```

**Error 2: No convertir a minúsculas**
```python
# ❌ INCORRECTO - "Oso" != "osO"
palabra = input()  # Debe ser input().lower()
```

**Error 3: Olvidar el caso base**
```python
# ❌ INCORRECTO - Recursión infinita
def es_palindromo(palabra):
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])  # No maneja len <= 1
```

**Error 4: Formato de salida incorrecto**
```python
# ❌ INCORRECTO - Formato diferente
print(f"{palabra} es palíndromo")  # Falta "La palabra" y "un"
print(f"Es un palindromo")  # Falta la palabra
```
