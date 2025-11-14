#!/usr/bin/env python3
"""
Script para corregir puntos de código Unicode incorrectos en archivos JSON.
"""

import json
from pathlib import Path

def fix_unicode_codepoints(text):
    """Corrige puntos de código Unicode mal interpretados."""
    # Mapeo de secuencias incorrectas a emojis correctos
    corrections = [
        # Emoji de bombilla: U+F0 U+178 U+2019 U+A1 -> U+1F4A1
        ('\u00f0\u0178\u2019\u00a1', '\U0001F4A1'),  # 💡
        # Emoji de fuego
        ('\u00f0\u0178\u201c\u00a5', '\U0001F525'),  # 🔥
        # Emoji de letras
        ('\u00f0\u0178\u201c\u00a4', '\U0001F524'),  # 🔤
        # Emoji de bug - varias variantes
        ('\u00f0\u0178\u0090\u009b', '\U0001F41B'),  # 🐛
        ('ðŸ›', '\U0001F41B'),  # 🐛 - variante directa
        # Emoji de números
        ('\u00f0\u0178\u201c\u00a2', '\U0001F522'),  # 🔢
        # Emoji de gráfico
        ('\u00f0\u0178\u201c\u0160', '\U0001F4CA'),  # 📊
        # Emoji de ciclo - varias variantes
        ('\u00f0\u0178\u201c\u201e', '\U0001F504'),  # 🔄
        ('ðŸ"„', '\U0001F504'),  # 🔄 - variante directa
        ('Á°Å¸â€â€ž', '\U0001F504'),  # 🔄 - variante con Á
        # Emoji de nota
        ('\u00f0\u0178\u201d\u0153', '\U0001F4DD'),  # 📝
        # Emoji de stop
        ('\u00f0\u0178\u203a\u2018', '\U0001F6D1'),  # 🛑
        ('Á°Å¸Ââ€º', '\U0001F41B'),  # 🐛 - variante con Á
        # Lupa
        ('\u00f0\u0178\u201c\u008d', '\U0001F50D'),  # 🔍
        # Libros
        ('\u00f0\u0178\u201d\u0161', '\U0001F4DA'),  # 📚
        # Correcciones de palabras específicas
        ('Ášsalas', 'Úsalas'),
        ('Ãšsalas', 'Úsalas'),
    ]
    
    result = text
    for wrong, correct in corrections:
        result = result.replace(wrong, correct)
    
    return result

def process_json_file(file_path):
    """Procesa un archivo JSON corrigiendo caracteres Unicode."""
    try:
        # Leer el archivo
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Aplicar correcciones
        fixed_content = fix_unicode_codepoints(content)
        
        if fixed_content == original_content:
            return 'unchanged'
        
        # Verificar que sea JSON válido
        try:
            json.loads(fixed_content)
        except json.JSONDecodeError as e:
            print(f"❌ Error de JSON en {file_path.name}: {e}")
            return 'error'
        
        # Guardar
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"✅ {file_path.relative_to(file_path.parents[3])}")
        return 'fixed'
        
    except Exception as e:
        print(f"❌ Error en {file_path.name}: {e}")
        return 'error'

def main():
    """Procesa todos los archivos JSON de Programación I."""
    base_path = Path(__file__).parent / 'backend' / 'problems' / 'Programacion I'
    
    if not base_path.exists():
        print(f"❌ No se encontró: {base_path}")
        return
    
    print("🔍 Corrigiendo encoding en archivos de Programación I...\n")
    
    # Buscar archivos
    hints_files = list(base_path.glob('**/hints.json'))
    metadata_files = list(base_path.glob('**/metadata.json'))
    all_files = sorted(hints_files + metadata_files)
    
    fixed = 0
    unchanged = 0
    errors = 0
    
    for file_path in all_files:
        result = process_json_file(file_path)
        if result == 'fixed':
            fixed += 1
        elif result == 'unchanged':
            unchanged += 1
        else:
            errors += 1
    
    print(f"\n📊 Resumen:")
    print(f"   ✅ Corregidos: {fixed}")
    print(f"   ⚪ Sin cambios: {unchanged}")
    print(f"   ❌ Errores: {errors}")
    print(f"   📁 Total: {len(all_files)}")

if __name__ == '__main__':
    main()
