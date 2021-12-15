from pyspark.sql import SparkSession

from pyspark.sql.types import StringType, StructType, StructField

spark = SparkSession.builder.getOrCreate()

csvSchema = StructType([
    StructField("Store",StringType(),False),
    StructField("Type", StringType(), False),
    StructField("City", StringType(), False),
    ])

df = spark.read.format("csv").option("header", True).schema(csvSchema).load('input/stores.dat')

df.show()

quit()