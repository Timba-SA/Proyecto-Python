````markdown
# Problema: Juego de adivinanza

## 🎯 Objetivo
Crear un juego donde el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, mostrar cuántos intentos fueron necesarios.

## 📥 Entrada
Números enteros (intentos del usuario) hasta acertar

**Ejemplo de entrada:**
```
5
3
7
```

## 📤 Salida Esperada
```
3
```
(Si acertó en el tercer intento)

## 💡 Pistas de Implementación

**Pista 1 - Generar número aleatorio**:
```python
import random
numero_secreto = random.randint(0, 9)
```

**Pista 2 - Contar intentos**:
```python
intentos = 0
while True:
    intento = int(input())
    intentos += 1
    if intento == numero_secreto:
        print(intentos)
        break
```

## ⚠️ Conceptos Importantes
- **random.randint(a, b)** genera un número aleatorio entre a y b (inclusive)
- Cuenta cada intento antes de verificar si acertó
- El ciclo solo termina cuando el usuario acierta

## 📋 Nota
Para las pruebas automatizadas, se usa una semilla fija para que el número sea predecible.

````
