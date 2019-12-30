FROM python:3.7-alpine

RUN pip install Flask flask_cors

COPY app.py /app.py

COPY data.json /data.json

RUN chmod a+x /app.py

EXPOSE 5000

CMD [ "python", "/app.py" ]