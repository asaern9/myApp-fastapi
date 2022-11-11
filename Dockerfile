FROM python:3.9

# Create work directory
WORKDIR ./

#Install poetry env, project dependency and model files
COPY poetry.lock pyproject.toml ./
RUN pip install --no-cache-dir poetry==1.2.0 && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy application files
COPY ./ ./

# Expose port and run application
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

