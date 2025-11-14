"""
Script para corregir problemas de encoding en metadata.json
Convierte caracteres mojibake a sus equivalentes correctos en UTF-8
"""

import json
from pathlib import Path

# Mapeo de caracteres mal codificados a correctos
FIXES = {
    'Ã¡': 'á',
    'Ã©': 'é',
    'Ã­': 'í',
    'Ã³': 'ó',
    'Ãº': 'ú',
    'Ã±': 'ñ',
    'Ã': 'Á',
    'Ã‰': 'É',
    'Ã': 'Í',
    'Ã"': 'Ó',
    'Ãš': 'Ú',
    'Ã¼': 'ü',
    'Ãƒ': 'Ã',  # Doble encoding
    'ÃƒÂ¡': 'á',
    'ÃƒÂ­': 'í',
    'ÃƒÂ³': 'ó',
}

def fix_text(text):
    """Fix mojibake characters in text"""
    if not isinstance(text, str):
        return text
    
    result = text
    for wrong, correct in FIXES.items():
        result = result.replace(wrong, correct)
    return result

def fix_dict(data):
    """Recursively fix all strings in a dictionary"""
    if isinstance(data, dict):
        return {key: fix_dict(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [fix_dict(item) for item in data]
    elif isinstance(data, str):
        return fix_text(data)
    else:
        return data

def main():
    base_path = Path(r"c:\Users\juani\Desktop\Proyecto-Python\backend\problems\Programacion I")
    
    print("\n=== CORRIGIENDO ENCODING EN METADATA.JSON ===\n")
    
    fixed_count = 0
    total_count = 0
    
    for metadata_path in base_path.rglob("metadata.json"):
        total_count += 1
        
        # Leer archivo con UTF-8
        with open(metadata_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Si tiene caracteres problemáticos, corregir
        if any(wrong in content for wrong in FIXES.keys()):
            ejercicio = metadata_path.parent.name
            
            # Parsear JSON
            data = json.loads(content)
            
            # Mostrar título antes
            old_title = data.get('title', '')
            
            # Corregir todos los strings
            fixed_data = fix_dict(data)
            
            # Mostrar título después
            new_title = fixed_data.get('title', '')
            
            print(f"✓ {ejercicio:35} {old_title} → {new_title}")
            
            # Guardar con UTF-8 sin BOM
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(fixed_data, f, indent=2, ensure_ascii=False)
            
            fixed_count += 1
    
    print(f"\n--- RESUMEN ---")
    print(f"Total archivos: {total_count}")
    print(f"Corregidos: {fixed_count}")
    print(f"Sin cambios: {total_count - fixed_count}")


if __name__ == "__main__":
    main()
