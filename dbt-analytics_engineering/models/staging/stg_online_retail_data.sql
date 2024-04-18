{{ config(materialized='view') }}

select
    {{ dbt_utils.surrogate_key(['invoice_no', 'invoice_datetime']) }} as transaction_id,
    cast(invoice_no as string) as invoice_no,
    cast(stock_code as string) as stock_code,
    cast(description as string) as description,
    cast(quantity as numeric) as quantity,
    TIMESTAMP_SECONDS(CAST(invoice_datetime / 1000000000 AS INT64)) AS invoice_datetime,
    cast(unit_price as numeric) as unit_price,
    cast(customer_id as string) as customer_id,
    cast(country as string) as country,
    cast(total_price as numeric) as total_price,
    cast(time as time) as time_,
    cast(month as string) as	month,
    cast(day as string)	as day,
    cast(year as string) as year

from {{ source('staging', 'online_retail_data') }}

-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}
