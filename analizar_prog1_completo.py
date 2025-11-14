"""
Script para analizar todos los ejercicios de Programación I y detectar problemas
"""
import os
import json
import subprocess
from pathlib import Path
from collections import defaultdict

def analyze_all_prog1():
    """Analiza todos los ejercicios de Programación I"""
    base_path = Path("backend/problems/Programacion I")
    
    issues = defaultdict(list)
    stats = {
        "total": 0,
        "starter_empty": 0,
        "starter_with_solution": 0,
        "rubric_mismatch": 0,
        "missing_files": 0
    }
    
    for unit_dir in sorted(base_path.iterdir()):
        if not unit_dir.is_dir() or unit_dir.name.startswith('__'):
            continue
            
        print(f"\n{'='*80}")
        print(f"📚 {unit_dir.name}")
        print(f"{'='*80}")
        
        for exercise_dir in sorted(unit_dir.iterdir()):
            if not exercise_dir.is_dir() or exercise_dir.name.startswith('__'):
                continue
            
            stats["total"] += 1
            exercise_name = exercise_dir.name
            print(f"\n🔍 {exercise_name}")
            
            # Verificar archivos requeridos
            required_files = {
                "prompt.md": exercise_dir / "prompt.md",
                "starter.py": exercise_dir / "starter.py",
                "tests_public.py": exercise_dir / "tests_public.py",
                "tests_hidden.py": exercise_dir / "tests_hidden.py",
                "metadata.json": exercise_dir / "metadata.json",
                "rubric.json": exercise_dir / "rubric.json"
            }
            
            missing = []
            for name, path in required_files.items():
                if not path.exists():
                    missing.append(name)
            
            if missing:
                print(f"   ❌ Archivos faltantes: {', '.join(missing)}")
                issues[exercise_name].append(f"Falta: {', '.join(missing)}")
                stats["missing_files"] += 1
                continue
            
            # Analizar starter.py
            starter_content = required_files["starter.py"].read_text(encoding='utf-8')
            has_pass = 'pass' in starter_content
            has_return = 'return ' in starter_content and 'pass' not in starter_content
            
            if has_pass:
                print("   ✅ Starter vacío (con pass)")
                stats["starter_empty"] += 1
            elif has_return:
                print("   ⚠️  Starter tiene implementación")
                issues[exercise_name].append("Starter tiene código implementado")
                stats["starter_with_solution"] += 1
            else:
                print("   ⚠️  Starter sin pass ni return")
                issues[exercise_name].append("Starter en estado ambiguo")
            
            # Analizar rubric.json
            try:
                rubric = json.loads(required_files["rubric.json"].read_text(encoding='utf-8'))
                tests = rubric.get("tests", [])
                max_points = rubric.get("max_points", 0)
                total_points = sum(t.get("points", 0) for t in tests)
                
                if total_points != max_points:
                    print(f"   ⚠️  Rúbrica: suma={total_points} != max_points={max_points}")
                    issues[exercise_name].append(f"Rúbrica desbalanceada: {total_points} vs {max_points}")
                    stats["rubric_mismatch"] += 1
                else:
                    print(f"   ✅ Rúbrica: {total_points} puntos")
                    
                # Contar tests públicos vs ocultos
                public_count = sum(1 for t in tests if t.get("visibility") == "public")
                hidden_count = sum(1 for t in tests if t.get("visibility") == "hidden")
                print(f"   📊 Tests: {public_count} públicos, {hidden_count} ocultos")
                
            except json.JSONDecodeError:
                print("   ❌ Error al leer rubric.json")
                issues[exercise_name].append("rubric.json inválido")
            
            # Analizar metadata.json
            try:
                metadata = json.loads(required_files["metadata.json"].read_text(encoding='utf-8'))
                unit_id = metadata.get("unit_id", "")
                difficulty = metadata.get("difficulty", "")
                hints_count = len(metadata.get("hints", []))
                
                print(f"   📝 Unit: {unit_id}, Dificultad: {difficulty}, Hints: {hints_count}")
                
            except json.JSONDecodeError:
                print("   ❌ Error al leer metadata.json")
                issues[exercise_name].append("metadata.json inválido")
    
    # Resumen final
    print(f"\n\n{'='*80}")
    print("📊 RESUMEN GENERAL")
    print(f"{'='*80}")
    print(f"\nTotal de ejercicios analizados: {stats['total']}")
    print(f"  ✅ Starters vacíos: {stats['starter_empty']}")
    print(f"  ⚠️  Starters con solución: {stats['starter_with_solution']}")
    print(f"  ⚠️  Rúbricas desbalanceadas: {stats['rubric_mismatch']}")
    print(f"  ❌ Archivos faltantes: {stats['missing_files']}")
    
    if issues:
        print(f"\n\n{'='*80}")
        print("⚠️  PROBLEMAS ENCONTRADOS")
        print(f"{'='*80}")
        for exercise, problems in sorted(issues.items()):
            print(f"\n{exercise}:")
            for problem in problems:
                print(f"  - {problem}")
    else:
        print("\n\n✅ No se encontraron problemas!")
    
    # Guardar reporte
    report = {
        "stats": stats,
        "issues": dict(issues)
    }
    
    with open("analisis_prog1_completo.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Reporte guardado en: analisis_prog1_completo.json")

if __name__ == "__main__":
    analyze_all_prog1()
