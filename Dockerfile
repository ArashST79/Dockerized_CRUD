FROM python:3

RUN mkdir -p /opt/services/crudapp/src
COPY ./requirements.txt /opt/services/crudapp/src/
WORKDIR /opt/services/crudapp/src
RUN pip install -r requirements.txt
ADD . /opt/services/crudapp/src
EXPOSE 5080
CMD ["python", "app.py"]

