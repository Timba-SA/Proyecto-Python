````markdown
# Problema: Números del 0 al 100

## 🎯 Objetivo
Crear un programa que imprima todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

## 📥 Entrada
Ninguna

## 📤 Salida Esperada
```
0
1
2
3
...
98
99
100
```

## 💡 Pistas de Implementación

**Pista 1 - Usar range()**:
```python
for i in range(0, 101):  # Del 0 al 100 inclusive
    print(i)
```

**Pista 2 - Range excluye el límite superior**:
- `range(0, 100)` genera del 0 al 99
- `range(0, 101)` genera del 0 al 100

## ⚠️ Conceptos Importantes
- El ciclo **for** itera sobre una secuencia de valores
- **range(inicio, fin)** genera números desde inicio hasta fin-1
- Para incluir el 100, usa `range(0, 101)`

````
