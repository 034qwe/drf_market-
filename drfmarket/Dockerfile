FROM python:3.9

ENV PYTHONDONTWRITENBYTECODE=1
ENV PYTHONUNBUFFRED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .


# CMD ["python", "drfmarket/manage.py", "runserver",]  