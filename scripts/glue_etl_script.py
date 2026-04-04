import sys
from pyspark.context import SparkContext
from pyspark.sql.functions import to_date
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

# Load raw data
df = spark.read.csv(
    "s3://superstore-analytics-bucket/raw/Sample_Superstore.csv",
    header = True,
    inferSchema = True
)

# Basic transformations
df_clean = df.dropDuplicates()

# Convert dates
df_clean = df_clean.withColumn("Order Date", to_date("Order Date", "MM/dd/yyyy"))

# Write to curated layer (Parquet)
df_clean.write.mode("overwrite").parquet(
    "s3://superstore-analytics-bucket/curated/orders/"
)