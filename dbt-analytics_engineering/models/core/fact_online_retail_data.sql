{{ config(materialized='table') }}

select *
from {{ ref('stg_online_retail_data') }}
