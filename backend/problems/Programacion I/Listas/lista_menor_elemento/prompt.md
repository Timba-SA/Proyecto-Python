# Problema: Menor Elemento de una Lista

## 🎯 Objetivo
Encontrar el menor elemento de una lista de números enteros.

## 📥 Entrada
Números enteros separados por espacios. Ejemplo: `5 2 9 1 7`

## 📤 Salida Esperada
El menor elemento de la lista.

## 📋 Ejemplos
```
Entrada: 5 2 9 1 7
Salida: 1
```

```
Entrada: -5 -2 -9 -1
Salida: -9
```

## 💡 Solución
```python
def main():
    numeros = list(map(int, input().split()))
    menor = min(numeros)
    print(menor)

if __name__ == "__main__":
    main()
```
