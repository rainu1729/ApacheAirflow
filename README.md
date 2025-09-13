# Apache Airflow

Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows. It allows you to orchestrate complex data pipelines using Python code.

This project uses [uv](https://github.com/astral-sh/uv) for fast Python package management.

Sample example DAGs are included in the `dags` folder to help you get started.

## Getting Started with Docker Compose

First, download the official `docker-compose.yaml` file from the Apache Airflow website:

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.2/docker-compose.yaml'
```

Before starting Apache Airflow, create a `.env` file in the project root and set `AIRFLOW_UID` to your current user ID. You can do this by running:

```bash
echo "AIRFLOW_UID=$(id -u)" > .env
```

To start Apache Airflow using Docker Compose in the background, run:

```bash
docker compose up -d
```

To stop and remove the containers, run:

```bash
docker compose down
```

## Accessing the Airflow UI

Once running, you can access the Airflow web UI at: [http://localhost:8080](http://localhost:8080)