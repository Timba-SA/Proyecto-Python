"""
Script para ajustar las proporciones de tests públicos/ocultos en rubrics.
Objetivo: 70% públicos (7 puntos) / 30% ocultos (3 puntos) sobre 10 puntos totales.
"""

import json
from pathlib import Path

def ajustar_rubric(rubric_path):
    """Ajusta un rubric para tener 7 pts públicos y 3 pts ocultos."""
    with open(rubric_path, 'r', encoding='utf-8') as f:
        rubric = json.load(f)
    
    # Contar tests por visibilidad
    tests_publicos = [t for t in rubric['tests'] if t['visibility'] == 'public']
    tests_ocultos = [t for t in rubric['tests'] if t['visibility'] == 'hidden']
    
    total_tests = len(tests_publicos) + len(tests_ocultos)
    
    if total_tests == 0:
        return None, "Sin tests"
    
    # Calcular puntos actuales
    pts_publicos_actual = sum(t['points'] for t in tests_publicos)
    pts_ocultos_actual = sum(t['points'] for t in tests_ocultos)
    
    # Si ya está en 7/3, no hacer nada
    if pts_publicos_actual == 7 and pts_ocultos_actual == 3:
        return None, "Ya correcto (7/3)"
    
    # Calcular nueva distribución
    # Objetivo: 7 puntos públicos, 3 puntos ocultos
    pts_publicos_objetivo = 7
    pts_ocultos_objetivo = 3
    
    # Distribuir puntos equitativamente entre tests del mismo tipo
    if len(tests_publicos) > 0:
        # Asignar 1 punto a cada test público primero
        for test in tests_publicos:
            test['points'] = 1
        
        # Distribuir los puntos restantes
        puntos_restantes = pts_publicos_objetivo - len(tests_publicos)
        for i in range(puntos_restantes):
            tests_publicos[i % len(tests_publicos)]['points'] += 1
    
    if len(tests_ocultos) > 0:
        # Asignar 1 punto a cada test oculto primero
        for test in tests_ocultos:
            test['points'] = 1
        
        # Distribuir los puntos restantes
        puntos_restantes = pts_ocultos_objetivo - len(tests_ocultos)
        for i in range(puntos_restantes):
            tests_ocultos[i % len(tests_ocultos)]['points'] += 1
    
    # Verificar que sume exactamente 10
    total_nuevo = sum(t['points'] for t in rubric['tests'])
    if total_nuevo != 10:
        # Ajuste fino
        diff = 10 - total_nuevo
        if diff > 0:
            # Faltan puntos, agregar a públicos
            for i in range(diff):
                tests_publicos[i % len(tests_publicos)]['points'] += 1
        else:
            # Sobran puntos, quitar de públicos
            for i in range(abs(diff)):
                if tests_publicos[i % len(tests_publicos)]['points'] > 1:
                    tests_publicos[i % len(tests_publicos)]['points'] -= 1
    
    rubric['max_points'] = 10
    
    # Guardar
    with open(rubric_path, 'w', encoding='utf-8') as f:
        json.dump(rubric, f, indent=2, ensure_ascii=False)
    
    pts_publicos_nuevo = sum(t['points'] for t in tests_publicos)
    pts_ocultos_nuevo = sum(t['points'] for t in tests_ocultos)
    
    return (pts_publicos_actual, pts_ocultos_actual, pts_publicos_nuevo, pts_ocultos_nuevo), "Ajustado"


def main():
    base_path = Path(r"c:\Users\juani\Desktop\Proyecto-Python\backend\problems\Programacion I")
    
    print("\n=== AJUSTANDO PROPORCIONES DE RUBRICS ===\n")
    print("Objetivo: 7 pts públicos (70%) / 3 pts ocultos (30%)\n")
    
    ajustados = 0
    ya_correctos = 0
    errores = 0
    
    # Recorrer todos los rubrics
    for rubric_path in base_path.rglob("rubric.json"):
        ejercicio = rubric_path.parent.name
        resultado, mensaje = ajustar_rubric(rubric_path)
        
        if resultado:
            old_pub, old_ocu, new_pub, new_ocu = resultado
            print(f"✓ {ejercicio:35} {old_pub}/{old_ocu} → {new_pub}/{new_ocu}")
            ajustados += 1
        elif "Ya correcto" in mensaje:
            ya_correctos += 1
        else:
            print(f"✗ {ejercicio:35} {mensaje}")
            errores += 1
    
    print(f"\n--- RESUMEN ---")
    print(f"Ajustados: {ajustados}")
    print(f"Ya correctos: {ya_correctos}")
    print(f"Errores: {errores}")
    print(f"Total: {ajustados + ya_correctos + errores}")


if __name__ == "__main__":
    main()
