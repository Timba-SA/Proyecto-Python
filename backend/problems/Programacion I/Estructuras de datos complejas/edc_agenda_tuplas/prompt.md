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

## 💡 Pista
Las tuplas pueden usarse como claves en diccionarios: `(día, hora)`

````
