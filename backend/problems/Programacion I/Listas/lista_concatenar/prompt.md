# Problema: Concatenar Dos Listas

## 🎯 Objetivo
Unir dos listas en una sola.

## 📥 Entrada
Primera línea: primera lista de números
Segunda línea: segunda lista de números

## 📤 Salida
Las dos listas concatenadas, separadas por espacios.

## 📋 Ejemplos
```
Entrada:
1 2 3
4 5 6
Salida: 1 2 3 4 5 6
```



**Nota**: Estos son algunos ejemplos. Tu solución será probada con casos adicionales, incluyendo casos borde y situaciones especiales.
## 💡 Solución
```python
def main():
    lista1 = list(map(int, input().split()))
    lista2 = list(map(int, input().split()))
    concatenada = lista1 + lista2
    print(' '.join(map(str, concatenada)))

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
