FROM python:3.11-alpine
WORKDIR /discord-bot-ticket
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "src/__main__.py"]