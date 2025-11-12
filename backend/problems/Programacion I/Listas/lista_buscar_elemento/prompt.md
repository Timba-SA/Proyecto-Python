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
