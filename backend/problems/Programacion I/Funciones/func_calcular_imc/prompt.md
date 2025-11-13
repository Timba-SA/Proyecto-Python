# Problema: Calcular IMC (Índice de Masa Corporal)

## 🎯 Objetivo
Crear una función que calcule el IMC de una persona.

## 📥 Entrada
La función recibe:
- `peso` (número en kg)
- `altura` (número en metros)

## 📤 Salida
Devuelve el IMC redondeado a 2 decimales

## 📋 Fórmula
IMC = peso / (altura²)

## 💡 Ejemplo
```python
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

if __name__ == "__main__":
    print(calcular_imc(70, 1.75))  # 22.86
```


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
