````markdown
# Problema: Invertir dígitos de un número

## 🎯 Objetivo
Invertir el orden de los dígitos de un número ingresado por el usuario.

## 📥 Entrada
Un número entero positivo

**Ejemplo de entrada:**
```
547
```

## 📤 Salida Esperada
```
745
```

## 💡 Pistas de Implementación

**Pista 1 - Extraer y construir**:
```python
numero = int(input())
invertido = 0

while numero > 0:
    digito = numero % 10        # Extrae último dígito
    invertido = invertido * 10 + digito  # Lo agrega al invertido
    numero = numero // 10       # Elimina último dígito

print(invertido)
```

**Pista 2 - Paso a paso con 547**:
1. digito = 7, invertido = 7, numero = 54
2. digito = 4, invertido = 74, numero = 5
3. digito = 5, invertido = 745, numero = 0

## ⚠️ Conceptos Importantes
- **% 10** extrae el último dígito
- **// 10** elimina el último dígito
- **invertido * 10** desplaza dígitos a la izquierda

## 📋 Ejemplos Adicionales
- Entrada: `123` → Salida: `321`
- Entrada: `1000` → Salida: `1` (los ceros a la derecha se pierden)
- Entrada: `9` → Salida: `9`

````
