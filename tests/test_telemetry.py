from frosttuneiq.telemetry.collector import TelemetryCollector

def test_collect():
    collector = TelemetryCollector()
    result = collector.collect("iceberg_catalog.db_sales")
    assert "table" in result
    assert "filters" in result
    assert "joins" in result
    print("Telemetry test passed!")
