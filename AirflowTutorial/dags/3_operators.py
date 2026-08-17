from airflow.sdk import dag, task 
from airflow.operators.bash import BashOperator

@dag(
        dag_id = "operators_dag"

)
def operators_dag():

    @task.python
    def first_task():
        print("This is first task")

    @task.python
    def second_task():
        print("This is second task")
    
    @task.bash
    def bash_task_modern():
        return "echo https://airflow.apache.org/"
    
    bash_task_oldSchool = BashOperator(
    task_id = "run_after_loop",
    bash_command = "echo https://airflow.apache.org/",
    )
    

    # Defining task dependencies
    first = first_task()
    second = second_task()
    bash_command = bash_task_modern()
    bash_oldschool = bash_task_oldSchool

    first >> second >> bash_command >> bash_oldschool

# Instantiating the DAG
operators_dag()