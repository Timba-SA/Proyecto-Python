````markdown
# Problema: Hola Mundo

## 🎯 Objetivo

Crear tu primer programa en Python que imprima el clásico mensaje "Hola Mundo!" en pantalla.

## 📖 Concepto Clave

Este es el programa más básico en programación. Te enseña a:
- Usar la función `print()` para mostrar texto
- Entender la estructura básica de un programa Python
- Respetar el formato exacto de salida

## 📥 Entrada

**No hay entrada** - Este programa no recibe datos del usuario.

## 📤 Salida Esperada

El programa debe imprimir **EXACTAMENTE** la siguiente línea:
```
Hola Mundo!
```

**IMPORTANTE**:
- ✅ "Hola" con H mayúscula
- ✅ "Mundo" con M mayúscula  
- ✅ Signo de exclamación al final
- ✅ Un espacio entre "Hola" y "Mundo"
- ❌ NO imprimas comillas, puntos extras ni texto adicional

## 📋 Ejemplos de Ejecución

**Ejemplo 1 (único caso):**
```
Salida: Hola Mundo!
```

## ⚙️ Restricciones Técnicas

Tu código DEBE cumplir obligatoriamente con:

1. **Estructura del programa**:
   - ✅ Crear una función llamada exactamente `main()` (sin parámetros)
   - ✅ Toda la lógica debe estar dentro de `main()`
   - ✅ Al final del archivo, incluir: `if __name__ == "__main__": main()`

2. **Función print()**:
   - ✅ Usar `print()` para mostrar el mensaje
   - ✅ El texto debe ir entre comillas: `print("texto")`
   - ❌ NO uses `input()` en este ejercicio

3. **Formato de salida**:
   - ✅ Mensaje exacto: `Hola Mundo!`
   - ❌ NO agregues texto extra como "El mensaje es: Hola Mundo!"

## 💡 Pistas de Implementación

**Pista 1 - Función print()**:
La función `print()` muestra texto en pantalla. El texto va entre comillas:
```python
print("Tu mensaje aquí")
```

**Pista 2 - Estructura del programa**:
```python
def main():
    # Aquí va tu código que imprime el mensaje
    pass  # Reemplaza esto

if __name__ == "__main__":
    main()
```

**Pista 3 - Solución**:
Solo necesitas una línea de código dentro de `main()`:
```python
def main():
    print("Hola Mundo!")
```

## ⚠️ Errores Comunes a Evitar

❌ **Error 1**: Olvidar las comillas
```python
print(Hola Mundo!)  # ¡ERROR! Python pensará que son variables
```

❌ **Error 2**: Formato incorrecto
```python
print("hola mundo")  # ¡MAL! Minúsculas y sin exclamación
print("HOLA MUNDO!")  # ¡MAL! Todo mayúsculas
print("Hola Mundo.")  # ¡MAL! Punto en lugar de exclamación
```

❌ **Error 3**: Texto adicional
```python
print("El mensaje es: Hola Mundo!")  # ¡MAL! Texto extra
```

❌ **Error 4**: No definir main()
```python
print("Hola Mundo!")  # ¡MAL! Código suelto, debe estar en main()
```

✅ **Código correcto**:
```python
def main():
    print("Hola Mundo!")

if __name__ == "__main__":
    main()
```

## 🎓 ¿Qué Aprendes?

- ✅ Cómo usar la función `print()`
- ✅ La estructura básica de un programa Python
- ✅ La importancia del formato exacto
- ✅ Cómo definir y llamar funciones

````