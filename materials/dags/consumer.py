from airflow import Dataset
from airflow.decorators import dag, task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")


@dag(
    dag_id="consumer",
    schedule=[my_file],
    start_date=datetime(2024, 1, 1),
    catchup=False
)
@task
def read_dataset():
    with open(my_file.uri, "r") as f:
        print(f.read())


read_dataset()