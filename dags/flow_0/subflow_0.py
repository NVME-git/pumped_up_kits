from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator


def subflow_0(parent_dag_name, child_dag_name, args):
    dag_subdag = DAG(
        dag_id='%s.%s' % (parent_dag_name, child_dag_name),
        default_args=args,
        schedule_interval="@daily",
    )

    last_task = None

    for i in range(5):
        task = DummyOperator(
            task_id=f'{child_dag_name}-task-{i}',
            default_args=args,
            dag=dag_subdag,
        )

        if last_task:
            last_task >> task

        last_task = task

    return dag_subdag