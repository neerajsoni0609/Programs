'''
1 , Rahul , Dravid | 100k
2 , Virat , Kohli | 200k
3 , MS , Dhoni , 270k
4 , Dinesh , Kartik , 80k
'''

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import col, split, split_part, when, size

spark = SparkSession.builder.appName("data_cleaning").getOrCreate()

schema1 = StructType([
    StructField("id", IntegerType(), True,),
    StructField("first_name", StringType(), True,),
    StructField("last_name", StringType(), True,),
    StructField("salary", StringType(), True,)
])

df = spark.read.format("csv") \
            .schema(schema1) \
            .option("delimiter", " , ") \
            .load("input.txt")

df1 = df.withColumn("splitted_col", split(col("last_name"), "\\s\\|\\s"))
df2 = df1.withColumn("last_name", col("splitted_col").getItem(0)) \
        .withColumn("salary", when(size(col("splitted_col")) > 1, col("splitted_col").getItem(1)).otherwise(col("salary")))

df3 = df2.drop("splitted_col").show()

# Asked in Synechron Interview