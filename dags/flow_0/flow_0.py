from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.subdag_operator import SubDagOperator
from flow_0.subflow_0 import *
from flow_0.scripts.script_0 import *
from datetime import datetime

DAG_name = 'flow_0'
args = {
	'start_date' : datetime(2020, 1, 1), 
	'catchup' : False
}
with DAG(
	DAG_name,	
	description=DAG_name, 
	default_args=args,	
	schedule_interval='0 0 1 1 *') as dag:

	dummy_task 	= DummyOperator(task_id='dummy_task', retries=3)

	python_task	= PythonOperator(task_id='python_task', python_callable=my_func)
	
	a = DummyOperator(task_id='a', retries=3)
	
	b1 = DummyOperator(task_id='b1', retries=3)
	b2 = DummyOperator(task_id='b2', retries=3)
	
	
	c = DummyOperator(task_id='c', retries=3)
	
	SubDAG_name = 'subflow_0'
	d = SubDagOperator(task_id=SubDAG_name, subdag=subflow_0(DAG_name, SubDAG_name, args), dag=dag)	

	dummy_task >> python_task >> a >> [b1, b2] >> c >> d