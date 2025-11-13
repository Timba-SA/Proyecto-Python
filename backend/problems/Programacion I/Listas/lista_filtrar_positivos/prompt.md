# Problema: Filtrar Números Positivos

## 🎯 Objetivo
Filtrar solo los números positivos de una lista (mayores a 0).

## 📥 Entrada
Números separados por espacios. Ejemplo: `-5 3 -1 8 0 2`

## 📤 Salida
Solo los números positivos, separados por espacios.

## 📋 Ejemplos
```
Entrada: -5 3 -1 8 0 2
Salida: 3 8 2
```

```
Entrada: -1 -2 -3
Salida: 
```
(Si no hay positivos, imprime línea vacía)



**Nota**: Estos son algunos ejemplos. Tu solución será probada con casos adicionales, incluyendo casos borde y situaciones especiales.
## 💡 Solución
```python
def main():
    numeros = list(map(int, input().split()))
    positivos = [n for n in numeros if n > 0]
    if positivos:
        print(' '.join(map(str, positivos)))
    else:
        print()

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
