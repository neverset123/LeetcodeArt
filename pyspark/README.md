## data tyep
to avoid change data type from int to float
```
df.withColumn("timestamp", F.col(timestamp)-int(1*60))
```