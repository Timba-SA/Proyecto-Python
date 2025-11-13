# 📦 Legacy Files - Código Histórico

Estos archivos representan la arquitectura monolítica original del MVP antes de la refactorización a microservicios (Octubre 2025).

## ⚠️ NO USAR ESTOS ARCHIVOS EN PRODUCCIÓN

Este directorio contiene código histórico preservado únicamente como referencia educativa y para entender la evolución del proyecto.

## 📄 Archivos

### `app.py` (anteriormente `app.py.legacy`)
Aplicación monolítica FastAPI original. Ha sido reemplazada por:
- `backend/app.py` - API REST FastAPI
- `worker/tasks.py` - Worker RQ para procesamiento de jobs
- `backend/services/` - Arquitectura de capa de servicios

### `runner.py`
Lógica original de ejecución Docker (130 líneas). Ahora reemplazada por:
- `worker/services/docker_runner.py` - Ejecución Docker moderna con traducción de paths
- `worker/tasks.py` - Orquestación de jobs

### `Dockerfile.monolithic` (anteriormente `Dockerfile`)
Dockerfile original de contenedor único. Ahora reemplazado por:
- `backend/Dockerfile` - Contenedor del servicio backend
- `worker/Dockerfile` - Contenedor del servicio worker
- `frontend/Dockerfile` - Contenedor del servicio frontend
- `runner/Dockerfile` - Contenedor sandbox minimalista

### `requirements.txt`
Dependencias monolíticas originales. Ahora reemplazadas por:
- `backend/requirements.txt` - Dependencias del backend
- `worker/requirements.txt` - Dependencias del worker
- Cada servicio tiene sus propias dependencias aisladas

## 📅 Historial de Migración

**25 de Octubre, 2025**: Refactorización a microservicios completada
- Separación de responsabilidades en servicios backend, worker, frontend
- Implementación de arquitectura de capa de servicios
- Agregado de logging estructurado y validación
- Migración a schemas Pydantic v2

**10 de Noviembre, 2025**: Archivos legacy movidos a este directorio
- Limpieza de estructura del directorio raíz
- Mejora de claridad arquitectónica

**13 de Noviembre, 2025**: Documentación actualizada
- READMEs actualizados en todo el proyecto
- Estructura de paquetes Python completada con `__init__.py`
- Tests corregidos y optimizados

## 📖 Referencias

- Ver `LEGACY_FILES.md` en el directorio raíz para notas detalladas de migración
- Ver `CLAUDE.md` para la documentación completa del proyecto actual
- Ver `README.md` principal para instrucciones de uso

## 💡 Lecciones Aprendidas

La migración de monolito a microservicios proporcionó:
- ✅ Mejor separación de responsabilidades
- ✅ Escalabilidad independiente de servicios
- ✅ Testing más granular y mantenible
- ✅ Deployment más flexible
- ✅ Código más limpio y organizado

## 🎓 Valor Educativo

Estos archivos son útiles para:
- Entender decisiones de arquitectura
- Comparar patrones monolíticos vs microservicios
- Aprender sobre refactorización a gran escala
- Estudiar evolución de código en proyectos reales

---

**Última actualización**: Noviembre 13, 2025
