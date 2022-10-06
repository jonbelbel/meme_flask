FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install flask

RUN pip install requests

ENTRYPOINT ["python"]

CMD ["meme_flask.py"]