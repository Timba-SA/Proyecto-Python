# Problema: Mayor de edad

## 🎯 Objetivo
Crear un programa que lea una edad desde la entrada estándar y determine si la persona es mayor de edad (18 años o más) o menor de edad (17 años o menos).

## 📥 Entrada
El programa recibirá **exactamente un valor** desde la entrada estándar:
- **Tipo de dato**: Número entero
- **Cómo leerlo**: Usar `input()` y convertir con `int()`
- **Ejemplos de valores válidos**: `20`, `18`, `15`, `0`, `100`, `5`
- **Formato de lectura**: Una línea con el número

```python
edad = int(input())  # Lee y convierte a entero
```

## 📤 Salida Esperada
El programa debe imprimir **exactamente una línea** con uno de estos dos mensajes:

### ✅ Si edad >= 19:
```
Es mayor de edad
```

### ✅ Si edad <= 18:
```
Es menor de edad
```

**IMPORTANTE - Formato exacto**:
- ✅ Usar estas palabras EXACTAS (mayúsculas y minúsculas como se muestra)
- ✅ Primera letra "E" en mayúscula en ambos mensajes
- ✅ La palabra "menor" (no "No es mayor")
- ❌ NO imprimir mensajes adicionales como "Ingrese edad:", "La persona es:", etc.
- ❌ NO agregar espacios extras al inicio o final
- ❌ NO cambiar mayúsculas/minúsculas

**Nota sobre mayoría de edad en Argentina**: En Argentina, según el Código Civil y Comercial, se es mayor de edad a partir de los **18 años cumplidos**. Sin embargo, para este ejercicio académico, utilizaremos la condición `edad >= 19` para practicar el uso de operadores relacionales.

## 📋 Ejemplos de Ejecución

**Ejemplo 1 - Mayor de edad**
```
Entrada: 20
Salida: Es mayor de edad
```
**Explicación**: Como 20 >= 19, la persona es mayor de edad.

**Ejemplo 2 - Menor de edad**
```
Entrada: 15
Salida: Es menor de edad
```
**Explicación**: Como 15 < 19, la persona es menor de edad.

**Ejemplo 3 - Caso borde: Exactamente 18**
```
Entrada: 18
Salida: Es menor de edad
```
**Explicación**: Como 18 < 19, según la condición del ejercicio, la salida es "Es menor de edad". **IMPORTANTE**: La condición es `edad >= 19`, por lo tanto 18 NO cumple.

**Ejemplo 4 - Edad muy joven**
```
Entrada: 5
Salida: Es menor de edad
```
**Explicación**: Como 5 < 19, la persona es menor de edad.

**Ejemplo 5 - Caso borde: Exactamente 19**
```
Entrada: 19
Salida: Es mayor de edad
```
**Explicación**: Como 19 >= 19, la persona es mayor de edad. Es el primer valor que cumple la condición.

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. La función DEBE llamarse exactamente `main`
2. La función NO debe recibir parámetros
3. Debe incluir `if __name__ == "__main__": main()` al final (ya provisto)

### ✅ Lectura de datos:
1. Usar `input()` para leer la entrada
2. Convertir a entero con `int()`: `edad = int(input())`
3. NO imprimir prompts (mensajes que pidan datos)

### ✅ Lógica condicional:
1. Usar operador `>=` (mayor o igual que)
2. La condición es: `if edad >= 19:`
3. El caso `edad == 18` debe ir al bloque else (Es menor de edad)

### ✅ Salida de datos:
1. Usar `print()` con el mensaje exacto
2. Dos opciones posibles: `"Es mayor de edad"` o `"Es menor de edad"`
3. Sin espacios extras, sin caracteres adicionales

## 💡 Pistas de Implementación

**Pista 1 - Estructura básica**:
```python
def main():
    edad = int(input())  # Lee y convierte a entero

    if edad >= 19:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
```

**Pista 2 - Diferencia con "No es mayor"**:
Observa la diferencia entre estos dos mensajes:
- ✅ `"Es menor de edad"` (este problema)
- ❌ `"No es mayor de edad"` (otro problema)

Asegúrate de usar el mensaje correcto: **"Es menor de edad"**.

**Pista 3 - El caso 18**:
Recuerda que en este ejercicio, una persona de 18 años todavía NO es mayor de edad:
- `18 >= 19` → False → "Es menor de edad"
- `19 >= 19` → True → "Es mayor de edad"

**Nota**: Aunque legalmente en Argentina se es mayor de edad a los 18 años, este ejercicio usa 19+ como criterio para practicar operadores relacionales.

## ⚠️ Errores Comunes a Evitar

**Error 1: Usar > en lugar de >=**
```python
# ❌ INCORRECTO - Usa >
if edad > 18:
    print("Es mayor de edad")
```
```python
# ✅ CORRECTO - Usa >=
if edad >= 19:
    print("Es mayor de edad")
```
**Por qué está mal**: Una persona de 19 años debe clasificarse como "mayor de edad". La condición correcta es `edad >= 19`.

**Error 2: Mensaje incorrecto para edad < 19**
```python
# ❌ INCORRECTO - Mensaje equivocado
if edad >= 19:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")  # ¡Incorrecto!
```
```python
# ✅ CORRECTO - Mensaje exacto
if edad >= 19:
    print("Es mayor de edad")
else:
    print("Es menor de edad")  # ¡Correcto!
```
**Por qué está mal**: El mensaje debe ser exactamente "Es menor de edad", no "No es mayor de edad".

**Error 3: Mayúsculas incorrectas**
```python
# ❌ INCORRECTO - Mayúsculas incorrectas
print("es mayor de edad")
print("ES MENOR DE EDAD")
print("Es Mayor De Edad")
```
```python
# ✅ CORRECTO - Mayúsculas exactas
print("Es mayor de edad")
print("Es menor de edad")
```
**Por qué está mal**: Solo la primera letra "E" debe estar en mayúscula, el resto en minúsculas (excepto "E" en "de" que va en minúscula).

**Error 4: Imprimir mensajes adicionales**
```python
# ❌ INCORRECTO - Texto adicional
print("Por favor, ingrese su edad:")
edad = int(input())
if edad >= 19:
    print("Resultado: Es mayor de edad")
```
```python
# ✅ CORRECTO - Solo el resultado
edad = int(input())
if edad >= 19:
    print("Es mayor de edad")
```
**Por qué está mal**: No debe haber prompts ni etiquetas adicionales. El programa solo lee y responde.
