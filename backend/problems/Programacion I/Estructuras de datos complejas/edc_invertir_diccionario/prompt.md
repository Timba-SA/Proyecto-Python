````markdown
# Problema: Invertir diccionario (países y capitales)

## 🎯 Objetivo
Dado un diccionario que mapea países con capitales, crear un nuevo diccionario donde las capitales sean claves y los países valores.

## 📥 Entrada
Diccionario predefinido:
```python
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}
```

## 📤 Salida Esperada
```
{'Buenos Aires': 'Argentina', 'Santiago': 'Chile', 'Brasilia': 'Brasil', 'Montevideo': 'Uruguay'}
```

## 💡 Pistas de Implementación

**Pista 1 - Invertir un diccionario**:
```python
invertido = {}
for clave, valor in original.items():
    invertido[valor] = clave
```

**Pista 2 - Comprensión de diccionario (alternativa)**:
```python
invertido = {valor: clave for clave, valor in original.items()}
```

## ⚠️ Conceptos Importantes
- Las **claves** del diccionario original se convierten en **valores** del invertido
- Los **valores** del diccionario original se convierten en **claves** del invertido

````
