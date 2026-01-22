FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install tabulate
CMD ["python", "main.py"]
