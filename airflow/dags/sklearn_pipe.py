from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
import datetime as dt


init_path = "/home/zalina/xflow/data/raw/iris__{{ ds }}.csv"
path_train_data = "/home/zalina/xflow/data/processed/train_data__{{ ds }}.csv"
path_train_labels = "/home/zalina/xflow/data/processed/train_labels__{{ ds }}.csv"
path_test_data = "/home/zalina/xflow/data/processed/test_data__{{ ds }}.csv"
path_test_labels = "/home/zalina/xflow/data/processed/test_labels__{{ ds }}.csv"


args = {
    "owner": "admin",
    "start_date": dt.datetime(2023, 12, 1),
    "retries": 3,
    "retry_delays": dt.timedelta(minutes=1),
    "depends_on_past": False
}



with DAG(
    dag_id='sklearn_comments',
    default_args=args,
    schedule_interval=None,
    tags=['youtube', 'score'],
) as dag:
    get_data = BashOperator(task_id='get_data',
                            bash_command=f"python3 /home/zalina/xflow/scripts2/load_data.py --output_path {init_path}",
                            dag=dag)
    split_data = BashOperator(task_id='split_data',
                            bash_command=f"python3 /home/zalina/xflow/scripts2/split_data.py --input_path {init_path} --output_path_train_data {path_train_data} --output_path_train_labels {path_train_labels} --output_path_test_data {path_test_data} --output_path_test_labels {path_test_labels}",
                            dag=dag)
    # train_test_split_data = BashOperator(task_id='train_test_split_data',
    #                         bash_command="python3 /home/zalina/xflow/scripts/train_test_split.py",
    #                         dag=dag)
    # train_model = BashOperator(task_id='train_model',
    #                         bash_command="python3 /home/zalina/xflow/scripts/train_model.py",
    #                         dag=dag)
    # test_model = BashOperator(task_id='test_model',
    #                         bash_command="python3 /home/zalina/xflow/scripts/test_model.py",
    #                         dag=dag)
    get_data >> split_data

