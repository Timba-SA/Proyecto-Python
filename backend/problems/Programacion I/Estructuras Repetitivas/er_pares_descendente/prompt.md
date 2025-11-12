````markdown
# Problema: Números pares descendentes

## 🎯 Objetivo
Imprimir todos los números pares comprendidos entre 0 y 100, en orden descendente.

## 📥 Entrada
Ninguna

## 📤 Salida Esperada
```
100
98
96
94
...
4
2
0
```

## 💡 Pistas de Implementación

**Pista 1 - Usar range() con paso negativo**:
```python
for i in range(100, -1, -2):  # Desde 100 hasta 0, de 2 en 2
    print(i)
```

**Pista 2 - Alternativa verificando paridad**:
```python
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)
```

## ⚠️ Conceptos Importantes
- **range(inicio, fin, paso)** tiene 3 parámetros
- **paso negativo** hace que el rango sea descendente
- **range(100, -1, -2)** → empieza en 100, termina en 0, decrementa de 2 en 2

## 📋 Datos
- Primer número: 100
- Último número: 0
- Total de números: 51 (desde 0 hasta 100 hay 51 pares)

````
