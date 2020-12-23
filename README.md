# Airflow 2.0 Sandbox
Sandbox for getting started with Airflow 2.0
## Using this repo
To start, ensure you have `docker` and `docker-compose` installed.
Once you have them installed, run the following command to persist the `postgres` data in this volume:


## Environment Variables
Create the following files in the root directory of the repository:
- `.pg.env`
- `.env`

The `.pg.env` contains the `postgres` environment variables for the root user
of the database. In this case, you can use:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=airflow
POSTGRES_PORT=5432
```

Next, the `.env` file contains Airflow environment variables, and the only one required to get started is as follows:

```
AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://postgres:postgres@postgres:5432/airflow
```

The `postgres` credentials need to match this values connection string in the form of
```
AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{SERVICE_NAME}:{POSTGRES_PORT}/{POSTGRES_DB}
```

Note that the `SERVICE_NAME` in this example uses `postgres` as that is the service name defined in the `docker-compose.yaml`.

## Create a Docker volume for the database
```bash
docker volume create --name airflow-pg
```

## Initialize Database Backend & Create User
After creating the `airflow-pg` Docker volume to persist the database, you'll need to create a user
to log into the Airflow UI.

While running the `postgres` database in a seperate terminal:
```bash
docker-compose up postgres
```

You can run the following command to initialize the database and create a user.
Make sure to replace the command line flags in the `create_admin` service with
the values you would use for your user.

```bash
docker-compose up initdb create_admin
```
Once these tasks are completed the containers will exit with code 0, and you can
exit the process, and start the webserver and scheduler.

## Starting the Webserver + Scheduler
Run the following command to start the webserver + scheduler:
```bash
docker-compose up webserver scheduler
```
