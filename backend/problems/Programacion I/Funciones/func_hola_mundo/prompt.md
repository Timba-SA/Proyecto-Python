# Problema: Función Hola Mundo

## 🎯 Objetivo

Crear una función que imprima "Hola Mundo!" y llamarla desde el programa principal.

## 📥 Entrada

No hay entrada (no se usa `input()`).

## 📤 Salida Esperada

El programa debe imprimir:
```
Hola Mundo!
```

## 📋 Ejemplo de Ejecución

```
Salida: Hola Mundo!
```

## ⚙️ Restricciones Técnicas

1. **Definición de función**:
   - ✅ Crear una función llamada exactamente `imprimir_hola_mundo()`
   - ✅ La función no recibe parámetros
   - ✅ La función debe usar `print()` para mostrar el mensaje

2. **Programa principal**:
   - ✅ Incluir `if __name__ == "__main__":`
   - ✅ Llamar a la función `imprimir_hola_mundo()` desde main

3. **Formato de salida**:
   - ✅ El mensaje debe ser exactamente: `Hola Mundo!`
   - ✅ Con H y M mayúsculas
   - ✅ Con signo de exclamación al final

## 💡 Pistas de Implementación

1. La estructura básica es:
   ```python
   def imprimir_hola_mundo():
       # Tu código aquí
       pass
   
   if __name__ == "__main__":
       imprimir_hola_mundo()
   ```

2. Las funciones se definen con la palabra clave `def`

3. Para llamar a una función, escribe su nombre seguido de paréntesis

## ⚠️ Errores Comunes a Evitar

❌ **Error 1**: No definir la función
```python
# ¡MAL! - No hay función definida
print("Hola Mundo!")
```

❌ **Error 2**: No llamar a la función
```python
def imprimir_hola_mundo():
    print("Hola Mundo!")
# ¡MAL! - Olvidé llamar a la función
```

❌ **Error 3**: Formato incorrecto del mensaje
```python
print("hola mundo")  # ¡MAL! - Minúsculas y sin exclamación
```

✅ **Código correcto**:
```python
def imprimir_hola_mundo():
    print("Hola Mundo!")

if __name__ == "__main__":
    imprimir_hola_mundo()
```
