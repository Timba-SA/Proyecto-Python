````markdown
# Problema: Agregar frutas al diccionario

## 🎯 Objetivo
Dado un diccionario inicial de frutas con sus precios, agregar tres nuevas frutas con sus respectivos precios y mostrar el diccionario resultante.

## 📥 Entrada
No hay entrada del usuario. El programa trabaja con un diccionario predefinido:
```python
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
```

Debes agregar las siguientes frutas:
- Naranja = 1200
- Manzana = 1500
- Pera = 2300

## 📤 Salida Esperada
El programa debe imprimir el diccionario completo después de agregar las nuevas frutas.

**IMPORTANTE - Formato exacto**:
```
{'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
```

## 📋 Ejemplo de Ejecución

**Salida:**
```
{'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
```

## ⚙️ Restricciones Técnicas

### ✅ Estructura del programa:
1. La función DEBE llamarse exactamente `main`
2. La función NO debe recibir parámetros
3. Debe incluir `if __name__ == "__main__": main()` al final (ya provisto)

### ✅ Manipulación de diccionarios:
1. Partir del diccionario inicial dado
2. Agregar las tres frutas especificadas con sus precios
3. Imprimir el diccionario resultante usando `print()`

### ✅ Salida de datos:
1. Imprimir el diccionario completo usando `print(diccionario)`
2. El orden de las frutas originales debe mantenerse
3. Las nuevas frutas deben agregarse en el orden especificado

## 💡 Pistas de Implementación

**Pista 1 - Agregar elementos a un diccionario**:
```python
# Forma 1: Asignación directa
diccionario['nueva_clave'] = valor

# Forma 2: Método update
diccionario.update({'clave1': valor1, 'clave2': valor2})
```

**Pista 2 - Estructura básica**:
```python
def main():
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    
    # Agregar las tres frutas
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    
    print(precios_frutas)
```

## ⚠️ Errores Comunes a Evitar

**Error 1: No mantener el diccionario original**
```python
# ❌ INCORRECTO - Crear un diccionario nuevo
precios_frutas = {'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
```
```python
# ✅ CORRECTO - Agregar al diccionario existente
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
```

**Error 2: Sintaxis incorrecta para agregar**
```python
# ❌ INCORRECTO
precios_frutas.add('Naranja', 1200)  # No existe método .add()
```
```python
# ✅ CORRECTO
precios_frutas['Naranja'] = 1200
```

**Error 3: No imprimir el resultado**
```python
# ❌ INCORRECTO - Solo agregar sin mostrar
precios_frutas['Naranja'] = 1200
# ... sin print()
```
```python
# ✅ CORRECTO - Imprimir el resultado
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)
```

````
