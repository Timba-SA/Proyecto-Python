````markdown
# Problema: Promedio de notas por alumno

## 🎯 Objetivo
Ingresar nombres y notas de 3 alumnos, y mostrar el promedio de cada uno.

## 📥 Entrada
- 3 nombres de alumnos
- Para cada alumno: 3 notas (enteros)

**Ejemplo:**
```
Sofía
10
9
8
Luis
6
7
7
Ana
9
8
10
```

## 📤 Salida Esperada
```
Sofía: 9.0
Luis: 6.666666666666667
Ana: 9.0
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
- Guarda las notas como tupla: `(nota1, nota2, nota3)`
- Usa `sum(tupla) / len(tupla)` para calcular el promedio

````
