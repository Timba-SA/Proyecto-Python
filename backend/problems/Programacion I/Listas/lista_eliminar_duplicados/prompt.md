# Problema: Eliminar Duplicados

## 🎯 Objetivo
Eliminar elementos duplicados de una lista y mostrar solo los únicos en orden.

## 📥 Entrada
Números separados por espacios. Ejemplo: `1 2 2 3 3 3 4`

## 📤 Salida
Los elementos únicos ordenados, separados por espacios.

## 📋 Ejemplos
```
Entrada: 1 2 2 3 3 3 4
Salida: 1 2 3 4
```



**Nota**: Estos son algunos ejemplos. Tu solución será probada con casos adicionales, incluyendo casos borde y situaciones especiales.
## 💡 Solución
```python
def main():
    numeros = list(map(int, input().split()))
    unicos = sorted(set(numeros))
    print(' '.join(map(str, unicos)))

if __name__ == "__main__":
    main()
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
