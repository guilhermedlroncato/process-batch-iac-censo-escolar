from pyspark.sql.functions import max, count, mean, col, min
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName('ExerciseSpark').getOrCreate()
)

# ler dados do censo escolar 2020 no S3
enem = spark.read\
        .format('csv')\
        .option('header', True)\
        .option('inferSchema', True)\
        .option('delimiter', ';')\
        .load('s3://datalake-roncato-igti-edc-tf/raw-data/censo/')

# salvar o dado em parquet no S3
enem\
    .write\
    .mode('overwrite')\
    .format('parquet')\
    .save('s3://datalake-roncato-igti-edc-tf/staging/censo/')
