# src/frosttuneiq/optimizer/partitioner.py
"""Generates new Iceberg partition specs dynamically."""

class DynamicPartitioner:
    def generate_spec(self, table: str, suggestions: dict):
        print(f"[Partitioner] Generating new partition spec for {table}...")
        spec_parts = []
        for col, buckets in suggestions.get("bucket_suggestions", {}).items():
            spec_parts.append(f"bucket({buckets}, {col})")
        return f"ALTER TABLE {table} SET PARTITION SPEC ({', '.join(spec_parts)})"

