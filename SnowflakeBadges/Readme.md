 Data Pipeline Project: API and CSV Data Integration with Azure SQL, ADLS, and Snowflake

This project implements a robust data pipeline that integrates data from two sources (JSON API and CSV), processes the data in Azure SQL (Silver and Gold layers), stores files in Azure Data Lake Storage (ADLS), and refreshes Snowflake external tables. The pipeline uses Azure Data Factory (ADF) for orchestration.

---

## **Data Sources**
1. **JSON API**  
   - **URL**: [https://dummyapi.online/api/users](https://dummyapi.online/api/users)  
   - **Data Type**: JSON  

2. **CSV**  
   - **URL**: [https://github.com/Kamalesh-Radhakrishnan/adf_data/blob/main/customers.csv](https://github.com/Kamalesh-Radhakrishnan/adf_data/blob/main/customers.csv)  
   - **Data Type**: CSV  

---

## **Data Storage Locations**
1. **Azure SQL Database**  
   - **Silver Layer**: For raw data storage after initial ingestion.  
   - **Gold Layer**: For processed data with history tracking (SCD-II).

2. **Snowflake External Table**  
   - Points to ADLS folder for external data access.

---

## **Database Tables**

### **Azure SQL Silver Layer**  
Stores raw data after ingestion.  
| Column      | Data Type      | Description               |
|-------------|----------------|---------------------------|
| id          | INT (PK)       | Unique identifier         |
| name        | VARCHAR(255)   | Name of the user          |
| username    | VARCHAR(255)   | Username of the user      |
| email       | VARCHAR(255)   | Email address             |
| street      | VARCHAR(255)   | Street name               |
| city        | VARCHAR(255)   | City name                 |
| state       | VARCHAR(255)   | State name                |
| zipcode     | VARCHAR(20)    | Zip code                  |

### **Azure SQL Gold Layer**  
Stores transformed data with history tracking (SCD-II).  
| Column             | Data Type      | Description                            |
|---------------------|----------------|----------------------------------------|
| id                 | INT (PK)       | Unique identifier                      |
| name               | VARCHAR(255)   | Name of the user                       |
| username           | VARCHAR(255)   | Username of the user                   |
| email              | VARCHAR(255)   | Email address                          |
| address            | VARCHAR(1024)  | Concatenation of street, city, state   |
| zipcode            | VARCHAR(20)    | Zip code                               |
| created_timestamp  | DATETIME       | Record creation timestamp              |
| update_timestamp   | DATETIME       | Record update timestamp                |
| is_active          | BIT            | Indicates if the record is active      |

### **Snowflake External Table**  
Points to ADLS folder for raw data access.  
| Column      | Data Type      | Description               |
|-------------|----------------|---------------------------|
| id          | INT (PK)       | Unique identifier         |
| name        | VARCHAR(255)   | Name of the user          |
| username    | VARCHAR(255)   | Username of the user      |
| email       | VARCHAR(255)   | Email address             |
| street      | VARCHAR(255)   | Street name               |
| city        | VARCHAR(255)   | City name                 |
| state       | VARCHAR(255)   | State name                |
| zipcode     | VARCHAR(20)    | Zip code                  |

---

## **Data Pipeline Flow**

1. **Ingest JSON API Data**
   - Use a Copy Activity in ADF to pull data from [JSON API](https://dummyapi.online/api/users).
   - Flatten the JSON structure and load it into the **Silver Layer (Azure SQL)**.

2. **Transform Data to Gold Layer**
   - Load data from the **Silver Layer** into the **Gold Layer (Azure SQL)**.
   - Perform SCD-II (Slowly Changing Dimension Type-II) transformations to maintain historical data.

3. **Export Data to ADLS**
   - Save raw data from the **Silver Layer** to **ADLS** in CSV format.  
   - JSON Source Path: `user_data/json_source/json_source_yymmdd_hhmmssfff.csv`  
   - CSV Source Path: `user_data/csv_source/csv_source_yymmdd_hhmmssfff.csv`

4. **Ingest CSV Data**
   - Use a Dataflow activity in ADF to pull data from the [CSV Source](https://github.com/Kamalesh-Radhakrishnan/adf_data/blob/main/customers.csv).
   - Load the data into the **Silver Layer (Azure SQL)**.

5. **Refresh Snowflake External Table**
   - Refresh the Snowflake external table to point to the updated **ADLS folder**.

---

## **Pipeline Highlights**

- **Silver Layer**: Truncate-and-load process ensures fresh data in each pipeline run.
- **Gold Layer**: Implements SCD-II for historical data tracking.
- **ADLS Storage**: Centralized raw data storage for Snowflake access.
- **ADF Orchestration**: Manages the end-to-end data pipeline seamlessly.

---

## **How to Run the Pipeline**

1. Configure Azure SQL databases, ADLS, and Snowflake as per the project requirements.
2. Set up Azure Data Factory with the following activities:
   - **Copy Activity**: For JSON API ingestion.
   - **Dataflow Activity**: For CSV ingestion and transformations.
   - **Pipeline**: For orchestrating the entire process.
3. Run the pipeline and verify data storage in:
   - **Azure SQL (Silver and Gold Layers)**.
   - **ADLS (CSV files)**.
   - **Snowflake External Table**.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## **Author**
Kamalesh Radhakrishnan  
Feel free to connect and contribute!