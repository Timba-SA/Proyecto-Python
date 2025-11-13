````markdown
# Problema: Actualizar precios de frutas

## 🎯 Objetivo
Dado el diccionario de frutas resultante del ejercicio anterior, actualizar los precios de tres frutas específicas.

## 📥 Entrada
No hay entrada del usuario. El programa trabaja con el diccionario resultante del ejercicio anterior:
```python
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
```

Debes actualizar los siguientes precios:
- Banana = 1330
- Manzana = 1700
- Melón = 2800

## 📤 Salida Esperada
```
{'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
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

## 💡 Pista
Para actualizar un valor: `diccionario['clave'] = nuevo_valor`

````
