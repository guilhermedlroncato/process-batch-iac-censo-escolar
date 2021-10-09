import boto3
import pandas as pd

# criar um cliente para integragir com S3
s3_client = boto3.client('s3')

# fazendo upload de arquivo para o bucket S3
print('Iniciando Upload do arquivo matricula_co.csv...')
s3_client.upload_file('../data/matricula_co.csv', 'datalake-roncato-igti-edc-tf', 'raw-data/censo/matricula_co.csv')
print('Iniciando Upload do arquivo matricula_nordeste.csv...')
s3_client.upload_file('../data/matricula_nordeste.csv', 'datalake-roncato-igti-edc-tf', 'raw-data/censo/matricula_nordeste.csv')
print('Iniciando Upload do arquivo matricula_norte.csv...')
s3_client.upload_file('../data/matricula_norte.csv', 'datalake-roncato-igti-edc-tf', 'raw-data/censo/matricula_norte.csv')
print('Iniciando Upload do arquivo matricula_sudeste.csv...')
s3_client.upload_file('../data/matricula_sudeste.csv', 'datalake-roncato-igti-edc-tf', 'raw-data/censo/matricula_sudeste.csv')
print('Iniciando Upload do arquivo matricula_sul.csv...')
s3_client.upload_file('../data/matricula_sul.csv', 'datalake-roncato-igti-edc-tf', 'raw-data/censo/matricula_sul.csv')

