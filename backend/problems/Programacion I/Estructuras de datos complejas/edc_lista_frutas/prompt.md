````markdown
# Problema: Extraer nombres de frutas

## 🎯 Objetivo
Crear una lista que contenga únicamente los nombres de las frutas (sin los precios) del diccionario.

## 📥 Entrada
No hay entrada del usuario. Usar el diccionario actualizado:
```python
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
```

## 📤 Salida Esperada
```
['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera']
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
- Usa `diccionario.keys()` para obtener las claves
- Convierte a lista con `list()`

````
