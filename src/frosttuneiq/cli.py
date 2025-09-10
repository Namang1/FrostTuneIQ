import typer
from frosttuneiq.telemetry.collector import TelemetryCollector
from frosttuneiq.optimizer.recluster import ReclusterEngine

app = typer.Typer()

@app.command()
def run(table: str):
    print(f"Running FrostTuneIQ on table: {table}")
    collector = TelemetryCollector()
    telemetry = collector.collect(table)
    print("[Telemetry Collected]", telemetry)

    recluster = ReclusterEngine()
    # Example: just a placeholder SQL
    partition_sql = f"ALTER TABLE {table} ADD PARTITION (order_date='2025-09-10')"
    recluster.execute(table, partition_sql)
    print("[Recluster Complete]")

if __name__ == "__main__":
    app()
