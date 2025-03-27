FROM python:latest

COPY sum.py /app/sum.py

ENTRYPOINT [ "python", "/app/sum.py" ]