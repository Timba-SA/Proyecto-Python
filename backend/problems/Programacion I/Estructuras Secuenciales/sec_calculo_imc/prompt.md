# Cálculo de IMC

## Descripción

Desarrolla un programa en Python que pida al usuario su altura en metros y peso en kilogramos, y calcule su Índice de Masa Corporal (IMC).

## Entrada

Dos números decimales: altura (metros) y peso (kg)

## Salida

{imc:.2f} (formato con 2 decimales)

## Ejemplo

**Entrada:**
```
1.75
70
```

**Salida:**
```
22.86
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
