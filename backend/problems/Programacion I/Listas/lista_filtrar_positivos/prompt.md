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
