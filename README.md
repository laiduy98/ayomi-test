# Technical Test AYOMI
--------------------

## How to start

It is necessary to create a ```.env``` file at first. Normally, the ```.env``` file will be **ignored** but for the demo purpose, this repo already has it. However, you can choose the environment variables as you like.

```
DB_USER=fastapi_user
DB_PASSWORD=fastapi_password
DB_NAME=fastapi_db
```

### With docker

```sh
docker-compose up --build
```

You can stop the service by this command.

```sh
docker-compose down
```

### With a conda env for testing purpose

```sh
conda create -n ayomi
conda activate ayomi
conda install fastapi uvicorn sqlalchemy httpx psycopg2-binary

```



## File description

- ```database.py```: 

Defines a database service as in the documentation of FastAPI.

- ```main.py```:


- ```npi.py```:

Contains the NPI calculator. It could be run directly to test the function.


- ```schemas.py```:

To validate results we receive as well as to reformat the data that we want to send to the browser.

- ```docker-compose.yml```:

Contains 2 services and 1 volume. the first is the FastAPI app and the second is a Postgres database. The data of the db is mounted to a volume to maintain the data if we want to restart the service or turn it off.

## API description

Fortunately, FastAPI is built-in with a document generator. You can find the documents for the APIs at ```/docs``` after you start the server.

The csv is created as a downloadable file instead of store on the server's disk so that the web browser client can download it.

## Unit test

FastAPI also come with a built-in TestClient. HTTPX is required to use it. To run the test file:

```sh
python test.py
```