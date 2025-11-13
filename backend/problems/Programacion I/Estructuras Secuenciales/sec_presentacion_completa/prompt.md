# Presentación Completa

## Descripción

Desarrolla un programa en Python que solicite al usuario su nombre, apellido, edad y lugar de residencia. Luego, debe mostrar en pantalla una oración que utilice todos estos datos.

## Entrada

Cuatro líneas: nombre, apellido, edad, lugar de residencia

## Salida

Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}

## Ejemplo

**Entrada:**
```
Juan
Pérez
25
Buenos Aires
```

**Salida:**
```
Soy Juan Pérez, tengo 25 años y vivo en Buenos Aires
```

## Restricciones

- Debes usar la función `main()` que lee de stdin y escribe a stdout
- No agregues mensajes de solicitud al usar `input()`
- La salida debe ser exacta según el formato especificado


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
