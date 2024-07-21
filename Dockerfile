FROM python:3.12
WORKDIR /
COPY . .
RUN pip install -r requirements.txt
RUN set -e
RUN export FLASK_APP=core/server.py
ENV FLASK_APP=core/server.py
RUN flask db upgrade -d core/migrations/

EXPOSE 7755

CMD ["gunicorn","-c","gunicorn_config.py","core.server:app"]