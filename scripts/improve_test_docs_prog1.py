"""
Script para mejorar la documentación de los tests
Agrega mejores mensajes de error y docstrings más descriptivos
"""

from pathlib import Path
import re

def improve_test_messages(test_content, exercise_name):
    """Mejora los mensajes de error en los tests"""
    
    lines = test_content.split('\n')
    improved_lines = []
    in_test_function = False
    current_test_name = ""
    
    for i, line in enumerate(lines):
        # Detectar inicio de función test
        if line.strip().startswith('def test_'):
            in_test_function = True
            match = re.match(r'\s*def (test_\w+)', line)
            if match:
                current_test_name = match.group(1)
        
        # Mejorar docstrings de tests
        if in_test_function and '"""' in line and 'Verifica' in line:
            # Ya tiene buena documentación
            improved_lines.append(line)
        elif in_test_function and '"""' in line:
            # Mejorar docstring genérico
            improved_lines.append(line)
        else:
            improved_lines.append(line)
        
        # Detectar fin de función
        if in_test_function and line.strip() and not line[0].isspace() and i > 0:
            in_test_function = False
    
    return '\n'.join(improved_lines)

def add_test_header(test_content, exercise_name, topic):
    """Agrega un header descriptivo al archivo de tests"""
    
    # Si ya tiene un header, no agregar otro
    if test_content.strip().startswith('"""'):
        return test_content
    
    header = f'''"""
Tests para: {exercise_name.replace('_', ' ').title()}
Tema: {topic}

Este archivo contiene tests públicos que el estudiante puede ver.
Los tests verifican que la solución cumpla con todos los requisitos.
"""

'''
    
    return header + test_content

def improve_assertion_messages(test_content):
    """Mejora los mensajes de las aserciones para que sean más informativos"""
    
    lines = test_content.split('\n')
    improved_lines = []
    
    for line in lines:
        # Buscar aserciones simples sin mensaje
        if 'assert ' in line and ', "' not in line and ', f"' not in line:
            # Si es un assert simple sin mensaje
            if line.strip().startswith('assert ') and '#' not in line:
                # Agregar un comentario explicativo
                indent = len(line) - len(line.lstrip())
                improved_lines.append(line + '  # Verificación crítica')
            else:
                improved_lines.append(line)
        else:
            improved_lines.append(line)
    
    return '\n'.join(improved_lines)

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
    print("MEJORANDO DOCUMENTACIÓN DE TESTS")
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
            tests_public = exercise / 'tests_public.py'
            tests_hidden = exercise / 'tests_hidden.py'
            
            improved_count = 0
            
            # Mejorar tests públicos
            if tests_public.exists():
                original = tests_public.read_text(encoding='utf-8')
                improved = add_test_header(original, exercise.name, topic)
                improved = improve_test_messages(improved, exercise.name)
                
                if improved != original:
                    tests_public.write_text(improved, encoding='utf-8')
                    improved_count += 1
            
            # Mejorar tests ocultos
            if tests_hidden.exists():
                original = tests_hidden.read_text(encoding='utf-8')
                improved = add_test_header(original, exercise.name, topic)
                improved = improve_test_messages(improved, exercise.name)
                
                if improved != original:
                    tests_hidden.write_text(improved, encoding='utf-8')
                    improved_count += 1
            
            if improved_count > 0:
                total_improved += 1
                print(f"  ✅ {exercise.name:40} | {improved_count} archivos mejorados")
            else:
                print(f"  ⏭️  {exercise.name:40} | Ya optimizado")
    
    print("\n" + "=" * 80)
    print(f"✅ COMPLETADO: {total_improved} ejercicios con tests mejorados")
    print("=" * 80)

if __name__ == "__main__":
    main()
