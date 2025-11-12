# Problema: Función Saludar Usuario

## 🎯 Objetivo

Crear una función que reciba un nombre como parámetro y devuelva un saludo personalizado.

## 📥 Entrada

La función recibe un parámetro: `nombre` (string)

## 📤 Salida Esperada

La función debe **devolver** (con `return`) un string con el formato: `"Hola {nombre}!"`

Por ejemplo:
- Si se llama `saludar_usuario("Marcos")`, debe devolver: `"Hola Marcos!"`
- Si se llama `saludar_usuario("Ana")`, debe devolver: `"Hola Ana!"`

## 📋 Ejemplo de Ejecución

```python
resultado = saludar_usuario("Marcos")
print(resultado)  # Salida: Hola Marcos!
```

## ⚙️ Restricciones Técnicas

1. **Función**:
   - ✅ Nombre: `saludar_usuario(nombre)`
   - ✅ Debe recibir UN parámetro llamado `nombre`
   - ✅ Debe **devolver** (return) el saludo, NO imprimirlo

2. **Formato**:
   - ✅ El saludo debe ser: `"Hola {nombre}!"`
   - ✅ Con "Hola" con H mayúscula
   - ✅ Con signo de exclamación al final

## 💡 Solución

```python
def saludar_usuario(nombre):
    """Devuelve un saludo personalizado"""
    return f"Hola {nombre}!"

if __name__ == "__main__":
    saludo = saludar_usuario("Marcos")
    print(saludo)
```
