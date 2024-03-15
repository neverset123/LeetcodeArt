/*
delta lake is a storage layer that brings ACID transactions to Apache Spark and big data workloads.
delta cache enable
spark.databricks.io.cache.maxDiskUsage = 100GB
spark.databricks.io.cache.maxMetaDataCache = 100GB
spark.databricks.io.cache.compression.enabled = true
*/

-- result cache
cache select * from delta.`/mnt/delta/bronze/bronze` as bronze where bronze.id = 1

-- check table time travel
DESCRIBE HISTORY delta.`/mnt/delta/bronze/bronze`

-- query at specific timestamp
SELECT * FROM delta.`/mnt/delta/bronze/bronze` TIMESTAMP AS OF '2022-01-01 00:00:00'

-- merge dataset on condition
MERGE INTO delta.`/mnt/delta/bronze/bronze` as target
Using delta.`/mnt/delta/bronze/bronze` as source
ON target.id = source.id
WHEN MATCHED THEN
  UPDATE SET *
WHEN NOT MATCHED THEN
  INSERT *

-- optimize for data reading
OPTIMIZE delta.`/mnt/delta/bronze/bronze` zorder by id

-- write data to delta lake with updated schema
-- df.write.format("delta").mode("overwrite").option("mergeSchema", "true").save("/mnt/delta/bronze/bronze")