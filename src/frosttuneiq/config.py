from pydantic_settings import BaseSettings


class Config(BaseSettings):
    spark_master: str = "local[*]"
    iceberg_catalog: str = "iceberg_catalog"
    iceberg_warehouse: str = r"C:\Users\Naman.goyal\PycharmProjects\FrostTuneIQ\iceberg_warehouse"
    log_level: str = "INFO"


config = Config()