# 🐳 Runner Image

Imagen Docker minimalista utilizada para la ejecución aislada y segura del código de los estudiantes.

## 🎯 Propósito

Esta imagen proporciona un entorno de ejecución sandboxed para:
- Ejecutar código Python de estudiantes de forma segura
- Correr tests pytest sin riesgos de seguridad
- Aislar completamente la ejecución del sistema host
- Garantizar consistencia en las evaluaciones

## ✨ Características

- 🐍 **Python 3.11** base minimalista
- 🧪 **pytest** incluido para ejecución de tests
- 👤 **Usuario no-root** (uid: 1000, nombre: sandbox)
- 🚫 **Sin paquetes adicionales** (máxima seguridad)
- 🔒 **Sin acceso a red** durante ejecución
- 📦 **Imagen ligera** optimizada para rapidez

## 🏗️ Construcción

```bash
# Desde el directorio raíz del proyecto
docker build -t py-playground-runner:latest ./runner

# Verificar la imagen
docker images | grep py-playground-runner
```

## 🔒 Medidas de Seguridad

Cuando el worker ejecuta contenedores, aplica las siguientes restricciones:

### Aislamiento de Red
```bash
--network none  # Sin acceso a Internet ni red interna
```

### Sistema de Archivos
```bash
--read-only                                      # Filesystem read-only
--tmpfs /tmp:rw,noexec,nosuid,size=64m          # Temp limitado sin ejecución
--tmpfs /workspace:rw,noexec,nosuid,size=128m   # Workspace limitado
```

### Límites de Recursos
```bash
--cpus=1.0          # Máximo 1 CPU core
--memory=256m       # Máximo 256MB RAM
--memory-swap=256m  # Sin swap adicional
```

### Timeout y Limpieza
- ⏱️ Timeout de 3-5 segundos por ejecución
- 🧹 Limpieza automática de contenedores
- 🗑️ Eliminación de workspaces temporales

## 📝 Uso por el Worker

El worker (`worker/services/docker_runner.py`) utiliza esta imagen así:

```python
container = client.containers.run(
    image='py-playground-runner:latest',
    command=['python', '-m', 'pytest', ...],
    volumes={workspace_path: {'bind': '/workspace', 'mode': 'ro'}},
    working_dir='/workspace',
    user='1000:1000',
    network_mode='none',
    read_only=True,
    tmpfs={
        '/tmp': 'rw,noexec,nosuid,size=64m',
        '/workspace': 'rw,noexec,nosuid,size=128m'
    },
    mem_limit='256m',
    memswap_limit='256m',
    cpu_quota=100000,
    remove=True,
    detach=False
)
```

## 🧪 Testing Local

Para probar la imagen localmente:

```bash
# Crear un archivo de test simple
echo 'def test_suma(): assert 1 + 1 == 2' > test_simple.py

# Ejecutar en el contenedor (Linux/Mac)
docker run --rm \
  -v $(pwd):/workspace:ro \
  -w /workspace \
  --network none \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=64m \
  py-playground-runner:latest \
  python -m pytest test_simple.py -v

# Windows PowerShell
docker run --rm `
  -v ${PWD}:/workspace:ro `
  -w /workspace `
  --network none `
  --read-only `
  --tmpfs /tmp:rw,noexec,nosuid,size=64m `
  py-playground-runner:latest `
  python -m pytest test_simple.py -v
```

## 📊 Especificaciones Técnicas

| Aspecto | Detalle |
|---------|---------|
| **Imagen Base** | python:3.11-slim |
| **Tamaño** | ~150MB |
| **Python** | 3.11.x |
| **pytest** | Latest stable |
| **Usuario** | sandbox (uid 1000) |
| **Shell** | /bin/bash |
| **Working Dir** | /workspace |

## 🔄 Actualización

Si modificas el Dockerfile:

```bash
# Reconstruir la imagen
docker build -t py-playground-runner:latest ./runner

# Reiniciar el worker para usar la nueva imagen
docker compose restart worker
```

## 🐛 Troubleshooting

**Error: "Image not found"**
```bash
# Verificar que la imagen existe
docker images py-playground-runner

# Si no existe, construirla
cd runner && docker build -t py-playground-runner:latest .
```

**Error: "Permission denied"**
```bash
# Linux/Mac: Agregar usuario al grupo docker
sudo usermod -aG docker $USER
newgrp docker
```

**Tests fallan en el contenedor pero funcionan localmente**
- Verificar que todos los archivos necesarios están en el workspace
- Revisar permisos de archivos (deben ser legibles por uid 1000)
- Comprobar que no hay dependencias de red o sistema

## 📚 Referencias

- [Docker SDK for Python](https://docker-py.readthedocs.io/)
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [pytest Documentation](https://docs.pytest.org/)

---

**Última actualización**: Noviembre 13, 2025
