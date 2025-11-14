````markdown
# Problema: Saludo Personalizado

## 🎯 Objetivo

Crear un programa que reciba el nombre de una persona y muestre un saludo personalizado en pantalla.

## 📖 Concepto Clave

Este ejercicio te enseña a:
- Leer datos del usuario con `input()`
- Almacenar datos en variables
- Combinar texto estático con variables usando f-strings
- Mostrar resultados personalizados con `print()`

## 📥 Entrada

El programa recibirá **UNA línea** con:
- Un nombre (texto/string)
- Ejemplos válidos: `Juan`, `María`, `Pedro`, `Ana Lucía`

**IMPORTANTE**: 
- Usa `input()` SIN mensaje para leer el nombre
- No uses `input("Ingresa tu nombre: ")` ❌
- Usa solo `input()` ✅

## 📤 Salida Esperada

El programa debe imprimir **EXACTAMENTE** la siguiente línea:
```
Hola [nombre], bienvenido!
```

Donde `[nombre]` se reemplaza con el nombre ingresado.

**IMPORTANTE**:
- ✅ "Hola" con H mayúscula
- ✅ Una coma después del nombre
- ✅ "bienvenido" en minúsculas
- ✅ Signo de exclamación al final
- ❌ NO agregues texto extra

## 📋 Ejemplos de Ejecución

**Ejemplo 1:**
```
Entrada: Juan
Salida: Hola Juan, bienvenido!
```

**Ejemplo 2:**
```
Entrada: María
Salida: Hola María, bienvenido!
```

**Ejemplo 3:**
```
Entrada: Pedro
Salida: Hola Pedro, bienvenido!
```

**Ejemplo 4:**
```
Entrada: Ana Lucía
Salida: Hola Ana Lucía, bienvenido!
```
Explicación: Nombres compuestos también funcionan.

## ⚙️ Restricciones Técnicas

Tu código DEBE cumplir obligatoriamente con:

1. **Estructura del programa**:
   - ✅ Crear una función llamada exactamente `main()` (sin parámetros)
   - ✅ Toda la lógica debe estar dentro de `main()`
   - ✅ Al final del archivo, incluir: `if __name__ == "__main__": main()`

2. **Lectura de datos**:
   - ✅ Usar `input()` para leer el nombre
   - ✅ El dato ya es un string, no necesitas convertir
   - ❌ NO uses mensajes como `input("Nombre: ")`

3. **Procesamiento**:
   - ✅ Guardar el nombre en una variable
   - ✅ Usar f-strings o concatenación para el saludo

4. **Salida de datos**:
   - ✅ Usar `print()` para mostrar el resultado
   - ✅ Formato exacto: `Hola [nombre], bienvenido!`

## 💡 Pistas de Implementación

**Pista 1 - Lectura de datos**:
```python
nombre = input()  # Lee una línea de texto
```

**Pista 2 - F-strings (formato moderno)**:
Las f-strings te permiten insertar variables en texto:
```python
mensaje = f"Hola {nombre}, bienvenido!"
print(mensaje)
```

**Pista 3 - Estructura completa**:
```python
def main():
    nombre = input()  # Leer nombre
    print(f"Hola {nombre}, bienvenido!")  # Mostrar saludo

if __name__ == "__main__":
    main()
```

**Pista 4 - Alternativa con concatenación**:
Si no quieres usar f-strings, puedes concatenar con +:
```python
print("Hola " + nombre + ", bienvenido!")
```

## ⚠️ Errores Comunes a Evitar

❌ **Error 1**: Usar mensaje en input()
```python
nombre = input("Ingresa tu nombre: ")  # ¡MAL! No debe tener mensaje
```

❌ **Error 2**: Formato de salida incorrecto
```python
print(f"Hola {nombre}!")  # ¡MAL! Falta ", bienvenido"
print(f"hola {nombre}, bienvenido!")  # ¡MAL! "hola" en minúscula
print(f"Hola {nombre}, Bienvenido!")  # ¡MAL! "Bienvenido" en mayúscula
```

❌ **Error 3**: No usar la variable
```python
nombre = input()
print("Hola Juan, bienvenido!")  # ¡MAL! Nombre fijo, no usa variable
```

❌ **Error 4**: Olvidar leer el input
```python
def main():
    print("Hola Juan, bienvenido!")  # ¡MAL! No lee nombre del usuario
```

✅ **Código correcto**:
```python
def main():
    nombre = input()
    print(f"Hola {nombre}, bienvenido!")

if __name__ == "__main__":
    main()
```

## 🎓 ¿Qué Aprendes?

- ✅ Cómo leer datos del usuario con `input()`
- ✅ Cómo almacenar datos en variables
- ✅ Cómo usar f-strings para formatear texto
- ✅ La diferencia entre texto estático y dinámico
- ✅ Cómo construir mensajes personalizados

````