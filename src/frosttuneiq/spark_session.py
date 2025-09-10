from pyspark.sql import SparkSession

def get_spark_session():
    spark = (
        SparkSession.builder
        .appName("FrostTuneIQ")
        .master("local[*]")  # Run locally using all cores
        # Iceberg catalog config
        .config("spark.sql.catalog.local_iceberg", "org.apache.iceberg.spark.SparkCatalog")
        .config("spark.sql.catalog.local_iceberg.type", "hadoop")
        .config("spark.sql.catalog.local_iceberg.warehouse", "iceberg_warehouse")
        .getOrCreate()
    )
    return spark
