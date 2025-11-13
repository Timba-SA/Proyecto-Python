# Problema: Buscar Elemento en una Lista

## 🎯 Objetivo
Verificar si un elemento existe en una lista.

## 📥 Entrada
Primera línea: números separados por espacios
Segunda línea: número a buscar

## 📤 Salida
`Si` si el elemento existe, `No` si no existe.

## 📋 Ejemplos
```
Entrada:
1 2 3 4 5
3
Salida: Si
```

```
Entrada:
1 2 3 4 5
10
Salida: No
```



**Nota**: Estos son algunos ejemplos. Tu solución será probada con casos adicionales, incluyendo casos borde y situaciones especiales.
## 💡 Solución
```python
def main():
    numeros = list(map(int, input().split()))
    buscar = int(input())
    if buscar in numeros:
        print("Si")
    else:
        print("No")

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
