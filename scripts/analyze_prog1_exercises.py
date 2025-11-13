"""
Script para analizar todos los ejercicios de Programación I
y generar un reporte de mejoras necesarias
"""

import os
import json
from pathlib import Path
from collections import defaultdict

def analyze_exercise(exercise_path):
    """Analiza un ejercicio individual y retorna métricas de calidad"""
    metrics = {
        'path': str(exercise_path),
        'name': exercise_path.name,
        'topic': exercise_path.parent.name,
        'has_prompt': False,
        'has_starter': False,
        'has_solution': False,
        'has_tests_public': False,
        'has_tests_hidden': False,
        'has_rubric': False,
        'has_hints': False,
        'prompt_quality': 0,
        'starter_quality': 0,
        'test_quality': 0,
        'issues': []
    }
    
    # Verificar existencia de archivos
    prompt_file = exercise_path / 'prompt.md'
    starter_file = exercise_path / 'starter.py'
    solution_file = exercise_path / 'solution_reference.py'
    tests_public_file = exercise_path / 'tests_public.py'
    tests_hidden_file = exercise_path / 'tests_hidden.py'
    rubric_file = exercise_path / 'rubric.json'
    hints_file = exercise_path / 'hints.json'
    
    metrics['has_prompt'] = prompt_file.exists()
    metrics['has_starter'] = starter_file.exists()
    metrics['has_solution'] = solution_file.exists()
    metrics['has_tests_public'] = tests_public_file.exists()
    metrics['has_tests_hidden'] = tests_hidden_file.exists()
    metrics['has_rubric'] = rubric_file.exists()
    metrics['has_hints'] = hints_file.exists()
    
    # Analizar calidad del prompt
    if metrics['has_prompt']:
        try:
            content = prompt_file.read_text(encoding='utf-8')
            # Criterios de calidad del prompt
            if '## 🎯 Objetivo' in content:
                metrics['prompt_quality'] += 1
            if '## 📥 Entrada' in content:
                metrics['prompt_quality'] += 1
            if '## 📤 Salida' in content or '## 📤 Salida Esperada' in content:
                metrics['prompt_quality'] += 1
            if '## 📋 Ejemplos' in content or '## 📋 Ejemplo' in content:
                metrics['prompt_quality'] += 1
            if '## 💡 Pistas' in content or '## 💡 Pista' in content:
                metrics['prompt_quality'] += 1
            if '## ⚠️ Errores Comunes' in content:
                metrics['prompt_quality'] += 1
            if len(content) < 500:
                metrics['issues'].append('Prompt muy corto')
        except Exception as e:
            metrics['issues'].append(f'Error leyendo prompt: {e}')
    else:
        metrics['issues'].append('Falta archivo prompt.md')
    
    # Analizar calidad del starter
    if metrics['has_starter']:
        try:
            content = starter_file.read_text(encoding='utf-8')
            if 'def main():' in content:
                metrics['starter_quality'] += 1
            if 'TODO' in content:
                metrics['starter_quality'] += 1
            if 'if __name__ == "__main__":' in content:
                metrics['starter_quality'] += 1
            if len(content.strip()) < 50:
                metrics['issues'].append('Starter muy simple')
        except Exception as e:
            metrics['issues'].append(f'Error leyendo starter: {e}')
    else:
        metrics['issues'].append('Falta archivo starter.py')
    
    # Analizar calidad de tests
    if metrics['has_tests_public']:
        try:
            content = tests_public_file.read_text(encoding='utf-8')
            test_count = content.count('def test_')
            metrics['test_quality'] = test_count
            if test_count < 3:
                metrics['issues'].append(f'Pocos tests públicos ({test_count})')
            if 'assert' not in content:
                metrics['issues'].append('Tests sin assertions')
        except Exception as e:
            metrics['issues'].append(f'Error leyendo tests: {e}')
    else:
        metrics['issues'].append('Falta archivo tests_public.py')
    
    # Verificar hints
    if not metrics['has_hints']:
        metrics['issues'].append('Falta archivo hints.json')
    
    # Verificar rubric
    if not metrics['has_rubric']:
        metrics['issues'].append('Falta archivo rubric.json')
    
    return metrics

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
    
    all_metrics = []
    topic_stats = defaultdict(lambda: {'total': 0, 'missing_hints': 0, 'missing_rubric': 0, 'low_quality': 0})
    
    print("=" * 80)
    print("ANÁLISIS DE EJERCICIOS DE PROGRAMACIÓN I")
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
            metrics = analyze_exercise(exercise)
            all_metrics.append(metrics)
            topic_stats[topic]['total'] += 1
            
            # Calcular puntuación de calidad
            quality_score = (
                metrics['prompt_quality'] * 10 +
                metrics['starter_quality'] * 10 +
                metrics['test_quality'] * 5 +
                (20 if metrics['has_hints'] else 0) +
                (10 if metrics['has_rubric'] else 0) +
                (10 if metrics['has_solution'] else 0)
            )
            
            # Mostrar estado
            status = "✅" if quality_score >= 80 else "⚠️" if quality_score >= 50 else "❌"
            print(f"  {status} {metrics['name']:40} | Score: {quality_score:3}/100", end="")
            
            if not metrics['has_hints']:
                topic_stats[topic]['missing_hints'] += 1
                print(" | ❌ hints", end="")
            if not metrics['has_rubric']:
                topic_stats[topic]['missing_rubric'] += 1
                print(" | ❌ rubric", end="")
            if quality_score < 50:
                topic_stats[topic]['low_quality'] += 1
            
            if metrics['issues']:
                print(f"\n      Issues: {', '.join(metrics['issues'])}")
            else:
                print()
    
    # Resumen general
    print("\n" + "=" * 80)
    print("RESUMEN POR TEMA")
    print("=" * 80)
    
    total_exercises = 0
    total_missing_hints = 0
    total_missing_rubric = 0
    total_low_quality = 0
    
    for topic, stats in topic_stats.items():
        total_exercises += stats['total']
        total_missing_hints += stats['missing_hints']
        total_missing_rubric += stats['missing_rubric']
        total_low_quality += stats['low_quality']
        
        print(f"\n{topic}:")
        print(f"  Total ejercicios: {stats['total']}")
        print(f"  Sin hints.json: {stats['missing_hints']}")
        print(f"  Sin rubric.json: {stats['missing_rubric']}")
        print(f"  Baja calidad: {stats['low_quality']}")
    
    print("\n" + "=" * 80)
    print("TOTALES")
    print("=" * 80)
    print(f"Total de ejercicios: {total_exercises}")
    print(f"Ejercicios sin hints.json: {total_missing_hints}")
    print(f"Ejercicios sin rubric.json: {total_missing_rubric}")
    print(f"Ejercicios de baja calidad: {total_low_quality}")
    print()
    
    # Guardar reporte detallado
    report_path = base_path.parent.parent.parent / 'PROG1_ANALYSIS_REPORT.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            'summary': {
                'total_exercises': total_exercises,
                'missing_hints': total_missing_hints,
                'missing_rubric': total_missing_rubric,
                'low_quality': total_low_quality
            },
            'by_topic': dict(topic_stats),
            'all_metrics': all_metrics
        }, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Reporte detallado guardado en: {report_path}")

if __name__ == "__main__":
    main()
