from frosttuneiq.spark_session import get_spark_session

spark = get_spark_session()

# Create a sample Iceberg table
spark.sql("""
CREATE TABLE IF NOT EXISTS local_iceberg.sales (
    order_id STRING,
    customer_id STRING,
    region STRING,
    order_date DATE,
    amount DOUBLE
) USING iceberg
""")

# Insert some dummy data
spark.sql("""
INSERT INTO local_iceberg.sales VALUES
('O1', 'C1', 'North', DATE '2025-09-10', 100.0),
('O2', 'C2', 'South', DATE '2025-09-10', 200.0),
('O3', 'C1', 'North', DATE '2025-09-11', 150.0)
""")

print("Sample Iceberg table 'sales' created with dummy data!")
