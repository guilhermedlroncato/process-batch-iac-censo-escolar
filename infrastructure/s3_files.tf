resource "aws_s3_bucket_object" "spark_insert" {
  bucket = aws_s3_bucket.dl.id
  key    = "emr-code/pyspark/spark_insert_staging.py"
  acl    = "private"
  source = "../etl/spark_insert_staging.py"
  etag   = filemd5("../etl/spark_insert_staging.py")
}
