#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corregir encoding mal convertido en metadata.json
Corrige caracteres que quedaron mal después de la primera corrección
"""

import json
import os
from pathlib import Path

# Mapeo de caracteres mal codificados a caracteres correctos
FIXES = {
    # Doble encoding - caracteres latinos
    'Íƒ¡': 'á',
    'Íƒ©': 'é', 
    'Íƒ­': 'í',
    'Íƒ³': 'ó',
    'Íƒº': 'ú',
    'Íƒ±': 'ñ',
    'ÍƒÂ¡': 'á',
    'ÍƒÂ©': 'é',
    'ÍƒÂ­': 'í',
    'ÍƒÂ³': 'ó',
    'ÍƒÂº': 'ú',
    'ÍƒÂ±': 'ñ',
    # Mayúsculas
    'Ánd': 'Índ',  # Fix para Índice que quedó como Ándice
    # Otros símbolos
    'Í—': '×',
    'Ï€': 'π',
    'Â²': '²',
}

def fix_string(text):
    """Corrige caracteres mal codificados en un string"""
    if not isinstance(text, str):
        return text
    
    result = text
    for wrong, correct in FIXES.items():
        result = result.replace(wrong, correct)
    
    return result

def fix_json_recursive(obj):
    """Corrige encoding en una estructura JSON recursivamente"""
    if isinstance(obj, dict):
        return {k: fix_json_recursive(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [fix_json_recursive(item) for item in obj]
    elif isinstance(obj, str):
        return fix_string(obj)
    else:
        return obj

def process_metadata_file(filepath):
    """Procesa un archivo metadata.json y corrige su encoding"""
    try:
        # Leer el archivo
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Guardar título original para comparación
        original_title = data.get('title', '')
        
        # Corregir encoding en toda la estructura
        fixed_data = fix_json_recursive(data)
        
        # Guardar con encoding correcto
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(fixed_data, f, ensure_ascii=False, indent=2)
        
        new_title = fixed_data.get('title', '')
        
        # Mostrar cambios
        folder_name = os.path.basename(os.path.dirname(filepath))
        if original_title != new_title:
            print(f"✓ {folder_name:35} {original_title} → {new_title}")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"✗ Error en {filepath}: {e}")
        return False

def main():
    """Procesa todos los archivos metadata.json en Programación I"""
    base_path = Path(__file__).parent.parent / 'backend' / 'problems' / 'Programacion I'
    
    print("=== CORRIGIENDO ENCODING V2 EN METADATA.JSON ===\n")
    
    total = 0
    fixed = 0
    
    # Buscar todos los metadata.json
    for metadata_file in base_path.rglob('metadata.json'):
        total += 1
        if process_metadata_file(metadata_file):
            fixed += 1
    
    print(f"\n--- RESUMEN ---")
    print(f"Total archivos: {total}")
    print(f"Corregidos: {fixed}")
    print(f"Sin cambios: {total - fixed}")

if __name__ == "__main__":
    main()
