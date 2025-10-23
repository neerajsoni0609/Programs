import pandas as pd

from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, dense_rank, sum

data = {
   "region": ["East", "East", "East", "West", "West", "South", "South", "South"],
   "salesperson": ["Alice", "Bob", "Alice", "David", "Eva", "Frank", "Grace", "Frank"],
   "amount": [100, 200, 50, 300, 150, 400, 100, 200]
}
df = pd.DataFrame(data)

spark = SparkSession.builder.appName("Demo").getOrCreate()
df1 = spark.createDataFrame(df)

df3 = df1.groupBy("region", "salesperson").agg(sum("amount").alias("amount"))

window_ref = Window.partitionBy("region").orderBy(col("amount").desc())
df2 = df3.withColumn("rank", dense_rank().over(window_ref))
df2.show()
