# Problema: Convertir Segundos a Horas

## 🎯 Objetivo
Crear una función que convierta segundos a horas.

## 📥 Entrada
La función recibe: `segundos` (número entero)

## 📤 Salida
Devuelve las horas (puede ser decimal)

## 📋 Fórmula
horas = segundos / 3600

## 💡 Ejemplo
```python
def segundos_a_horas(segundos):
    return segundos / 3600

if __name__ == "__main__":
    print(segundos_a_horas(7200))  # 2.0
```
