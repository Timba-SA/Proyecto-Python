# Minimal Python image for sandboxed test execution
FROM python:3.11-slim

# Install only pytest (minimal dependencies)
RUN pip install --no-cache-dir pytest==8.3.3

# Create workspace directory
RUN mkdir /workspace
WORKDIR /workspace

# Copy project code first (as root, before switching user)
COPY . /workspace

# Install dependencies from requirements.txt (as root, with full permissions)
RUN pip install -r requirements.txt

# Non-root user for security
RUN useradd -m -u 1000 sandbox && chown -R sandbox:sandbox /workspace
USER sandbox

# Default command (will be overridden)
CMD ["pytest"]
