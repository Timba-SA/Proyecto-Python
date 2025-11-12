# Problema: Promedio de Elementos de una Lista

## 🎯 Objetivo

Implementar un programa que reciba una lista de números y calcule el promedio (media aritmética) de todos sus elementos.

## 📥 Entrada

El programa recibirá **UNA línea** con:
- Números (enteros o decimales) separados por espacios
- Ejemplo: `10 20 30 40`

**IMPORTANTE**: Debes leer la entrada con `input()`, usar `.split()` para separar, y convertir cada número con `float()`.

## 📤 Salida Esperada

El programa debe imprimir **UN número decimal**:
- El promedio de todos los elementos de la lista
- Formato: número con hasta 2 decimales

**IMPORTANTE**:
- ✅ Imprime el promedio redondeado a 2 decimales
- ✅ Usa `round(promedio, 2)` para redondear
- ❌ NO imprimas: "El promedio es: 25.0" o mensajes adicionales

## 📋 Ejemplos de Ejecución

**Ejemplo 1:**
```
Entrada: 10 20 30 40
Salida: 25.0
```
Explicación: (10 + 20 + 30 + 40) / 4 = 100 / 4 = 25.0

**Ejemplo 2:**
```
Entrada: 5 5 5 5 5
Salida: 5.0
```
Explicación: (5 + 5 + 5 + 5 + 5) / 5 = 25 / 5 = 5.0

**Ejemplo 3:**
```
Entrada: 7 8 9
Salida: 8.0
```
Explicación: (7 + 8 + 9) / 3 = 24 / 3 = 8.0

**Ejemplo 4:**
```
Entrada: 10 15 20
Salida: 15.0
```
Explicación: (10 + 15 + 20) / 3 = 45 / 3 = 15.0

## ⚙️ Restricciones Técnicas

Tu código DEBE cumplir obligatoriamente con:

1. **Estructura del programa**:
   - ✅ Crear una función llamada exactamente `main()` (sin parámetros)
   - ✅ Toda la lógica debe estar dentro de `main()`
   - ✅ Al final del archivo, incluir: `if __name__ == "__main__": main()`

2. **Lectura de datos**:
   - ✅ Usar `input()` para leer la línea
   - ✅ Usar `.split()` para separar los números
   - ✅ Convertir cada elemento a float con `float()`
   - ❌ NO solicitar datos con mensajes

3. **Procesamiento**:
   - ✅ Calcular la suma de todos los elementos
   - ✅ Dividir entre la cantidad de elementos: `len(lista)`
   - ✅ Redondear a 2 decimales con `round()`

4. **Salida de datos**:
   - ✅ Usar `print()` para mostrar el resultado
   - ✅ Formato: número redondeado a 2 decimales

## 💡 Pistas de Implementación

1. La estructura básica es:
   ```python
   def main():
       numeros = list(map(float, input().split()))
       promedio = sum(numeros) / len(numeros)
       print(round(promedio, 2))
   ```

2. El promedio se calcula: suma_total / cantidad_elementos

3. La función `round(numero, decimales)` redondea a la cantidad de decimales especificada

## ⚠️ Errores Comunes a Evitar

❌ **Error 1**: No convertir a números
```python
numeros = input().split()  # ¡MAL! quedan como texto
```

❌ **Error 2**: Olvidar redondear
```python
print(promedio)  # Puede mostrar muchos decimales
```

❌ **Error 3**: Formato de salida incorrecto
```python
print(f"Promedio: {promedio}")  # ¡MAL! texto adicional
```

✅ **Código correcto**:
```python
def main():
    numeros = list(map(float, input().split()))
    promedio = sum(numeros) / len(numeros)
    print(round(promedio, 2))

if __name__ == "__main__":
    main()
```
