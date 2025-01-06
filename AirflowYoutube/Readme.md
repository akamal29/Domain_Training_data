# Simple Airflow Project

This project demonstrates a basic Apache Airflow DAG that executes a simple Python task. 

## Project Overview

* **Purpose:** This DAG showcases a fundamental Airflow workflow with a single Python task.
* **Functionality:** 
    - The DAG is scheduled to run daily.
    - A Python function (`print_hello`) is defined within the DAG.
    - The `PythonOperator` executes the `print_hello` function, which prints "Hello, Airflow!" to the logs.

## Setup and Requirements

1. **Install Python and Dependencies:**
   - Ensure you have Python 3.x installed.
   - Create a virtual environment (recommended):
     ```bash
     python3 -m venv my_airflow_env
     source my_airflow_env/bin/activate 
     ```
   - Install Apache Airflow:
     ```bash
     pip install apache-airflow
     ```

2. **Initialize Airflow:**
   - Initialize the database:
     ```bash
     airflow db init
     ```

3. **Set Environment Variable (optional):**
   - If you want to customize the Airflow home directory:
     ```bash
     export AIRFLOW_HOME=~/airflow 
     ```

4. **Create DAGs Directory:**
   - Create a directory to store your DAG files:
     ```bash
     mkdir -p ~/airflow/dags
     ```

5. **Start Airflow Services:**
   - Start the scheduler:
     ```bash
     airflow scheduler
     ```
   - Start the webserver:
     ```bash
     airflow webserver -p 8080 
     ```

## Running the DAG

1. **Access Airflow Web UI:**
   - Open your web browser and navigate to: `http://localhost:8080`

2. **Trigger the DAG:**
   - Locate your DAG (e.g., `simple_hello_airflow`) in the Airflow UI.
   - Click "Trigger DAG" to initiate an immediate run.

3. **Monitor Execution:**
   - Observe the DAG's progress and task statuses in the Airflow UI.
   - View task logs for details about the execution.

## Verification

- Check the task logs in the Airflow UI for the output: "Hello, Airflow!"

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Commit and push your changes to your branch.
