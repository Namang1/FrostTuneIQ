from pyspark.sql import SparkSession

def get_spark_session():
    spark = (
        SparkSession.builder
        .appName("FrostTuneIQ")
        # Connect to the Spark Master running in Docker
        .master("spark://localhost:7077")
        .config(
            "spark.jars.packages",
            "org.apache.iceberg:iceberg-spark-runtime-3.4_2.13:1.5.2"  # use latest stable Iceberg
        )
        .config("spark.sql.catalog.local_iceberg", "org.apache.iceberg.spark.SparkCatalog")
        .config("spark.sql.catalog.local_iceberg.type", "hadoop")
        .config("spark.sql.catalog.local_iceberg.warehouse", "/opt/bitnami/spark/iceberg_warehouse")
        .getOrCreate()
    )
    return spark


if __name__ == "__main__":
    spark = get_spark_session()
    print("✅ Spark session created successfully!")
    print("🔥 Spark version:", spark.version)
    print("📂 Available databases:", spark.catalog.listDatabases())
