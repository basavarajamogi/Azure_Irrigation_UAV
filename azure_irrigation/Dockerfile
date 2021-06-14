FROM python:3.8.2

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install Werkzeug

EXPOSE 8080
CMD ["python", "/waitress_server.py"]