# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Enter the file path here
file_path = "/datasets/orders.json"

# Read the JSON file
df = spark.read.json(file_path)

# Explode the products array
df_exploded = df.withColumn("product", explode("products"))

# Select and flatten the required fields
df_flat = df_exploded.select(
    col("customer_id"),
    col("order_id"),
    col("product.product_name").alias("product_name"),
    col("product.product_price").alias("product_price")
)

# Display the final DataFrame using the display() function
display(df_flat)
