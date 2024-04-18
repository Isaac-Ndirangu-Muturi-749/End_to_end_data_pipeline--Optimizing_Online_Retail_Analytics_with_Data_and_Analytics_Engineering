{{ config(
    materialized='table'
) }}

SELECT *
from {{ ref('stg_online_retail_data') }}
