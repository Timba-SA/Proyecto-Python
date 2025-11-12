````markdown
# Problema: Suma entre dos valores (excluyente)

## 🎯 Objetivo
Sumar todos los números enteros comprendidos entre dos valores dados por el usuario, **excluyendo** esos dos valores.

## 📥 Entrada
Dos números enteros en líneas separadas

**Ejemplo de entrada:**
```
3
7
```

## 📤 Salida Esperada
```
15
```

**Explicación:** 4 + 5 + 6 = 15 (se excluyen el 3 y el 7)

## 💡 Pistas de Implementación

**Pista 1 - Usar range() correctamente**:
```python
num1 = int(input())
num2 = int(input())

# Asegurar orden
if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for i in range(num1 + 1, num2):  # Excluye extremos
    suma += i
print(suma)
```

**Pista 2 - Casos especiales**:
- Si los números son iguales o consecutivos, no hay números entre ellos → suma = 0

## ⚠️ Conceptos Importantes
- **range(a, b)** genera números desde a hasta b-1
- Para excluir extremos: `range(menor + 1, mayor)`
- Un **acumulador** suma valores en cada iteración

## 📋 Ejemplos Adicionales
- Entrada: `5`, `5` → Salida: `0` (no hay números entre ellos)
- Entrada: `10`, `12` → Salida: `11`
- Entrada: `1`, `5` → Salida: `9` (2+3+4)

````
