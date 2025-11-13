"""
Script para mejorar los archivos starter.py
Agrega mejores comentarios TODO y estructura más clara
"""

from pathlib import Path
import re

def read_prompt_for_context(exercise_path):
    """Lee el prompt para entender qué necesita el estudiante"""
    prompt_file = exercise_path / 'prompt.md'
    if prompt_file.exists():
        return prompt_file.read_text(encoding='utf-8')
    return ""

def read_solution(exercise_path):
    """Lee la solución para ver la estructura correcta"""
    solution_file = exercise_path / 'solution_reference.py'
    if solution_file.exists():
        return solution_file.read_text(encoding='utf-8')
    return ""

def improve_starter(exercise_path):
    """Mejora el archivo starter.py con mejores comentarios y estructura"""
    
    starter_file = exercise_path / 'starter.py'
    if not starter_file.exists():
        return False
    
    starter_content = starter_file.read_text(encoding='utf-8')
    prompt = read_prompt_for_context(exercise_path)
    solution = read_solution(exercise_path)
    
    exercise_name = exercise_path.name
    topic = exercise_path.parent.name
    
    # Si el starter ya tiene buenos comentarios, no modificar
    todo_count = starter_content.count('TODO')
    if todo_count >= 4 and len(starter_content) > 200:
        return False
    
    # Detectar si es un ejercicio simple o complejo
    is_simple = len(solution) < 150
    
    # Crear un mejor starter basándose en el tipo de ejercicio
    new_starter = ""
    
    # Header con descripción
    new_starter += f'"""\n'
    new_starter += f'{exercise_name.replace("_", " ").title()}\n'
    new_starter += f'Tema: {topic}\n'
    new_starter += f'"""\n\n'
    
    # Importar bibliotecas si la solución las usa
    if 'import math' in solution:
        new_starter += 'import math\n\n'
    if 'import random' in solution:
        new_starter += 'import random\n\n'
    
    # Verificar si el ejercicio usa funciones auxiliares
    function_defs = re.findall(r'def (\w+)\(', solution)
    has_helper_functions = len(function_defs) > 1  # Más que solo main
    
    if has_helper_functions:
        # Agregar esqueleto de funciones auxiliares
        for func_name in function_defs:
            if func_name != 'main':
                # Extraer parámetros de la función
                match = re.search(rf'def {func_name}\((.*?)\)', solution)
                params = match.group(1) if match else ''
                
                new_starter += f'def {func_name}({params}):\n'
                new_starter += f'    """\n'
                new_starter += f'    TODO: Implementar la lógica de {func_name}\n'
                
                # Detectar si es recursiva
                if func_name in solution and f'{func_name}(' in solution[solution.find(f'def {func_name}'):]:
                    new_starter += f'    Esta función es RECURSIVA - debe llamarse a sí misma\n'
                    new_starter += f'    Recuerda: necesitas un caso base y un caso recursivo\n'
                
                new_starter += f'    """\n'
                new_starter += f'    pass  # Reemplaza esto con tu código\n\n'
    
    # Función main
    new_starter += 'def main():\n'
    new_starter += '    """\n'
    new_starter += '    Función principal del programa\n'
    new_starter += '    """\n'
    
    # Analizar qué hace el programa para dar mejores hints
    needs_input = 'input()' in solution
    uses_loop = 'for ' in solution or 'while ' in solution
    uses_conditional = 'if ' in solution
    returns_value = 'return ' in solution
    prints_output = 'print(' in solution
    
    step = 1
    
    if needs_input:
        # Detectar tipo de entrada
        if 'int(input())' in solution:
            new_starter += f'    # TODO {step}: Lee un número entero con int(input())\n'
        elif 'float(input())' in solution:
            new_starter += f'    # TODO {step}: Lee un número decimal con float(input())\n'
        elif '.split()' in solution:
            new_starter += f'    # TODO {step}: Lee y separa la entrada con input().split()\n'
        else:
            new_starter += f'    # TODO {step}: Lee la entrada del usuario\n'
        step += 1
    
    if uses_loop and topic == 'Estructuras Repetitivas':
        if 'range(' in solution:
            new_starter += f'    # TODO {step}: Crea un ciclo for con range()\n'
        elif 'while ' in solution:
            new_starter += f'    # TODO {step}: Crea un ciclo while con la condición apropiada\n'
        step += 1
        
        if 'suma' in exercise_name or 'acumulador' in prompt.lower():
            new_starter += f'    # TODO {step}: Inicializa un acumulador en 0 antes del ciclo\n'
            step += 1
        
        if 'contador' in prompt.lower() or 'contar' in exercise_name:
            new_starter += f'    # TODO {step}: Inicializa un contador en 0 antes del ciclo\n'
            step += 1
    
    if uses_conditional and topic == 'Estructuras Condicionales':
        new_starter += f'    # TODO {step}: Usa if/elif/else para tomar decisiones\n'
        new_starter += f'    # Verifica bien las condiciones (>, <, >=, <=, ==, !=)\n'
        step += 1
    
    if has_helper_functions:
        for func_name in function_defs:
            if func_name != 'main':
                new_starter += f'    # TODO {step}: Llama a la función {func_name}() con los parámetros apropiados\n'
                step += 1
    
    if prints_output:
        if 'f"' in solution or "f'" in solution:
            new_starter += f'    # TODO {step}: Imprime el resultado usando f-strings o print() directamente\n'
        else:
            new_starter += f'    # TODO {step}: Imprime el resultado (verifica el formato exacto)\n'
        step += 1
    
    new_starter += '    pass  # Reemplaza esto con tu código\n\n'
    
    # Agregar el bloque if __name__
    new_starter += 'if __name__ == "__main__":\n'
    new_starter += '    main()\n'
    
    # Solo actualizar si el nuevo starter es significativamente mejor
    if len(new_starter) > len(starter_content) * 1.2 or todo_count < 2:
        starter_file.write_text(new_starter, encoding='utf-8')
        return True
    
    return False

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
    
    total_improved = 0
    
    print("=" * 80)
    print("MEJORANDO ARCHIVOS STARTER.PY")
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
            starter_file = exercise / 'starter.py'
            
            if not starter_file.exists():
                print(f"  ❌ {exercise.name:40} | Falta starter.py")
                continue
            
            original_content = starter_file.read_text(encoding='utf-8')
            original_length = len(original_content)
            original_todos = original_content.count('TODO')
            
            if improve_starter(exercise):
                new_content = starter_file.read_text(encoding='utf-8')
                new_length = len(new_content)
                new_todos = new_content.count('TODO')
                
                total_improved += 1
                growth = ((new_length - original_length) / original_length) * 100
                print(f"  ⬆️  {exercise.name:40} | {original_todos} → {new_todos} TODOs (+{growth:.0f}%)")
            else:
                print(f"  ✅ {exercise.name:40} | {original_todos} TODOs (OK)")
    
    print("\n" + "=" * 80)
    print(f"✅ COMPLETADO: {total_improved} archivos starter.py mejorados")
    print("=" * 80)

if __name__ == "__main__":
    main()
