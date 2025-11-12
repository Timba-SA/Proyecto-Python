# Problema: Tabla de Multiplicar

## 🎯 Objetivo
Crear una función que imprima la tabla de multiplicar de un número.

## 📥 Entrada
La función recibe: `numero` (número entero)

## 📤 Salida
Imprime la tabla del 1 al 10 con formato: `numero x i = resultado`

## 💡 Ejemplo
```python
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

if __name__ == "__main__":
    tabla_multiplicar(5)
```

**Salida:**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```
