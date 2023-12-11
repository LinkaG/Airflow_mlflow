 
# Airflow & Mlflow Example Pipeline for Machine Learning (Local Development)

В этом репозитории показан пример Apache Airflow pipeline для локальной разработки проектов.

В качестве примера реализованы 2 пайплана:
1. [youtube_comments_score.py](airflow%2Fdags%2Fyoutube_comments_score.py) - получение информации о рейтинге канала по количеству лайков
2. [youtube_comments_score.py](airflow%2Fdags%2Fyoutube_comments_score.py) - классический пример классификации на датасете iris (+ click, + hydra)

## Usage
Для того, чтобы воспроизвести папйплайн, выполняются следующие шаги:

1. Создание виртуального окружение

   ```
   python3 -m venv env
   ```

2. Установка и настройка airflow

   ```
   pip3 install "apache-airflow[celery]==2.7.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.3/constraints-3.8.txt"
   export AIRFLOW_HOME=/home/your_user/xflow/airflow
   airflow db init
   ```

3. Установка и запуск mlflow

   ```
   pip3 install mlflow
   mlflow ui
   ```

4. Запуск Airflow webserver и sheduler :

    ```
    airflow webserver -p 8080
    ```
   
   ```
    airflow scheduler
   ```

5. Доступ к Airflow web interface в браузере по адресу: http://localhost:8080.

6. Триггерим нужный пайплайн в web-интерфейсе.

7. Результаты запуска пайплайна:

   ![image](images/airflow2.png)

8. Отслеживание экспериментов в mlflow (залогированы датасет, модель, метрики)
   ![image](images/mlflow2.png)


