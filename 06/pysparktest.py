import pyspark
from pyspark.sql import SparkSession

from pyspark.sql.types import StringType, StructType, StructField

spark = SparkSession.builder.getOrCreate()

csvSchema = StructType([
    StructField("id",StringType(),False)
    ])

df = spark.read.format("csv").schema(csvSchema).load('input.dat')

df.show()

quit()