# Objective: Build a runtime image for the support agent API.
# Why it exists: Deployment needs reproducible packaging.
# How to use: docker build -f infra/Dockerfile -t support-agent:local .
# Dependencies: pyproject.toml, src/support_agent/api.py.
# Owner: Builder.
# Update policy: Update when runtime dependencies or serving command changes.
# Examples: docker run -p 8000:8000 support-agent:local.
# Related files: infra/docker-compose.yml, .env.example.
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir -e .[api]
EXPOSE 8000
CMD ["uvicorn", "support_agent.api:app", "--host", "0.0.0.0", "--port", "8000"]
