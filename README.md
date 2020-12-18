# Airflow 2.0 Demo Sandbox

## Using this repo
To start, ensure you have `docker` and `docker-compose` installed.
Once you have them installed, run the following command to persist the `postgres` data in this volume:

### Create a Docker volume for the database
```bash
docker volume create --name airflow-pg
```

### Initialize Database Backend & Create User
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

### Starting the Webserver + Scheduler
Run the following command to start the webserver + scheduler:
```bash
docker-compose up webserver scheduler
```
