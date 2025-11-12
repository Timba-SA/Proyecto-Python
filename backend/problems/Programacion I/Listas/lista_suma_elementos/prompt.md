# Problema: Suma de Elementos de una Lista

## 🎯 Objetivo

Implementar un programa que reciba una lista de números enteros y calcule la suma de todos sus elementos.

## 📥 Entrada

El programa recibirá **UNA línea** con:
- Números enteros separados por espacios
- Ejemplo: `1 2 3 4 5`

**IMPORTANTE**: Debes leer la entrada como texto con `input()`, luego usar `.split()` para separar los números, y convertir cada uno a entero con `int()`.

## 📤 Salida Esperada

El programa debe imprimir **UN número entero**:
- La suma total de todos los elementos de la lista

**IMPORTANTE**:
- ✅ Imprime SOLO el número resultado
- ❌ NO imprimas: "La suma es: 15" o "15." o mensajes adicionales

## 📋 Ejemplos de Ejecución

**Ejemplo 1:**
```
Entrada: 1 2 3 4 5
Salida: 15
```
Explicación: 1 + 2 + 3 + 4 + 5 = 15

**Ejemplo 2:**
```
Entrada: 10 20 30
Salida: 60
```
Explicación: 10 + 20 + 30 = 60

**Ejemplo 3:**
```
Entrada: -5 5 -3 3
Salida: 0
```
Explicación: -5 + 5 + (-3) + 3 = 0

**Ejemplo 4:**
```
Entrada: 100
Salida: 100
```
Explicación: Si hay un solo elemento, la suma es ese elemento.

## ⚙️ Restricciones Técnicas

Tu código DEBE cumplir obligatoriamente con:

1. **Estructura del programa**:
   - ✅ Crear una función llamada exactamente `main()` (sin parámetros)
   - ✅ Toda la lógica debe estar dentro de `main()`
   - ✅ Al final del archivo, incluir: `if __name__ == "__main__": main()`

2. **Lectura de datos**:
   - ✅ Usar `input()` para leer la línea de entrada
   - ✅ Usar `.split()` para separar los números
   - ✅ Convertir cada elemento a entero con `int()`
   - ❌ NO solicitar datos con mensajes

3. **Procesamiento**:
   - ✅ Usar un bucle `for` para recorrer la lista
   - ✅ Acumular la suma en una variable
   - ⚠️ Puedes usar `sum()` incorporado de Python o implementar tu propio bucle

4. **Salida de datos**:
   - ✅ Usar `print()` para mostrar el resultado
   - ✅ Formato: solo el número (sin texto adicional)

## 💡 Pistas de Implementación

1. La estructura básica es:
   ```python
   def main():
       numeros = list(map(int, input().split()))
       # Tu código para calcular la suma aquí
       print(suma)
   ```

2. Para sumar todos los elementos puedes usar:
   - Opción 1: La función `sum(lista)`
   - Opción 2: Un bucle que acumule la suma

3. Ejemplo de suma con bucle:
   ```python
   suma = 0
   for numero in numeros:
       suma += numero
   ```

## ⚠️ Errores Comunes a Evitar

❌ **Error 1**: No convertir a enteros
```python
numeros = input().split()  # ¡MAL! quedan como texto
suma = sum(numeros)  # ¡ERROR! no puedes sumar texto
```

❌ **Error 2**: Formato de salida incorrecto
```python
print(f"La suma es: {suma}")  # ¡MAL! texto adicional
```

❌ **Error 3**: No leer correctamente la entrada
```python
numero = int(input())  # ¡MAL! lee solo un número, no una lista
```

✅ **Código correcto**:
```python
def main():
    numeros = list(map(int, input().split()))
    suma = sum(numeros)
    print(suma)

if __name__ == "__main__":
    main()
```
