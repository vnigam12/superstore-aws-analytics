-- Create table
create external table superstore_orders (
    order_id STRING,
    order_date DATE,
    ship_mode STRING,
    customer_name STRING,
    segment STRING,
    region STRING,
    category STRING,
    sales DOUBLE,
    profit DOUBLE
)
stored as parquet
location 's3://superstore-analytics-bucket/curated/orders/';

-- Sample analysis queries
-- Query 1. Top regions by sales
select region, sum(sales) as total_sales
from superstore_orders
group by region
order by total_sales desc;

-- Query 2. Profitability by category
select category, sum(profit) as total_profit
from superstore_orders
group by category;