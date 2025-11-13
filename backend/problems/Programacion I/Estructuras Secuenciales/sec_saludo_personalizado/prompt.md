# Saludo Personalizado

## Descripción

Escribe un programa en Python que pida al usuario su nombre y luego muestre un saludo en pantalla utilizando ese nombre.

## Entrada

El nombre del usuario

## Salida

Hola {nombre}!

## Ejemplo

**Entrada:**
```
Juan
```

**Salida:**
```
Hola Juan!
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
