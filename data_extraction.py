# -*- coding: utf-8 -*-

import yaml
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import tabula
import requests
import boto3

class DataExtractor:

    # contruct class
    def __init__(self):
        pass

    def read_rds_table(self, engine, table_name):
        with engine.connect() as connection:
              return pd.read_sql_table(table_name, connection)

    def retrieve_pdf_data(self, url):
        return pd.concat(tabula.read_pdf(url, pages="all"))

    def x_api_key(self):
        return {'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}

    def list_number_of_stores(self):
        url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
        header = self.x_api_key()
        response = requests.get(url, headers=header)
        return response.json()['number_stores']

    def retrieve_stores_data(self, number_of_stores):
        df_storesdata = []
        for store_number in range(number_of_stores):
            url = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
            header = self.x_api_key()
            response = requests.get(url, headers=header)
            df_storesdata.append(pd.json_normalize(response.json()))
        return pd.concat(df_storesdata)

    def extract_from_s3(self):
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket = 'data-handling-public', Key = 'products.csv')
        return pd.read_csv(response['Body'])
    
    def extract_dates_data(self):
        url = f'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
        response = requests.get(url)
        return pd.DataFrame(response.json())
        
        
        
        