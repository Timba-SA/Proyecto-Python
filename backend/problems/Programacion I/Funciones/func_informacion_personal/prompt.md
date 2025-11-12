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

## 💡 Solución
```python
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

if __name__ == "__main__":
    informacion_personal("Juan", "Pérez", 25, "Buenos Aires")
```
