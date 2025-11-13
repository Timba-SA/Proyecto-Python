````markdown
# Problema: Agenda con tuplas como claves

## 🎯 Objetivo
Crear una agenda donde las claves son tuplas (día, hora) y los valores son eventos.

## 📥 Entrada
Agenda predefinida:
```python
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Dentista",
    ("jueves", "14:00"): "Gimnasio"
}
```

Luego leer:
- Día
- Hora

**Ejemplo:**
```
lunes
10:00
```

## 📤 Salida Esperada
- Si existe: `Actividad: Reunión`
- Si no existe: `No hay actividad programada`


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
Las tuplas pueden usarse como claves en diccionarios: `(día, hora)`

````
