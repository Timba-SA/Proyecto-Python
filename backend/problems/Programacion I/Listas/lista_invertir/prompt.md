# Problema: Invertir una Lista

## 🎯 Objetivo
Invertir el orden de los elementos de una lista.

## 📥 Entrada
Números separados por espacios. Ejemplo: `1 2 3 4 5`

## 📤 Salida
Los números en orden inverso, separados por espacios.

## 📋 Ejemplos
```
Entrada: 1 2 3 4 5
Salida: 5 4 3 2 1
```

## 💡 Solución
```python
def main():
    numeros = list(map(int, input().split()))
    numeros.reverse()
    print(' '.join(map(str, numeros)))

if __name__ == "__main__":
    main()
```
