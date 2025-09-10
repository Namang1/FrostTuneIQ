from frosttuneiq.optimizer.recluster import ReclusterEngine

def test_recluster():
    recluster = ReclusterEngine()
    result = recluster.execute("iceberg_catalog.db_sales", "ALTER TABLE iceberg_catalog.db_sales ADD PARTITION (order_date='2025-09-10')")
    assert result is True
    print("Recluster test passed!")
