# Problema: Convertir Celsius a Fahrenheit

## 🎯 Objetivo
Crear una función que convierta temperatura de Celsius a Fahrenheit.

## 📥 Entrada
La función recibe: `celsius` (número)

## 📤 Salida
Devuelve la temperatura en Fahrenheit

## 📋 Fórmula
Fahrenheit = (Celsius × 9/5) + 32

## 💡 Ejemplo
```python
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    print(celsius_a_fahrenheit(0))    # 32.0
    print(celsius_a_fahrenheit(100))  # 212.0
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
