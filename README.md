# Intro to Project
In this experiment, we are creating a simple CRUD service using the Flask framework, PostgreSQL database, and Nginx for load balancing. The target project is a name retrieval app that includes a database with a table having two columns: id and user_name.

# Docker File
this is a docker file for the flaskapp with python. It's the main code for handling the requests
```
FROM python:3

RUN mkdir -p /opt/services/flaskapp/src
COPY ./requirements.txt /opt/services/flaskapp/src/
WORKDIR /opt/services/flaskapp/src
RUN pip install -r requirements.txt
ADD . /opt/services/flaskapp/src
EXPOSE 5090
CMD ["python", "app.py"]
```

# Docker-Compose
This is Docker compose file. we have three dockers here. db as postgres database image, crud app which we build it's image with the previous docker file, and also nginx docker as nginx pre-build image for load balancing
```
version: '3'
services:
  db:
    image: "postgres:9.6.5"
    volumes:
      - "dbdata:/var/lib/postgresql/data"
    env_file:
      - env_file
    networks:
      - db_nw
  crudapp:
    build: .
    env_file:
      - env_file
    volumes:
      - .:/opt/services/flaskapp/src
    networks:
      - db_nw
      - web_nw
    depends_on:
      - db
  nginx:
    image: "nginx:1.13.5"
    ports:
      - "8080:80"
    volumes:
      - ./conf.d:/etc/nginx/conf.d
    networks:
      - web_nw
    depends_on: 
      - flaskapp
networks:
  db_nw:
    driver: bridge
  web_nw:
    driver: bridge
volumes:
  dbdata:
```
# docker tool
we use labs.play-with-docker.com as docker. our project our uploaded here

# building up docker process

first we should clone our project here

```
git clone https://github.com/ArashST79/Dockerized_CRUD.git
```

changing directory

```
cd Dockerized_CRUD
```

then we should build up the docker with these three lines
```
docker-compose up -d db
docker-compose run --rm flaskapp /bin/bash -c "cd /opt/services/flaskapp/src && python -c  'import database; database.init_db()'"
docker-compose up
```

now we have three containers running on the system
