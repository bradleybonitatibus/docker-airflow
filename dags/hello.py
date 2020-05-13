import airflow
from airflow.models import DAG
from datetime import timedelta, datetime
from airflow.operators.python_operator import PythonOperator

args = {
    "owner": "Bradley Bonitatibus",
    "start_date": "2019-12-21",
}

def hello(**kwargs):
    print("Hello there")
    return

with DAG(
  default_args=args,
  schedule_interval="@hourly",
  dag_id="hello_airflow",
) as dag:

  task = PythonOperator(
    task_id="first",
    python_callable=hello,
    provide_context=True
  )

for i in range(40):
    next_task = PythonOperator(
      task_id="task_{0}".format(i),
      python_callable=hello,
      provide_context=True,
      op_kwargs={
          "num": i
      }
    )
    task >> next_task