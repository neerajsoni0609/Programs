'''
empid  date        status
101    10-01-2025  A
101    11-01-2025  A
101    12-01-2025  A
101    13-01-2025  P
101    14-01-2025  A
102    10-01-2025  A
102    11-01-2025  A
102    12-01-2025  P
102    13-01-2025  P
102    14-01-2025  A

Find employees with 3 or more consecutive absences
'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, when, lag, sum, row_number
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("get_data").getOrCreate()

data = [(101, "10-01-2025",  "A"), (101, "11-01-2025",  "A"), (101, "12-01-2025",  "A"), (101, "13-01-2025",  "P") \
        , (101, "14-01-2025", "A"), (102, "10-01-2025", "A"), (102, "11-01-2025", "A"), (102, "12-01-2025", "P") \
        , (102, "13-01-2025", "P"), (102, "14-01-2025", "A")]

columns = ["empid", "date", "status"]

df = spark.createDataFrame(data, columns)
df1 = df.withColumn("date_up", to_date(col("date")))

window_spec = Window.partitionBy("empid").orderBy("date")

df2 = df1.withColumn("row_number", row_number().over(window_spec)).where(col("status") == "A")

df1.show()