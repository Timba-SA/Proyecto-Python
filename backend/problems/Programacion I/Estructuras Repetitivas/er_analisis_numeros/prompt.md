````markdown
# Problema: Análisis de números

## 🎯 Objetivo
Permitir al usuario ingresar 100 números enteros y luego indicar cuántos son pares, impares, negativos y positivos.

## 📥 Entrada
100 números enteros (uno por línea)

**Ejemplo de entrada (10 números para prueba):**
```
5
-2
8
0
-7
3
4
-1
6
2
```

## 📤 Salida Esperada
4 líneas con:
1. Cantidad de pares
2. Cantidad de impares
3. Cantidad de negativos
4. Cantidad de positivos

**Ejemplo:**
```
6
4
3
5
```

## 💡 Pistas de Implementación

**Pista 1 - Usar 4 contadores**:
```python
pares = impares = positivos = negativos = 0

for i in range(100):
    numero = int(input())
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(pares, impares, negativos, positivos, sep='\n')
```

## ⚠️ Conceptos Importantes
- El **0** es par y no es ni positivo ni negativo
- Un número puede ser par Y positivo simultáneamente
- Usa **elif** para evitar contar dos veces

## 📋 Nota
Para probar usa menos números cambiando `range(100)` por `range(10)`, pero debe funcionar con 100.

````
