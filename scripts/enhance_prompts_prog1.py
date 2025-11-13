"""
Script para mejorar la calidad de los prompts de ejercicios
Agrega secciones faltantes y mejora el contenido existente
"""

import re
from pathlib import Path

def analyze_prompt(prompt_content):
    """Analiza qué secciones tiene y cuáles faltan"""
    sections = {
        'objetivo': '## 🎯 Objetivo' in prompt_content,
        'entrada': '## 📥 Entrada' in prompt_content,
        'salida': '## 📤 Salida' in prompt_content or '## 📤 Salida Esperada' in prompt_content,
        'ejemplos': '## 📋 Ejemplos' in prompt_content or '## 📋 Ejemplo' in prompt_content,
        'restricciones': '## ⚙️ Restricciones' in prompt_content,
        'pistas': '## 💡 Pistas' in prompt_content or '## 💡 Pista' in prompt_content,
        'errores': '## ⚠️ Errores Comunes' in prompt_content,
    }
    
    return sections

def enhance_prompt(exercise_path, prompt_content):
    """Mejora el contenido del prompt agregando secciones faltantes"""
    
    sections = analyze_prompt(prompt_content)
    exercise_name = exercise_path.name
    topic = exercise_path.parent.name
    
    # Si el prompt ya está completo, no modificar
    if all(sections.values()):
        return prompt_content, False
    
    # Si es muy corto, necesita más contenido
    needs_expansion = len(prompt_content) < 800
    
    enhanced = prompt_content
    modifications = []
    
    # Agregar sección de restricciones si falta
    if not sections['restricciones'] and needs_expansion:
        restriction_section = """
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
"""
        # Insertar antes de la última sección o al final
        if '## 💡 Pistas' in enhanced or '## 💡 Pista' in enhanced:
            enhanced = enhanced.replace('## 💡 Pista', restriction_section + '\n## 💡 Pista')
        elif '## ⚠️' in enhanced:
            enhanced = enhanced.replace('## ⚠️', restriction_section + '\n## ⚠️')
        else:
            enhanced += '\n' + restriction_section
        
        modifications.append('Agregada sección de Restricciones Técnicas')
    
    # Mejorar sección de ejemplos si es muy básica
    if sections['ejemplos'] and needs_expansion:
        # Verificar si tiene al menos 2 ejemplos
        example_count = enhanced.count('**Ejemplo')
        if example_count < 2:
            # Buscar dónde está la sección de ejemplos
            if '## 📋 Ejemplos' in enhanced:
                example_marker = '## 📋 Ejemplos'
            else:
                example_marker = '## 📋 Ejemplo'
            
            # Encontrar la siguiente sección
            parts = enhanced.split(example_marker)
            if len(parts) >= 2:
                before = parts[0] + example_marker
                after_parts = parts[1].split('##', 1)
                example_section = after_parts[0]
                rest = '##' + after_parts[1] if len(after_parts) > 1 else ''
                
                # Agregar nota sobre casos de prueba adicionales
                additional_examples = """

**Nota**: Estos son algunos ejemplos. Tu solución será probada con casos adicionales, incluyendo casos borde y situaciones especiales.
"""
                enhanced = before + example_section + additional_examples + rest
                modifications.append('Mejorada sección de Ejemplos')
    
    # Agregar sección de errores comunes si falta y el ejercicio es complejo
    if not sections['errores'] and needs_expansion and topic in ['Estructuras Condicionales', 'Estructuras Repetitivas', 'Recursividad']:
        errors_section = """
## ⚠️ Errores Comunes a Evitar

**Error 1: Formato de salida incorrecto**
```python
# ❌ INCORRECTO - Texto adicional
print(f"El resultado es: {resultado}")
```
```python
# ✅ CORRECTO - Solo el resultado
print(resultado)
```

**Error 2: No convertir tipos de datos**
```python
# ❌ INCORRECTO - input() devuelve string
valor = input()
```
```python
# ✅ CORRECTO - Convertir al tipo apropiado
valor = int(input())  # Para enteros
```

**Error 3: Indentación incorrecta**
```python
# ❌ INCORRECTO - Mala indentación
def main():
resultado = 42
print(resultado)
```
```python
# ✅ CORRECTO - Indentación correcta
def main():
    resultado = 42
    print(resultado)
```
"""
        # Agregar al final
        enhanced += '\n' + errors_section
        modifications.append('Agregada sección de Errores Comunes')
    
    return enhanced, len(modifications) > 0

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
    print("MEJORANDO PROMPTS DE EJERCICIOS")
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
            prompt_file = exercise / 'prompt.md'
            
            if not prompt_file.exists():
                print(f"  ❌ {exercise.name:40} | Falta prompt.md")
                continue
            
            prompt_content = prompt_file.read_text(encoding='utf-8')
            original_length = len(prompt_content)
            
            enhanced_content, modified = enhance_prompt(exercise, prompt_content)
            new_length = len(enhanced_content)
            
            if modified:
                # Guardar el prompt mejorado
                prompt_file.write_text(enhanced_content, encoding='utf-8')
                total_improved += 1
                growth = ((new_length - original_length) / original_length) * 100
                print(f"  ⬆️  {exercise.name:40} | {original_length} → {new_length} chars (+{growth:.0f}%)")
            else:
                sections = analyze_prompt(prompt_content)
                complete = sum(sections.values())
                print(f"  ✅ {exercise.name:40} | {complete}/7 secciones (OK)")
    
    print("\n" + "=" * 80)
    print(f"✅ COMPLETADO: {total_improved} prompts mejorados")
    print("=" * 80)

if __name__ == "__main__":
    main()
