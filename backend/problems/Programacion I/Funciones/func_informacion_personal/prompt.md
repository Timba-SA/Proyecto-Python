# Problema: Información Personal

## 🎯 Objetivo
Crear una función que reciba 4 parámetros e imprima información personal.

## 📥 Entrada
La función recibe: `nombre`, `apellido`, `edad`, `residencia`

## 📤 Salida
Debe imprimir: `"Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]"`

## 📋 Ejemplo
```python
informacion_personal("Juan", "Pérez", 25, "Buenos Aires")
# Salida: Soy Juan Pérez, tengo 25 años y vivo en Buenos Aires
```



**Nota**: Estos son algunos ejemplos. Tu solución será probada con casos adicionales, incluyendo casos borde y situaciones especiales.
## 💡 Solución
```python
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

if __name__ == "__main__":
    informacion_personal("Juan", "Pérez", 25, "Buenos Aires")
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
