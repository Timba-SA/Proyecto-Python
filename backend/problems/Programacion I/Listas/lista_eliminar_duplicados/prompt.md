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

## 💡 Solución
```python
def main():
    numeros = list(map(int, input().split()))
    unicos = sorted(set(numeros))
    print(' '.join(map(str, unicos)))

if __name__ == "__main__":
    main()
```
