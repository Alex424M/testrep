FROM python:3
WORKDIR /app
COPY calc.py /app/calc.py
CMD ["python", "/app/calc.py"]
