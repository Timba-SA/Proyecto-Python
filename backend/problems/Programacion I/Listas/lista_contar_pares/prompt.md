# Problema: Contar Números Pares

## 🎯 Objetivo
Contar cuántos números pares hay en una lista.

## 📥 Entrada
Números enteros separados por espacios. Ejemplo: `1 2 3 4 5 6`

## 📤 Salida
La cantidad de números pares.

## 📋 Ejemplos
```
Entrada: 1 2 3 4 5 6
Salida: 3
```



**Nota**: Estos son algunos ejemplos. Tu solución será probada con casos adicionales, incluyendo casos borde y situaciones especiales.
## 💡 Solución
```python
def main():
    numeros = list(map(int, input().split()))
    contador = sum(1 for n in numeros if n % 2 == 0)
    print(contador)

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
