# Problema: Mayor Elemento de una Lista

## 🎯 Objetivo

Implementar un programa que reciba una lista de números enteros y encuentre el mayor elemento.

## 📥 Entrada

El programa recibirá **UNA línea** con:
- Números enteros separados por espacios
- Ejemplo: `5 2 9 1 7`

## 📤 Salida Esperada

El programa debe imprimir **UN número entero**:
- El mayor elemento de la lista

## 📋 Ejemplos de Ejecución

**Ejemplo 1:**
```
Entrada: 5 2 9 1 7
Salida: 9
```

**Ejemplo 2:**
```
Entrada: -5 -2 -9 -1
Salida: -1
```

**Ejemplo 3:**
```
Entrada: 100
Salida: 100
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

```python
def main():
    numeros = list(map(int, input().split()))
    mayor = max(numeros)
    print(mayor)

if __name__ == "__main__":
    main()
```
