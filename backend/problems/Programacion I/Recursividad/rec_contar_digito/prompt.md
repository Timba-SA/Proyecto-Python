# Problema: Contar apariciones de un dígito recursivamente

## 🎯 Objetivo
Escribir una función recursiva que reciba un número entero positivo y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

## 📥 Entrada
El programa recibirá **dos valores** desde la entrada estándar en líneas separadas:
- **Primera línea**: numero (entero positivo)
- **Segunda línea**: digito (entero entre 0 y 9)

```python
numero = int(input())
digito = int(input())
```

**Concepto clave - Contar dígitos**: Verificar cada dígito individual del número y contar cuántas veces aparece el dígito buscado.

**Ejemplos**:
- En 12233421, el dígito 2 aparece 3 veces
- En 5555, el dígito 5 aparece 4 veces
- En 123456, el dígito 7 aparece 0 veces

**Operaciones clave**:
- `numero % 10`: obtiene el último dígito
- `numero // 10`: obtiene el número sin el último dígito

**Definición recursiva**:
- contar_digito(0, digito) = 0 (caso base)
- contar_digito(numero, digito):
  - Si numero % 10 == digito: 1 + contar_digito(numero // 10, digito)
  - Si no: 0 + contar_digito(numero // 10, digito)

## 📤 Salida Esperada
El programa debe imprimir **una línea** con la cantidad de veces que aparece el dígito.

Formato:
```
El digito D aparece C veces en el numero N
```

Donde:
- D es el dígito buscado
- C es el contador (cuántas veces aparece)
- N es el número original

## 📋 Ejemplos de Ejecución

**Ejemplo 1**
```
Entrada:
12233421
2
Salida: El digito 2 aparece 3 veces en el numero 12233421
```
**Explicación**: En 12233421, el 2 aparece en posiciones: 1**2**2**33**4**2**1 → 3 veces

**Ejemplo 2**
```
Entrada:
5555
5
Salida: El digito 5 aparece 4 veces en el numero 5555
```

**Ejemplo 3**
```
Entrada:
123456
7
Salida: El digito 7 aparece 0 veces en el numero 123456
```

**Ejemplo 4**
```
Entrada:
100200
0
Salida: El digito 0 aparece 4 veces en el numero 100200
```
**Explicación**: 1**00**2**00** → 4 veces

**Ejemplo 5**
```
Entrada:
9
9
Salida: El digito 9 aparece 1 veces en el numero 9
```

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. Debe existir una función llamada `contar_digito(numero, digito)` que sea **recursiva**
2. La función principal DEBE llamarse exactamente `main`
3. La función `main` NO debe recibir parámetros
4. Debe incluir `if __name__ == "__main__": main()` al final

### ✅ Implementación recursiva:
1. La función `contar_digito` DEBE usar recursividad
2. NO se puede convertir a string
3. NO se permite usar bucles dentro de `contar_digito`
4. Solo operaciones matemáticas: `%`, `//`, comparaciones

### ✅ Salida de datos:
1. Usar el formato exacto especificado
2. Sin tildes en "digito" ni "numero"
3. Incluir el dígito, el contador y el número original

## 💡 Pistas de Implementación

**Pista 1 - Estructura de la función recursiva**:
```python
def contar_digito(numero, digito):
    if numero == 0:  # Caso base
        return 0
    else:
        # Si el último dígito coincide, suma 1; si no, suma 0
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
```

**Pista 2 - Versión más compacta**:
```python
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    # Suma 1 si coincide, 0 si no (usando comparación como int)
    return (numero % 10 == digito) + contar_digito(numero // 10, digito)
```

**Pista 3 - Razonamiento recursivo**:
Para contar_digito(12233421, 2):
- 12233421 % 10 = 1 (no es 2) → 0 + contar_digito(1223342, 2)
- 1223342 % 10 = 2 (es 2) → 1 + contar_digito(122334, 2)
- 122334 % 10 = 4 (no es 2) → 0 + contar_digito(12233, 2)
- 12233 % 10 = 3 (no es 2) → 0 + contar_digito(1223, 2)
- 1223 % 10 = 3 (no es 2) → 0 + contar_digito(122, 2)
- 122 % 10 = 2 (es 2) → 1 + contar_digito(12, 2)
- 12 % 10 = 2 (es 2) → 1 + contar_digito(1, 2)
- 1 % 10 = 1 (no es 2) → 0 + contar_digito(0, 2)
- 0 → 0 (caso base)
- Total: 0 + 1 + 0 + 0 + 0 + 1 + 1 + 0 + 0 = 3

## ⚠️ Errores Comunes a Evitar

**Error 1: Convertir a string**
```python
# ❌ INCORRECTO
def contar_digito(numero, digito):
    return str(numero).count(str(digito))
```

**Error 2: Usar bucles**
```python
# ❌ INCORRECTO - No es recursivo
def contar_digito(numero, digito):
    contador = 0
    while numero > 0:
        if numero % 10 == digito:
            contador += 1
        numero //= 10
    return contador
```

**Error 3: No manejar el caso especial cuando numero=0 y digito=0**
```python
# ⚠️ CUIDADO: Si numero=0 y digito=0, ¿debería contar 1?
# En este ejercicio, numero=0 es caso base y retorna 0
# El 0 como dígito solo se cuenta si aparece en medio del número
```

**Error 4: Formato de salida incorrecto**
```python
# ❌ INCORRECTO
print(f"Aparece {contador} veces")
print(f"El dígito {digito} aparece {contador} veces")
```
