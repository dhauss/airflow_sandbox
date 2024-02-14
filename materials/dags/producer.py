from airflow import Dataset
from airflow.decorators import dag, task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")


@dag(
    dag_id="producer",
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False
)
@task(outlets=[my_file, my_file_2])
def update_dataset():
    with open(my_file.uri, "a+") as f:
        f.write("producer update 1")

    with open(my_file_2.uri, "a+") as f:
        f.write("producer update 2")


update_dataset()
