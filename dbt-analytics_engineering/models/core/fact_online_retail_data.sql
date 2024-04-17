{{ config(
    materialized='table',
    partition_by={
      "field": "invoice_datetime",
      "data_type": "timestamp",
      "granularity": "day"
    },
    cluster_by=["customer_id"]
) }}

SELECT *
from {{ ref('stg_online_retail_data') }}
