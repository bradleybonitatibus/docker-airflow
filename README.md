# Personal Airflow Deployment
Bradley Bonitatibus

## Using this repo
To start, ensure you have `docker` and `docker-compose` installed.
Once you have them installed, run the following command to persist the `postgres` data in this volume:

```bash
docker volume create --name airflow-pg
```

Next, you can spin up the deployment with:
```bash
docker-compose up --build
```

For more information on extending this, please visit the `puckle/docker-airflow` repo at <a href="https://github.com/puckel/docker-airflow">https://github.com/puckel/docker-airflow</a>