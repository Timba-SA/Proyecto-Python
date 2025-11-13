"""
Script para generar hints.json inteligentes para todos los ejercicios
de Programación I basándose en el contenido del prompt y tests
"""

import os
import json
from pathlib import Path

def read_prompt(exercise_path):
    """Lee el contenido del prompt para entender el ejercicio"""
    prompt_file = exercise_path / 'prompt.md'
    if prompt_file.exists():
        return prompt_file.read_text(encoding='utf-8')
    return ""

def read_starter(exercise_path):
    """Lee el starter code para ver qué necesita el estudiante"""
    starter_file = exercise_path / 'starter.py'
    if starter_file.exists():
        return starter_file.read_text(encoding='utf-8')
    return ""

def generate_hints_for_exercise(exercise_path, topic):
    """Genera hints personalizados basándose en el ejercicio"""
    
    exercise_name = exercise_path.name
    prompt_content = read_prompt(exercise_path)
    starter_content = read_starter(exercise_path)
    
    # Estructura base de hints
    hints = []
    
    # HINTS ESPECÍFICOS POR TIPO DE EJERCICIO
    
    # Estructuras Secuenciales
    if topic == "Estructuras Secuenciales":
        hints.append({
            "title": "💡 Estructura básica",
            "content": "Recuerda que en un programa secuencial, las instrucciones se ejecutan una tras otra en orden. Primero lees datos con `input()`, luego procesas, y finalmente imprimes el resultado con `print()`."
        })
        
        if "input()" in prompt_content:
            hints.append({
                "title": "📥 Lectura de datos",
                "content": "Usa `input()` para leer texto y conviértelo al tipo apropiado: `int(input())` para enteros, `float(input())` para decimales. No imprimas mensajes de solicitud."
            })
        
        if "print" in prompt_content.lower():
            hints.append({
                "title": "📤 Salida de datos",
                "content": "Verifica que tu salida sea exactamente como se pide. Usa `print()` sin texto adicional y asegúrate de que el formato coincida con los ejemplos."
            })
    
    # Estructuras Condicionales
    elif topic == "Estructuras Condicionales":
        hints.append({
            "title": "💡 Condicionales en Python",
            "content": "Usa `if`, `elif` y `else` para tomar decisiones. La sintaxis es: `if condicion:` seguido de código indentado. Verifica que uses los operadores correctos: `==`, `!=`, `>`, `<`, `>=`, `<=`."
        })
        
        if ">=" in prompt_content or "<=" in prompt_content:
            hints.append({
                "title": "⚠️ Mayor/Menor o igual",
                "content": "Los operadores `>=` y `<=` incluyen el valor de comparación. Por ejemplo: `edad >= 18` es verdadero para 18, 19, 20, etc."
            })
        
        hints.append({
            "title": "🎯 Casos borde",
            "content": "Presta especial atención a los valores límite mencionados en los ejemplos. Asegúrate de que tu condición los maneje correctamente."
        })
        
        if "mensaje" in prompt_content.lower() or "exacta" in prompt_content.lower():
            hints.append({
                "title": "📝 Mensajes exactos",
                "content": "Los mensajes de salida deben ser EXACTAMENTE como se especifican: mismas mayúsculas, minúsculas, espacios y puntuación. Copia el texto literal de los ejemplos."
            })
    
    # Estructuras Repetitivas
    elif topic == "Estructuras Repetitivas":
        hints.append({
            "title": "💡 Ciclos en Python",
            "content": "Python ofrece dos tipos de ciclos: `for` (cuando sabes cuántas iteraciones) y `while` (cuando la condición determina cuándo parar). Elige el más apropiado para tu problema."
        })
        
        if "range" in prompt_content or "range" in starter_content:
            hints.append({
                "title": "🔢 Uso de range()",
                "content": "`range(n)` genera números de 0 a n-1. `range(1, n+1)` genera de 1 a n. `range(inicio, fin, paso)` permite controlar el incremento. Para contar hacia atrás usa paso negativo."
            })
        
        if "acumulador" in prompt_content.lower() or "suma" in exercise_name:
            hints.append({
                "title": "📊 Patrón acumulador",
                "content": "Inicializa una variable en 0 antes del ciclo (ej: `suma = 0`). Dentro del ciclo, agrégale valores: `suma += i`. Al final del ciclo tendrás el total acumulado."
            })
        
        if "contador" in prompt_content.lower() or "contar" in exercise_name:
            hints.append({
                "title": "🔢 Patrón contador",
                "content": "Inicializa una variable en 0 antes del ciclo (ej: `contador = 0`). Cuando se cumple una condición, incrementa: `contador += 1`. Al final tendrás cuántas veces se cumplió."
            })
    
    # Funciones
    elif topic == "Funciones":
        hints.append({
            "title": "💡 Definición de funciones",
            "content": "Una función se define con `def nombre(parametros):` y debe `return` un valor. Los parámetros son las variables que recibe, el return es lo que devuelve al que la llama."
        })
        
        hints.append({
            "title": "🔄 Return vs Print",
            "content": "No confundas `return` con `print()`. `return` devuelve un valor para ser usado por quien llamó la función. `print()` solo muestra en pantalla. Lee bien qué se pide."
        })
        
        if "parametro" in prompt_content.lower() or "argumentos" in prompt_content.lower():
            hints.append({
                "title": "📥 Parámetros de función",
                "content": "Los parámetros se declaran entre paréntesis al definir la función: `def calcular(a, b, c):`. Dentro de la función, usas esos nombres como variables."
            })
    
    # Listas
    elif topic == "Listas":
        hints.append({
            "title": "💡 Trabajando con listas",
            "content": "Las listas en Python son colecciones ordenadas y mutables. Se crean con `[]` o `list()`. Accede a elementos por índice: `lista[0]` es el primero, `lista[-1]` es el último."
        })
        
        if ".append" in starter_content or "agregar" in exercise_name:
            hints.append({
                "title": "➕ Agregar elementos",
                "content": "Usa `lista.append(elemento)` para agregar al final. Usa `lista.insert(indice, elemento)` para insertar en una posición específica."
            })
        
        if "recorrer" in prompt_content.lower() or "for" in starter_content:
            hints.append({
                "title": "🔄 Iterar sobre listas",
                "content": "Para recorrer una lista: `for elemento in lista:` itera sobre valores. `for i in range(len(lista)):` itera sobre índices. Elige según necesites el valor o la posición."
            })
        
        if "sum" in exercise_name or "promedio" in exercise_name:
            hints.append({
                "title": "📊 Funciones útiles",
                "content": "`sum(lista)` suma todos los elementos. `len(lista)` da la cantidad. `max(lista)` y `min(lista)` dan el mayor y menor. Úsalas cuando corresponda."
            })
    
    # Estructuras de datos complejas
    elif topic == "Estructuras de datos complejas":
        hints.append({
            "title": "💡 Estructuras de datos",
            "content": "Python ofrece: listas `[]` (ordenadas, mutables), tuplas `()` (ordenadas, inmutables), diccionarios `{}` (pares clave-valor), y sets `{}` (únicos, sin orden). Elige la estructura apropiada."
            })
        
        if "diccionario" in exercise_name or "{}" in starter_content:
            hints.append({
                "title": "📖 Trabajando con diccionarios",
                "content": "Diccionarios usan pares clave-valor: `d = {'nombre': 'Juan', 'edad': 25}`. Accede con `d['nombre']`. Agrega con `d['nueva'] = valor`. Itera con `for k, v in d.items():`."
            })
        
        if "set" in exercise_name.lower() or "conjunto" in prompt_content.lower():
            hints.append({
                "title": "🔶 Sets (conjuntos)",
                "content": "Sets no permiten duplicados y no tienen orden: `s = {1, 2, 3}`. Usa `s.add(x)` para agregar, `s.remove(x)` para quitar. Útiles para operaciones de conjuntos: unión, intersección, diferencia."
            })
        
        if "tupla" in exercise_name:
            hints.append({
                "title": "📌 Tuplas inmutables",
                "content": "Las tuplas son como listas pero inmutables (no se pueden modificar): `t = (1, 2, 3)`. Útiles para agrupar datos relacionados que no deben cambiar."
            })
    
    # Recursividad
    elif topic == "Recursividad":
        hints.append({
            "title": "💡 Concepto de recursividad",
            "content": "Una función recursiva se llama a sí misma. SIEMPRE debe tener: 1) Caso base (cuándo detenerse), 2) Caso recursivo (llamada a sí misma con un problema más pequeño). Sin caso base, hay recursión infinita."
        })
        
        hints.append({
            "title": "🛑 Caso base",
            "content": "El caso base es la condición de parada. Debe ser una situación simple que puedas resolver sin recursión. Ejemplo: en factorial, si n=0 o n=1, retorna 1 sin llamarse nuevamente."
        })
        
        hints.append({
            "title": "🔄 Caso recursivo",
            "content": "El caso recursivo resuelve un problema grande usando la solución de uno más pequeño. Ejemplo: factorial(n) = n * factorial(n-1). Asegúrate de que cada llamada recursiva acerque al caso base."
        })
        
        if "factorial" in exercise_name:
            hints.append({
                "title": "📚 Ejemplo: Factorial",
                "content": "```python\ndef factorial(n):\n    if n == 0 or n == 1:  # Caso base\n        return 1\n    else:  # Caso recursivo\n        return n * factorial(n - 1)\n```"
            })
        
        if "fibonacci" in exercise_name:
            hints.append({
                "title": "📚 Ejemplo: Fibonacci",
                "content": "```python\ndef fibonacci(n):\n    if n == 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n```"
            })
    
    # Agregar hint de debugging siempre
    hints.append({
        "title": "🐛 Debugging",
        "content": "Si tu código no funciona: 1) Imprime valores intermedios para ver qué está pasando, 2) Prueba con los ejemplos dados, 3) Verifica tipos de datos, 4) Revisa la indentación. Usa `print()` para depurar."
    })
    
    # Crear el archivo hints.json
    hints_data = {
        "hints": hints,
        "total_hints": len(hints)
    }
    
    return hints_data

def main():
    base_path = Path(r'c:\Users\juani\Desktop\Proyecto Py\backend\problems\Programacion I')
    
    topics = [
        'Estructuras Secuenciales',
        'Estructuras Condicionales',
        'Estructuras Repetitivas',
        'Funciones',
        'Listas',
        'Estructuras de datos complejas',
        'Recursividad'
    ]
    
    total_generated = 0
    
    print("=" * 80)
    print("GENERANDO HINTS.JSON PARA TODOS LOS EJERCICIOS")
    print("=" * 80)
    print()
    
    for topic in topics:
        topic_path = base_path / topic
        if not topic_path.exists():
            continue
        
        print(f"\n📁 {topic}")
        print("-" * 80)
        
        exercises = sorted([d for d in topic_path.iterdir() if d.is_dir()])
        
        for exercise in exercises:
            hints_file = exercise / 'hints.json'
            
            if hints_file.exists():
                print(f"  ⏭️  {exercise.name:40} | Ya existe")
                continue
            
            # Generar hints
            hints_data = generate_hints_for_exercise(exercise, topic)
            
            # Guardar archivo
            with open(hints_file, 'w', encoding='utf-8') as f:
                json.dump(hints_data, f, indent=2, ensure_ascii=False)
            
            total_generated += 1
            print(f"  ✅ {exercise.name:40} | {hints_data['total_hints']} hints generados")
    
    print("\n" + "=" * 80)
    print(f"✅ COMPLETADO: {total_generated} archivos hints.json generados")
    print("=" * 80)

if __name__ == "__main__":
    main()
