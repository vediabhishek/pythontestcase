FROM python:3.6



COPY . /app

WORKDIR /app

EXPOSE 5000

RUN pip install -r requirement.txt

ENTRYPOINT ["python", "hello-world.py"]
