'''
user_id, ts, amount, status
42, 2025-07-01T10:01:00Z, 9.50, SUCCESS
42, 2025-07-01T11:45:00Z, 12.00, FAILED

1. Read July 2025 data from S3. Keep only SUCCESS.
2. Create dt = to_date(ts) and compute daily spend per user.
3. Ensure a complete user × date grid for July (fill missing with 0).
4. Write Parquet to s3://…/orders_daily/, partitioned by dt, targeting ~256MB files.
'''

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Demo").getOrCreate()

df = spark.read.csv("demo.csv", header = True, inferSchema = True)
df1 = df.withColumn("Date", F.to_date(F.col("ts")), F.date_format(F.col("ts"), "HH:mm:ss"))
df1.drop("ts")
df1.where(F.col("status") == "SUCCESS")

# Asked in OpenGov Interview