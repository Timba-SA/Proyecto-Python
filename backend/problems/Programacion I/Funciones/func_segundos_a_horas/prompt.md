# Problema: Convertir Segundos a Horas

## 🎯 Objetivo
Crear una función que convierta segundos a horas.

## 📥 Entrada
La función recibe: `segundos` (número entero)

## 📤 Salida
Devuelve las horas (puede ser decimal)

## 📋 Fórmula
horas = segundos / 3600

## 💡 Ejemplo
```python
def segundos_a_horas(segundos):
    return segundos / 3600

if __name__ == "__main__":
    print(segundos_a_horas(7200))  # 2.0
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
