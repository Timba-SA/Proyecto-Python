# Problema: Mayor Elemento de una Lista

## 🎯 Objetivo

Implementar un programa que reciba una lista de números enteros y encuentre el mayor elemento.

## 📥 Entrada

El programa recibirá **UNA línea** con:
- Números enteros separados por espacios
- Ejemplo: `5 2 9 1 7`

## 📤 Salida Esperada

El programa debe imprimir **UN número entero**:
- El mayor elemento de la lista

## 📋 Ejemplos de Ejecución

**Ejemplo 1:**
```
Entrada: 5 2 9 1 7
Salida: 9
```

**Ejemplo 2:**
```
Entrada: -5 -2 -9 -1
Salida: -1
```

**Ejemplo 3:**
```
Entrada: 100
Salida: 100
```

## 💡 Pistas de Implementación

```python
def main():
    numeros = list(map(int, input().split()))
    mayor = max(numeros)
    print(mayor)

if __name__ == "__main__":
    main()
```
