FROM python:3.9


WORKDIR /app


# EXPOSE 8000

COPY . /app


RUN pip install -r requirements.txt


CMD ["python", "drfmarket/manage.py", "runserver",]  