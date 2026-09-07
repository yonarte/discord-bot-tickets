FROM python:3.11-alpine
ENV POETRY_VIRTUALENVS_CREATE=false
RUN pip install poetry==2.4.3
WORKDIR /discord-bot-tickets
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --only main
COPY . .
CMD ["python", "src/main.py"]