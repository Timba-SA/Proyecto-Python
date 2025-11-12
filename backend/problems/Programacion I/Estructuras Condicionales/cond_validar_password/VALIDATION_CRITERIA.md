# Criterios de Validación - cond_validar_password

## Decisión de Diseño (11 Nov 2025)

### Criterio Actual
**Solo se valida LONGITUD**: Una contraseña es válida si tiene entre 8 y 14 caracteres (inclusive).

### ¿Qué se permite?
✅ **Espacios**: SÍ - "pass word" (9 chars) es válido
✅ **Caracteres especiales**: SÍ - "pass!123" (8 chars) es válido  
✅ **Solo números**: SÍ - "12345678" (8 chars) es válido
✅ **Solo letras**: SÍ - "password" (8 chars) es válido
✅ **Mezclados**: SÍ - "MiClave#2024" (12 chars) es válido

### Razonamiento Pedagógico
Este es un ejercicio de **Estructuras Condicionales básicas** enfocado en:
- Leer entrada con `input()`
- Usar función `len()` para obtener longitud
- Aplicar condicionales `if/else` con rangos numéricos
- Comparar valores: `8 <= len(password) <= 14`

**NO** está diseñado para enseñar:
- Expresiones regulares (regex)
- Validación compleja de patrones
- Seguridad de contraseñas real

### Tests de Casos Borde Agregados
1. **Espacios internos**: `"pass word"` (9 chars) → VÁLIDO
2. **Caracteres especiales**: `"pass!@#$"` (9 chars) → VÁLIDO  
3. **Solo espacios**: `"        "` (8 chars) → VÁLIDO (técnicamente cumple longitud)
4. **Espacios + caracteres**: `"abc 1234"` (8 chars) → VÁLIDO

### Evolución Futura (Opcional)
Si en el futuro se quiere enseñar validación avanzada, se podría crear un problema separado:
- **cond_validar_password_segura**: Requiere mayúsculas, números, caracteres especiales
- **cond_validar_password_sin_espacios**: Rechaza espacios
- Usar estos como ejercicios de nivel intermedio/avanzado

### Referencias
- Enunciado: `prompt.md` (líneas 14-15)
- Tests públicos: `tests_public.py`
- Tests ocultos: `tests_hidden.py`
