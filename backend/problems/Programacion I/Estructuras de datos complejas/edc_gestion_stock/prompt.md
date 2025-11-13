````markdown
# Problema: Gestión de inventario (stock)

## 🎯 Objetivo
Gestionar un inventario de productos permitiendo consultar y actualizar el stock.

## 📥 Entrada
Stock inicial:
```python
stock = {"Manzanas": 10, "Peras": 5, "Bananas": 8}
```

Luego leer:
- Nombre del producto
- Cantidad a agregar

**Ejemplo:**
```
Manzanas
5
```

## 📤 Salida Esperada
- Si existe: `Stock actualizado de Manzanas: 15`
- Si no existe: `Producto Naranjas agregado con stock: 10`


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
Usa `if producto in stock:` para verificar existencia

````
