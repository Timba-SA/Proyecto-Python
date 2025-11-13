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


## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. La función DEBE llamarse exactamente `main`
2. La función NO debe recibir parámetros
3. Debe incluir `if __name__ == "__main__": main()` al final (ya provisto)

### ✅ Lectura de datos:
1. Usar `input()` para leer la entrada
2. Convertir al tipo de dato apropiado: `int()`, `float()`, `str()`
3. NO imprimir prompts (mensajes que pidan datos)

### ✅ Salida de datos:
1. Usar `print()` con el formato exacto especificado
2. Sin espacios extras, sin caracteres adicionales
3. Respetar mayúsculas y minúsculas exactamente como se indica

## 💡 Pistas
- **Intersección** (`&`): elementos en ambos conjuntos
- **Diferencia simétrica** (`^`): elementos en uno u otro, pero no en ambos
- **Unión** (`|`): todos los elementos de ambos conjuntos

````
