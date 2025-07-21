from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
file_path = "/datasets/orders.json"
df = spark.read.json(file_path)
df_exploded = df.withColumn("product", explode("products"))
df_flattened = df_exploded.select(
"customer_id",
"order_id",
col('product.product_name").alias("product_name"),
col("product.product_price").alias("product_price")
)
display(df_flattened)
