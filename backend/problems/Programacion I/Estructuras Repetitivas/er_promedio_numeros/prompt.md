````markdown
# Problema: Promedio de números

## 🎯 Objetivo
Permitir al usuario ingresar 100 números enteros y luego calcular la media (promedio) de esos valores.

## 📥 Entrada
100 números enteros (uno por línea)

**Ejemplo de entrada (5 números para prueba):**
```
10
20
30
40
50
```

## 📤 Salida Esperada
```
30.0
```

**Explicación:** (10+20+30+40+50) / 5 = 150 / 5 = 30.0

## 💡 Pistas de Implementación

**Pista 1 - Acumular y dividir**:
```python
suma = 0

for i in range(100):
    numero = int(input())
    suma += numero

promedio = suma / 100
print(promedio)
```

**Pista 2 - División entera vs decimal**:
- `suma / 100` → resultado decimal (float)
- `suma // 100` → resultado entero
- Para promedio usa `/` para tener decimales

## ⚠️ Conceptos Importantes
- **Promedio** = suma de todos los valores / cantidad de valores
- Un **acumulador** suma todos los números
- El resultado puede ser decimal

## 📋 Nota
Para probar usa menos números cambiando `range(100)` y el divisor, pero debe funcionar con 100.

````
