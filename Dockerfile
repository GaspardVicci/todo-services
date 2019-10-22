FROM python:3.6

RUN apt-get update

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

ENV FLASK_APP "/app/run.py"
ENTRYPOINT ["/app/migrate.sh"]
CMD ["/app/run.py"]

