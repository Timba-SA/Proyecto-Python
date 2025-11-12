````markdown
# Problema: Contar dígitos de un número

## 🎯 Objetivo
Solicitar al usuario un número entero y determinar la cantidad de dígitos que contiene.

## 📥 Entrada
Un número entero (puede ser positivo, negativo o cero)

**Ejemplo de entrada:**
```
547
```

## 📤 Salida Esperada
```
3
```

## 💡 Pistas de Implementación

**Pista 1 - División sucesiva por 10**:
```python
numero = int(input())
contador = 0
while numero > 0:
    numero = numero // 10
    contador += 1
print(contador)
```

**Pista 2 - Usando strings (alternativa)**:
```python
numero = input()
print(len(numero))
```

## ⚠️ Conceptos Importantes
- Cada división por 10 elimina un dígito
- El número 0 tiene 1 dígito
- Para números negativos, trabaja con el valor absoluto

## 📋 Ejemplos Adicionales
- Entrada: `0` → Salida: `1`
- Entrada: `12345` → Salida: `5`
- Entrada: `-789` → Salida: `3`

````
