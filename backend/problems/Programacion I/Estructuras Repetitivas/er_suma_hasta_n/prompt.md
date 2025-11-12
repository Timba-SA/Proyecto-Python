````markdown
# Problema: Suma de 0 hasta N

## 🎯 Objetivo
Calcular la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

## 📥 Entrada
Un número entero positivo N

**Ejemplo de entrada:**
```
5
```

## 📤 Salida Esperada
```
15
```

**Explicación:** 0 + 1 + 2 + 3 + 4 + 5 = 15

## 💡 Pistas de Implementación

**Pista 1 - Ciclo con acumulador**:
```python
n = int(input())
suma = 0
for i in range(n + 1):  # De 0 a N inclusive
    suma += i
print(suma)
```

**Pista 2 - Fórmula matemática (alternativa)**:
```python
n = int(input())
suma = n * (n + 1) // 2
print(suma)
```

## ⚠️ Conceptos Importantes
- **range(n+1)** genera números del 0 al n (inclusive)
- Un **acumulador** empieza en 0 y suma valores
- La fórmula **n(n+1)/2** da el mismo resultado

## 📋 Ejemplos Adicionales
- Entrada: `0` → Salida: `0`
- Entrada: `10` → Salida: `55` (0+1+2+...+10)
- Entrada: `100` → Salida: `5050`

````
