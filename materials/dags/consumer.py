from airflow import Dataset
from airflow.decorators import dag, task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")


@dag(
    dag_id="consumer",
    schedule=[my_file, my_file_2],
    start_date=datetime(2024, 1, 1),
    catchup=False
)
@task
def read_dataset():
    with open(my_file.uri, "r") as f:
        print(f.read())


@task
def read_dataset_2():
    with open(my_file_2.uri, "r") as f:
        print(f.read())


read_dataset()
read_dataset_2()
