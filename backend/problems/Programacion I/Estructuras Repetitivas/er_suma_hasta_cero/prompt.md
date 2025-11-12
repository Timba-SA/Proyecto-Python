````markdown
# Problema: Suma secuencial hasta cero

## 🎯 Objetivo
Permitir al usuario ingresar números enteros y sumarlos en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

## 📥 Entrada
Números enteros (uno por línea) hasta que se ingrese 0

**Ejemplo de entrada:**
```
5
10
3
0
```

## 📤 Salida Esperada
```
18
```

## 💡 Pistas de Implementación

**Pista 1 - Ciclo infinito con break**:
```python
suma = 0
while True:
    numero = int(input())
    if numero == 0:
        break
    suma += numero
print(suma)
```

**Pista 2 - Alternativa con condición en el while**:
```python
suma = 0
numero = int(input())
while numero != 0:
    suma += numero
    numero = int(input())
print(suma)
```

## ⚠️ Conceptos Importantes
- **while True** crea un ciclo infinito
- **break** sale del ciclo inmediatamente
- El 0 no se suma, solo detiene el ciclo

## 📋 Ejemplos Adicionales
- Entrada: `0` → Salida: `0` (sin números que sumar)
- Entrada: `100`, `200`, `0` → Salida: `300`

````
