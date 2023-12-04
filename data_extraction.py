import yaml
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import tabula
import requests
import boto3
import concurrent.futures

class DataExtractor:

    # contruct class
    def __init__(self):
        pass

    def read_rds_table(self, engine, table_name):
        with engine.connect() as connection:
              return pd.read_sql_table(table_name, connection)

    def retrieve_pdf_data(self, url):
        print('RETIEVE PDF DATA FUNCTION CALLED')
        return pd.concat(tabula.read_pdf(url, pages="all"))

    def x_api_key(self):
        return {'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}

    def list_number_of_stores(self):
        url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
        header = self.x_api_key()
        response = requests.get(url, headers=header)
        return response.json()['number_stores']
    
    def retrieve_store_data(self, store_number):
        url = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
        header = self.x_api_key()
        response = requests.get(url, headers=header)
        return pd.json_normalize(response.json())

    def retrieve_all_stores_data(self, number_of_stores):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(self.retrieve_store_data, range(number_of_stores)))
        df_storesdata = pd.concat(results)
        return df_storesdata
    
    def process_all_stores(self):
        number_of_stores = self.list_number_of_stores()
        df_all_stores = self.retrieve_all_stores_data(number_of_stores)
        # Process the concatenated DataFrame as needed
        return df_all_stores
        

    def extract_from_s3(self):
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket = 'data-handling-public', Key = 'products.csv')
        return pd.read_csv(response['Body'])
    
    def extract_dates_data(self):
        url = f'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
        response = requests.get(url)
        return pd.DataFrame(response.json())
        
        
        
        