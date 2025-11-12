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
