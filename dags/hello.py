import json

from airflow.decorators import dag, task # noqa
from airflow.utils.dates import days_ago # noqa


default_args = {
    'owner': 'brad'
}


@dag(default_args=default_args, schedule_interval=None, start_date=days_ago(2))  # noqa
def my_first_airflow_2_pipeline():
    @task()
    def extract():
        """Pull some data and return it as dictionary
        """
        some_kv_data = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        data_dict = json.loads(some_kv_data)
        return data_dict

    @task(multiple_outputs=True)
    def transform(data_dict: dict):
        """Aggregate and transform dictionary data and return it
        """
        total = 0
        for v in data_dict.values():
            total += v

        return {'total_sales': total}

    @task()
    def load(total_order: float):
        """Load / log summarized data
        """
        print(f'Total sales is: {total_order}')

    data = extract()
    summary = transform(data)
    load(summary['total_sales'])


d = my_first_airflow_2_pipeline()
