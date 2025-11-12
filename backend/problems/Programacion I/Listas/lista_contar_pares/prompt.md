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

## 💡 Solución
```python
def main():
    numeros = list(map(int, input().split()))
    contador = sum(1 for n in numeros if n % 2 == 0)
    print(contador)

if __name__ == "__main__":
    main()
```
