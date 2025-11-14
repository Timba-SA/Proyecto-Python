#!/usr/bin/env python3
"""
Script definitivo para corregir todos los emojis mal codificados en hints.json
"""

import json
from pathlib import Path

def fix_all_emojis(text):
    """Corrige todos los patrones de emojis mal codificados."""
    # Mapeo completo de todos los emojis encontrados
    corrections = [
        # Bombilla 💡
        ('\u00f0\u0178\u2019\u00a1', '\U0001F4A1'),
        # Fuego 🔥
        ('\u00f0\u0178\u201c\u00a5', '\U0001F525'),
        # Letras 🔤
        ('\u00f0\u0178\u201c\u00a4', '\U0001F524'),
        # Bug 🐛 - varios patrones
        ('\u00f0\u0178\u0090\u203a', '\U0001F41B'),
        ('\u00c1\u00b0\u00c5\u00b8\u00c2\u0090\u00e2\u20ac\u00ba', '\U0001F41B'),  # Á°Å¸Ââ€º
        # Ciclo 🔄 - varios patrones
        ('\u00f0\u0178\u201c\u2020', '\U0001F504'),
        ('\u00f0\u0178\u201d\u201e', '\U0001F504'),  # ðŸ"„ nuevo patrón
        ('\u00c1\u00b0\u00c5\u00b8\u00e2\u20ac\u009d\u00e2\u20ac\u017e', '\U0001F504'),  # Á°Å¸â€â€ž
        # Números 🔢
        ('\u00f0\u0178\u201c\u00a2', '\U0001F522'),
        # Gráfico 📊
        ('\u00f0\u0178\u201c\u0160', '\U0001F4CA'),
        # Stop 🛑
        ('\u00f0\u0178\u203a\u2018', '\U0001F6D1'),
        # Nota 📝
        ('\u00f0\u0178\u201d\u0153', '\U0001F4DD'),
    ]
    
    result = text
    for wrong, correct in corrections:
        result = result.replace(wrong, correct)
    
    return result

def process_file(file_path):
    """Procesa un archivo JSON."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        fixed = fix_all_emojis(content)
        
        if fixed == original:
            return 'unchanged'
        
        # Validar JSON
        try:
            json.loads(fixed)
        except json.JSONDecodeError as e:
            print(f"❌ JSON inválido en {file_path.name}: {e}")
            return 'error'
        
        # Guardar
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        
        return 'fixed'
        
    except Exception as e:
        print(f"❌ Error en {file_path.name}: {e}")
        return 'error'

def main():
    """Procesa todos los hints.json."""
    base = Path(__file__).parent / 'backend' / 'problems' / 'Programacion I'
    
    files = sorted(base.glob('**/hints.json'))
    
    print(f"🔧 Corrigiendo emojis en {len(files)} archivos...\n")
    
    fixed = unchanged = errors = 0
    
    for f in files:
        result = process_file(f)
        if result == 'fixed':
            print(f"✅ {f.relative_to(base.parent)}")
            fixed += 1
        elif result == 'unchanged':
            unchanged += 1
        else:
            errors += 1
    
    print(f"\n📊 Resumen: ✅ {fixed} corregidos, ⚪ {unchanged} sin cambios, ❌ {errors} errores")

if __name__ == '__main__':
    main()
