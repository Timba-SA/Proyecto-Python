````markdown
# Problema: Agenda telefónica

## 🎯 Objetivo
Crear un programa que permita almacenar 5 contactos telefónicos y luego consultar el número de un contacto específico.

## 📥 Entrada
El programa debe leer:
1. **5 pares de datos** (nombre y teléfono):
   - Nombre del contacto (string)
   - Número de teléfono (string)
2. **1 nombre** para consultar

**Ejemplo de entrada:**
```
Juan
123456
Ana
987654
Pedro
555111
Maria
444222
Luis
333999
Juan
```

## 📤 Salida Esperada
- Si el contacto existe: mostrar `El número de [nombre] es: [teléfono]`
- Si no existe: mostrar `Contacto no encontrado`

**Ejemplo de salida para el ejemplo anterior:**
```
El número de Juan es: 123456
```

## 💡 Pistas de Implementación

**Pista 1 - Estructura básica**:
```python
def main():
    contactos = {}
    
    # Cargar 5 contactos
    for i in range(5):
        nombre = input()
        telefono = input()
        contactos[nombre] = telefono
    
    # Consultar un contacto
    nombre_buscar = input()
    if nombre_buscar in contactos:
        print(f"El número de {nombre_buscar} es: {contactos[nombre_buscar]}")
    else:
        print("Contacto no encontrado")
```

## ⚠️ Errores Comunes

**Error 1: No usar bucle para cargar contactos**
```python
# ❌ INCORRECTO - Pedir uno por uno manualmente
nombre1 = input()
telefono1 = input()
# ...
```

**Error 2: Formato de salida incorrecto**
```python
# ❌ INCORRECTO
print(contactos[nombre_buscar])

# ✅ CORRECTO
print(f"El número de {nombre_buscar} es: {contactos[nombre_buscar]}")
```

````
