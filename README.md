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

then we should build up the docker with these three other lines:


```
docker-compose up -d db
```

```
docker-compose run --rm flaskapp /bin/bash -c "cd /opt/services/flaskapp/src && python -c  'import database; database.init_db()'"
```

now we have three docker images, but one docker container 
![Screenshot (701)](https://github.com/ArashST79/Dockerized_CRUD/assets/31709401/10dc8052-5933-462e-b6d3-d00453c533c3)

```
docker-compose up
```

now we have three containers running on the system. (cannot show it here because after running this code I don't have access to terminal
![Screenshot (709)](https://github.com/ArashST79/Dockerized_CRUD/assets/31709401/458af95f-ee3c-4ab2-8f81-131b7341dbcd)


after that 8080 port should be opened. (nothing is defined in this url)
![Screenshot (702)](https://github.com/ArashST79/Dockerized_CRUD/assets/31709401/b5340372-370a-435a-8140-6b6d56d9de62)

# testing with postman

now we test each method with postman :

## creating a user
![Screenshot (703)](https://github.com/ArashST79/Dockerized_CRUD/assets/31709401/f93a8540-fb7a-4343-9139-ef05cab10cbd)

## getting a correct user with ID 1
![Screenshot (704)](https://github.com/ArashST79/Dockerized_CRUD/assets/31709401/1ff7ad77-2edd-487f-9a57-2932fbc0dcff)

## getting a wrong user with ID 10
![Screenshot (705)](https://github.com/ArashST79/Dockerized_CRUD/assets/31709401/881ed0f2-919a-454a-a088-f97914993d42)

## updating a user with ID 1
![Screenshot (706)](https://github.com/ArashST79/Dockerized_CRUD/assets/31709401/f7d04adb-8c04-4074-a7d2-54c6b63c1cac)

# deleting user with ID 1
![Screenshot (707)](https://github.com/ArashST79/Dockerized_CRUD/assets/31709401/d355495c-e81f-4316-b995-af5fcd91e00b)

# getting a user with ID 1 which is deleted 
![Screenshot (708)](https://github.com/ArashST79/Dockerized_CRUD/assets/31709401/c29ef0aa-a8cf-403f-8392-7c9808a83272)


