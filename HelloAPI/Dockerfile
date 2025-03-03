 FROM python:3.9.21-slim
 ENV PYTHONUNBUFFERED 1
 WORKDIR /code
 COPY ./requirements.txt /code/requirements.txt
 RUN pip install pytest-runner
 RUN pip install -r requirements.txt
 COPY . /code/
 CMD ["python3", "main.py"]
 EXPOSE 8000
 HEALTHCHECK NONE