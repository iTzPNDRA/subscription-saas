FROM python:3.12-slim
ENV POETRY_VERSION=1.8.2
RUN pip install --no-cache-dir poetry==$POETRY_VERSION
WORKDIR /app
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root --only main
COPY app /app/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
