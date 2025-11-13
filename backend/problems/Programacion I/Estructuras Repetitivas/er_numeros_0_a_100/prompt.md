````markdown
# Problema: Números del 0 al 100

## 🎯 Objetivo
Crear un programa que imprima todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

## 📥 Entrada
Ninguna

## 📤 Salida Esperada
```
0
1
2
3
...
98
99
100
```


## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. La función DEBE llamarse exactamente `main`
2. La función NO debe recibir parámetros
3. Debe incluir `if __name__ == "__main__": main()` al final (ya provisto)

### ✅ Lectura de datos:
1. Usar `input()` para leer la entrada
2. Convertir al tipo de dato apropiado: `int()`, `float()`, `str()`
3. NO imprimir prompts (mensajes que pidan datos)

### ✅ Salida de datos:
1. Usar `print()` con el formato exacto especificado
2. Sin espacios extras, sin caracteres adicionales
3. Respetar mayúsculas y minúsculas exactamente como se indica

## 💡 Pistas de Implementación

**Pista 1 - Usar range()**:
```python
for i in range(0, 101):  # Del 0 al 100 inclusive
    print(i)
```

**Pista 2 - Range excluye el límite superior**:
- `range(0, 100)` genera del 0 al 99
- `range(0, 101)` genera del 0 al 100

## ⚠️ Conceptos Importantes
- El ciclo **for** itera sobre una secuencia de valores
- **range(inicio, fin)** genera números desde inicio hasta fin-1
- Para incluir el 100, usa `range(0, 101)`

````


## ⚠️ Errores Comunes a Evitar

**Error 1: Formato de salida incorrecto**
```python
# ❌ INCORRECTO - Texto adicional
print(f"El resultado es: {resultado}")
```
```python
# ✅ CORRECTO - Solo el resultado
print(resultado)
```

**Error 2: No convertir tipos de datos**
```python
# ❌ INCORRECTO - input() devuelve string
valor = input()
```
```python
# ✅ CORRECTO - Convertir al tipo apropiado
valor = int(input())  # Para enteros
```

**Error 3: Indentación incorrecta**
```python
# ❌ INCORRECTO - Mala indentación
def main():
resultado = 42
print(resultado)
```
```python
# ✅ CORRECTO - Indentación correcta
def main():
    resultado = 42
    print(resultado)
```
