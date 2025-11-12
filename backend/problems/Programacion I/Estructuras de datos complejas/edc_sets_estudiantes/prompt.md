````markdown
# Problema: Operaciones con sets de estudiantes

## 🎯 Objetivo
Dados dos sets de números representando estudiantes que aprobaron cada parcial, realizar operaciones de conjuntos.

## 📥 Entrada
No hay entrada. Usar sets predefinidos:
```python
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}
```

## 📤 Salida Esperada
```
Aprobaron ambos: {4, 5}
Aprobaron solo uno: {1, 2, 3, 6, 7, 8}
Aprobaron al menos uno: {1, 2, 3, 4, 5, 6, 7, 8}
```

## 💡 Pistas
- **Intersección** (`&`): elementos en ambos conjuntos
- **Diferencia simétrica** (`^`): elementos en uno u otro, pero no en ambos
- **Unión** (`|`): todos los elementos de ambos conjuntos

````
