````markdown
# Problema: Palabras únicas y conteo

## 🎯 Objetivo
Analizar una frase e imprimir las palabras únicas y un conteo de apariciones.

## 📥 Entrada
Una frase (string)

**Ejemplo:**
```
hola mundo hola
```

## 📤 Salida Esperada
```
Palabras únicas: {'hola', 'mundo'}
Recuento: {'hola': 2, 'mundo': 1}
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
- Usa `.split()` para separar palabras
- Usa `set()` para palabras únicas
- Usa un diccionario para contar

````
