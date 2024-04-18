# End_to_end_data_pipeline---Optimizing_Online_Retail_Analytics_with_Data_and_Analytics_Engineering

![](images/data_analytics_pipeline.png)

## PROJECT STRUCTURE
```
.
├── README.md
├── (CI.CD)-Continous-Intergration-and-Deployment
│   └── cloudbuild.yaml
├── Looker_studio_Dashboard
├── data
│   ├── Online Retail.xlsx
│   └── README.md
├── dbt-Analytics_Engineering(Data Build Tool)
│   ├── README.md
│   ├── analyses
│   ├── dbt_project.yml
│   ├── macros
│   ├── models
│   │   ├── core
│   │   │   ├── fact_online_retail_data_partitioned_clustered.sql
│   │   │   └── fact_online_retail_data_unpartitioned.sql
│   │   └── staging
│   │       ├── schema.yml
│   │       └── stg_online_retail_data.sql
│   ├── package-lock.yml
│   ├── packages.yml
│   ├── seeds
│   ├── snapshots
│   └── tests
├── images
│   ├── data_analytics_pipeline.png
│   ├── data_analytics_pipeline.png:Zone.Identifier
│   ├── dbt_deploy_job_12hrs.png
│   ├── dbt_lineage_graph_DAG.png
│   ├── dbt_project_overview.png
│   ├── fact_online_retail_data_partitioned_clustered.png
│   ├── fact_online_retail_data_unpartitioned.png
│   ├── loading_from_api_transformations_to_gcs_partitioned.png
│   ├── loading_from_google_cloud_storage_to_bigquery_table.png
│   ├── pipelines_in_mage.png
│   ├── stg_online_retail_data.png
│   └── trigger_for_mage.png
├── mage-ai-Terraform-Infrastructure-As-Code
│   ├── README.md
│   ├── db.tf
│   ├── direct-disk-412820-2333e42872f1.json
│   ├── fs.tf
│   ├── load_balancer.tf
│   ├── main.tf
│   ├── terraform.tfstate
│   ├── terraform.tfstate.backup
│   └── variables.tf
└── mage-ai-Workflow-Orchestration
    ├── Dockerfile
    ├── README.md
    ├── direct-disk-412820-2333e42872f1.json
    ├── docker-compose.yml
    ├── mage_data
    │   └── magic-zoomcamp
    │       ├── mage-ai.db
    │       └── pipelines
    │           ├── example_pipeline
    │           ├── gcs_to_bigquery
    │           ├── loading_from_api_transformations_to_gcs_partitioned
    │           ├── loading_from_google_cloud_storage_to_bigquery_table
    │           ├── online_retail_data_loading_api_processing_to_gcs_partitioned
    │           ├── spirited_familiar
    │           └── spirited_hill
    ├── magic-zoomcamp
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   └── __init__.cpython-310.pyc
    │   ├── charts
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-310.pyc
    │   ├── custom
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-310.pyc
    │   ├── data_exporters
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   ├── cosmic_firefly.cpython-310.pyc
    │   │   │   ├── export_titanic_clean.cpython-310.pyc
    │   │   │   └── soulful_night.cpython-310.pyc
    │   │   ├── export_data_to_google_bigquery.py
    │   │   └── export_data_to_google_cloud_stoage_partitioned.py
    │   ├── data_loaders
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   ├── load_api_data.cpython-310.pyc
    │   │   │   ├── load_titanic.cpython-310.pyc
    │   │   │   ├── moonlit_water.cpython-310.pyc
    │   │   │   └── red_portal.cpython-310.pyc
    │   │   ├── daring_ancient.py
    │   │   ├── enigmatic_sky.py
    │   │   ├── load_data_from_api.py
    │   │   ├── load_data_from_google_cloud_storage.py
    │   │   ├── load_titanic.py
    │   │   ├── moonlit_water.py
    │   │   ├── polished_realm.py
    │   │   ├── refined_spellcaster.py
    │   │   ├── relaxed_monk.sql
    │   │   ├── timeless_sunrise.py
    │   │   └── utopian_ancient.py
    │   ├── dbt
    │   │   └── profiles.yml
    │   ├── dbts
    │   │   ├── __init__.py
    │   │   ├── humble_ancient.yaml
    │   │   ├── humble_sword.yaml
    │   │   └── mindful_silversmith.yaml
    │   ├── extensions
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-310.pyc
    │   ├── interactions
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-310.pyc
    │   ├── io_config.yaml
    │   ├── metadata.yaml
    │   ├── pipelines
    │   │   ├── __init__.py
    │   │   ├── loading_from_api_transformations_to_gcs_partitioned
    │   │   │   ├── __init__.py
    │   │   │   ├── __pycache__
    │   │   │   │   └── __init__.cpython-310.pyc
    │   │   │   └── metadata.yaml
    │   │   └── loading_from_google_cloud_storage_to_bigquery_table
    │   │       ├── __init__.py
    │   │       ├── __pycache__
    │   │       │   └── __init__.cpython-310.pyc
    │   │       └── metadata.yaml
    │   ├── requirements.txt
    │   ├── scratchpads
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-310.pyc
    │   ├── transformers
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   ├── fill_in_missing_values.cpython-310.pyc
    │   │   │   └── radiant_destiny.cpython-310.pyc
    │   │   └── transform_and_clean_api_data.py
    │   └── utils
    │       ├── __init__.py
    │       └── __pycache__
    │           └── __init__.cpython-310.pyc
    └── requirements.txt
```


## DATASET**:
Choose datasets that are suitable for building a data pipeline and dashboard. Look for datasets with sufficient volume, variety, and relevance to demonstrate your skills.

#### Files and Directories
```
├── data
│   ├── Online Retail.xlsx
│   └── README.md
```

A well-known dataset is the "Online Retail" dataset from the UCI Machine Learning Repository. This dataset contains transactional data from an online retail platform and is suitable for analyzing sales trends, customer behavior, and product performance.

Here are some details about the "Online Retail" dataset:

- **Source**: UCI Machine Learning Repository
- **Description**: This dataset contains transactional data from an online retail store based in the United Kingdom. The data includes customer information, product details, invoice numbers, transaction dates, and sales quantities. It covers transactions that occurred between 01/12/2010 and 09/12/2011.
- **Features**: The dataset includes attributes such as InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, and Country.
- **Format**: The dataset is typically provided in a CSV (Comma Separated Values) format.
- **Size**: The dataset is relatively small, with around 500,000 records.

You can find the "Online Retail" dataset on the UCI Machine Learning Repository website. Here is the direct link: [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail).

This dataset is popular among data scientists and analysts for exploring eCommerce sales data, performing market basket analysis, and building recommendation systems. It's a great choice for your data engineering project as it provides rich transactional data that can be used for various analyses and insights.




# **INFRASTRUCTURE AS CODE (IaC)**:
   - Use Infrastructure as Code (IaC) tools like Terraform to provision cloud resources.

#### Terraform
[Terraform](https://www.terraform.io/) is an open-source infrastructure as code software tool created by HashiCorp. It allows users to define and provision data center infrastructure using a high-level configuration language known as HashiCorp Configuration Language (HCL).

#### Files and Directories
```
├── mage-ai-Terraform-Infrastructure-As-Code
│   ├── README.md
│   ├── db.tf
│   ├── fs.tf
│   ├── load_balancer.tf
│   ├── main.tf
│   └── variables.tf
```


#### Usage
1. **Installation**: Ensure Terraform is installed on your local machine.
2. **Configuration**: Modify the `.tf` files to match your desired infrastructure configuration.
3. **Initialization**: Run `terraform init` to initialize the working directory containing Terraform configuration files.
4. **Planning**: Run `terraform plan` to create an execution plan. This step is optional but recommended to verify changes before applying them.
5. **Execution**: Run `terraform apply` to apply the changes required to reach the desired state of the configuration.
6. **Verification**: After applying changes, verify that the infrastructure has been provisioned correctly.
7. **Cleanup**: When done, run `terraform destroy` to destroy all the resources defined in the Terraform configuration.


# **DESIGN THE DATA PIPELINE**:
   - Decide whether to implement a batch  pipeline based on your preferences and the nature of the data.
   - Choose appropriate cloud services and infrastructure tools for data storage, processing, and orchestration.
   - Define the steps for data ingestion, transformation, loading into data lakes and data warehouses, and dashboard creation.

![](images/pipelines_in_mage.png)


![](images/loading_from_api_transformations_to_gcs_partitioned.png)

#### Files and Directories
```
└── mage-ai-Workflow-Orchestration
    ├── magic-zoomcamp
        ├── pipelines
        │   └── loading_from_api_transformations_to_gcs_partitioned
        ├── data_loaders
        │   └── load_data_from_api.py
        ├── transformers
        |   └── transform_and_clean_api_data.py
        └── data_exporters
            └── export_data_to_google_cloud_stoage_partitioned.py
```


![](images/loading_from_google_cloud_storage_to_bigquery_table.png)

#### Files and Directories
```
└── mage-ai-Workflow-Orchestration
    ├── magic-zoomcamp
        ├── pipelines
        │   └── loading_from_google_cloud_storage_to_bigquery_table
        ├── data_loaders
        │   └── load_data_from_google_cloud_storage.py
        └─ data_exporters
            └── export_data_to_google_bigquery.py
```

![](images/trigger_for_mage.png)

* **Batch**: If you want to run things periodically (/daily) in mage


5. **Implement Data Pipelines**:
   - Implement workflow orchestration using tools such as Mage to Develop batch processing and managing pipeline execution.



6. **PERFORM DATA TRANSFORMATIONS**:
   - Apply transformations using dedicated data transformation tools like dbt to prepare data for analytics.
   - Ensure data quality and consistency through validation and cleansing processes.
![](images/dbt_lineage_graph_DAG.png)
![](images/dbt_project_overview.png)

#### Files and Directories

```
├── dbt-Analytics_Engineering(Data Build Tool)
│   ├── dbt_project.yml
│   └── models
│       ├── core
│       │   ├── fact_online_retail_data_partitioned_clustered.sql
│       │   └── fact_online_retail_data_unpartitioned.sql
│       └── staging
│           ├── schema.yml
│           └── stg_online_retail_data.sql
```
![](images/dbt_deploy_job_12hrs.png)

8. **DOCUMENTATION AND TESTING**:
   - Document the project setup, data pipeline architecture, and dashboard components in a README file.

#### Files and Directories
```
├── dbt-Analytics_Engineering(Data Build Tool)
│   ├── dbt_project.yml
│   ├── models
│   │   └── staging
│   │       └── schema.yml
│   └── tests
```

# **BUILD THE DASHBOARD**:
   - Choose a BI tool such as Data Studio for creating the dashboard.
   - Design intuitive visualizations that provide insights into the processed data.
#### Files and Directories
```
├── Looker_studio_Dashboard
```

# (CI/CD)-CONTINOUS-INTERGRATION-AND-DEPLOYMENT


#### Files and Directories
```
├── (CI.CD)-Continous-Intergration-and-Deployment
│   └── cloudbuild.yaml
```




## Course Project

### Objective

The goal of this project is to apply everything we have learned
in this course to build an end-to-end data pipeline.

### Problem statement

Develop a dashboard with two tiles by:

* Selecting a dataset of interest (see [Datasets](#datasets))
* Creating a pipeline for processing this dataset and putting it to a datalake
* Creating a pipeline for moving the data from the lake to a data warehouse
* Transforming the data in the data warehouse: prepare it for the dashboard
* Building a dashboard to visualize the data


## Data Pipeline

The pipeline is be **batch**: this is the first thing you'll need to decide

* **Batch**: If you want to run things periodically (e.g. hourly/daily)

## Technologies

* **Cloud**: GCP
* **Infrastructure as code (IaC)**: Terraform, Google Cloud Run, Cloud Build
* **Workflow orchestration**: Mage
* **Data Warehouse**: BigQuery
* **Dashboard**: Looker Studio


## Dashboard

You can use any of the tools shown in the course (Data Studio or Metabase) or any other BI tool of your choice to build a dashboard. If you do use another tool, please specify and make sure that the dashboard is somehow accessible to your peers.

Your dashboard should contain at least two tiles, we suggest you include:

- 1 graph that shows the distribution of some categorical data
- 1 graph that shows the distribution of the data across a temporal line

Ensure that your graph is easy to understand by adding references and titles.

Example dashboard: ![image](https://user-images.githubusercontent.com/4315804/159771458-b924d0c1-91d5-4a8a-8c34-f36c25c31a3c.png)



## Evaluation Criteria

* Problem description
    * 0 points: Problem is not described
    * 2 points: Problem is described but shortly or not clearly
    * 4 points: Problem is well described and it's clear what the problem the project solves
* Cloud
    * 0 points: Cloud is not used, things run only locally
    * 2 points: The project is developed in the cloud
    * 4 points: The project is developed in the cloud and IaC tools are used
* Data ingestion (choose either batch or stream)
    * Batch / Workflow orchestration
        * 0 points: No workflow orchestration
        * 2 points: Partial workflow orchestration: some steps are orchestrated, some run manually
        * 4 points: End-to-end pipeline: multiple steps in the DAG, uploading data to data lake
    * Stream
        * 0 points: No streaming system (like Kafka, Pulsar, etc)
        * 2 points: A simple pipeline with one consumer and one producer
        * 4 points: Using consumer/producers and streaming technologies (like Kafka streaming, Spark streaming, Flink, etc)
* Data warehouse
    * 0 points: No DWH is used
    * 2 points: Tables are created in DWH, but not optimized
    * 4 points: Tables are partitioned and clustered in a way that makes sense for the upstream queries (with explanation)
* Transformations (dbt, spark, etc)
    * 0 points: No tranformations
    * 2 points: Simple SQL transformation (no dbt or similar tools)
    * 4 points: Tranformations are defined with dbt, Spark or similar technologies
* Dashboard
    * 0 points: No dashboard
    * 2 points: A dashboard with 1 tile
    * 4 points: A dashboard with 2 tiles
* Reproducibility
    * 0 points: No instructions how to run the code at all
    * 2 points: Some instructions are there, but they are not complete
    * 4 points: Instructions are clear, it's easy to run the code, and the code works


> [!NOTE]
> It's highly recommended to create a new repository for your project (not inside an existing repo) with a meaningful title, such as
> "Quake Analytics Dashboard" or "Bike Data Insights" and include as many details as possible in the README file. ChatGPT can assist you with this. Doing so will not only make it easier to showcase your project for potential job opportunities but also have it featured on the [Projects Gallery App](#projects-gallery).
> If you leave the README file empty or with minimal details, there may be point deductions as per the [Evaluation Criteria](#evaluation-criteria).

## Going the extra mile (Optional)

> [!NOTE]
> The following things are not covered in the course, are entirely optional and they will not be graded.

However, implementing these could significantly enhance the quality of your project:

* Add tests
* Use make
* Add CI/CD pipeline




$ tree
.
├── README.md
├── dashboard
├── data
│   ├── Online Retail.xlsx
│   └── README.md
├── dbt-analytics_engineering(Data Build Tool)
│   ├── README.md
│   ├── analyses
│   ├── dbt_project.yml
│   ├── macros
│   ├── models
│   │   ├── core
│   │   │   ├── fact_online_retail_data_partitioned_clustered.sql
│   │   │   └── fact_online_retail_data_unpartitioned.sql
│   │   └── staging
│   │       ├── schema.yml
│   │       └── stg_online_retail_data.sql
│   ├── package-lock.yml
│   ├── packages.yml
│   ├── seeds
│   ├── snapshots
│   └── tests
├── mage-ai-Terraform-Infrastructure-As-Code
│   ├── README.md
│   ├── db.tf
│   ├── direct-disk-412820-2333e42872f1.json
│   ├── fs.tf
│   ├── load_balancer.tf
│   ├── main.tf
│   ├── terraform.tfstate
│   ├── terraform.tfstate.backup
│   └── variables.tf
└── mage-ai-Workflow-Orchestration
    ├── Dockerfile
    ├── README.md
    ├── cloudbuild.yaml
    ├── direct-disk-412820-2333e42872f1.json
    ├── docker-compose.yml
    ├── mage_data
    │   └── magic-zoomcamp
    │       ├── mage-ai.db
    │       └── pipelines
    │           ├── example_pipeline
    │           ├── gcs_to_bigquery
    │           ├── loading_from_api_transformations_to_gcs_partitioned
    │           ├── loading_from_google_cloud_storage_to_bigquery_table
    │           ├── online_retail_data_loading_api_processing_to_gcs_partitioned
    │           ├── spirited_familiar
    │           └── spirited_hill
    ├── magic-zoomcamp
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   └── __init__.cpython-310.pyc
    │   ├── charts
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-310.pyc
    │   ├── custom
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-310.pyc
    │   ├── data_exporters
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   ├── cosmic_firefly.cpython-310.pyc
    │   │   │   ├── export_titanic_clean.cpython-310.pyc
    │   │   │   └── soulful_night.cpython-310.pyc
    │   │   ├── export_data_to_google_bigquery.py
    │   │   ├── export_data_to_google_cloud_stoage_partitioned.py
    │   │   └── export_titanic_clean.py
    │   ├── data_loaders
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   ├── load_api_data.cpython-310.pyc
    │   │   │   ├── load_titanic.cpython-310.pyc
    │   │   │   ├── moonlit_water.cpython-310.pyc
    │   │   │   └── red_portal.cpython-310.pyc
    │   │   ├── daring_ancient.py
    │   │   ├── enigmatic_sky.py
    │   │   ├── load_data_from_api.py
    │   │   ├── load_data_from_google_cloud_storage.py
    │   │   ├── load_titanic.py
    │   │   ├── moonlit_water.py
    │   │   ├── polished_realm.py
    │   │   ├── refined_spellcaster.py
    │   │   ├── relaxed_monk.sql
    │   │   ├── timeless_sunrise.py
    │   │   └── utopian_ancient.py
    │   ├── dbt
    │   │   └── profiles.yml
    │   ├── dbts
    │   │   ├── __init__.py
    │   │   ├── humble_ancient.yaml
    │   │   ├── humble_sword.yaml
    │   │   └── mindful_silversmith.yaml
    │   ├── extensions
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-310.pyc
    │   ├── interactions
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-310.pyc
    │   ├── io_config.yaml
    │   ├── metadata.yaml
    │   ├── pipelines
    │   │   ├── __init__.py
    │   │   ├── example_pipeline
    │   │   │   ├── __init__.py
    │   │   │   ├── __pycache__
    │   │   │   │   └── __init__.cpython-310.pyc
    │   │   │   └── metadata.yaml
    │   │   ├── loading_from_api_transformations_to_gcs_partitioned
    │   │   │   ├── __init__.py
    │   │   │   ├── __pycache__
    │   │   │   │   └── __init__.cpython-310.pyc
    │   │   │   └── metadata.yaml
    │   │   └── loading_from_google_cloud_storage_to_bigquery_table
    │   │       ├── __init__.py
    │   │       ├── __pycache__
    │   │       │   └── __init__.cpython-310.pyc
    │   │       └── metadata.yaml
    │   ├── requirements.txt
    │   ├── scratchpads
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-310.pyc
    │   ├── transformers
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-310.pyc
    │   │   │   ├── fill_in_missing_values.cpython-310.pyc
    │   │   │   └── radiant_destiny.cpython-310.pyc
    │   │   ├── fill_in_missing_values.py
    │   │   └── transform_and_clean_api_data.py
    │   └── utils
    │       ├── __init__.py
    │       └── __pycache__
    │           └── __init__.cpython-310.pyc
    └── requirements.txt

52 directories, 91 files
ndirangu749@de-zoomcamp ~/capstone_de_zoom
$

data

A well-known dataset is the "Online Retail" dataset from the UCI Machine Learning Repository. This dataset contains transactional data from an online retail platform and is suitable for analyzing sales trends, customer behavior, and product performance.

Here are some details about the "Online Retail" dataset:

- **Source**: UCI Machine Learning Repository
- **Description**: This dataset contains transactional data from an online retail store based in the United Kingdom. The data includes customer information, product details, invoice numbers, transaction dates, and sales quantities. It covers transactions that occurred between 01/12/2010 and 09/12/2011.
- **Features**: The dataset includes attributes such as InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, and Country.
- **Format**: The dataset is typically provided in a CSV (Comma Separated Values) format.
- **Size**: The dataset is relatively small, with around 500,000 records.

You can find the "Online Retail" dataset on the UCI Machine Learning Repository website. Here is the direct link: [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail).

This dataset is popular among data scientists and analysts for exploring eCommerce sales data, performing market basket analysis, and building recommendation systems. It's a great choice for your data engineering project as it provides rich transactional data that can be used for various analyses and insights.


terraform - Iaas

data - db.tf postgres 14
load_balancer.tf
fs.tf - filesystem Gcs
main.tf
variables.tf = variables





pipelines
1. loading_from_google_cloud_storage_to_bigquery_table
2. loading_from_api_transformations_to_gcs_partitioned

data_loader


transformer


data_exporter

load_data_from_api


transform_and_clean_api_data


export_data_to_google_cloud_stoage_partitioned



trigger for mage


dbt

documentation link = https://cloud.getdbt.com/accounts/246257/jobs/576492/docs/#!/overviewhttps://cloud.getdbt.com/accounts/246257/jobs/576492/docs/#!/overview


lineage graph

link for each model scripts

source
staging
core - fact tables





![](images/stg_online_retail_data.png)
![](images/fact_online_retail_data_partitioned_clustered.png)
![](images/fact_online_retail_data_unpartitioned.png)
