# -*- coding: utf-8 -*-
"""data_extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T0ktQEuI2q6liyulA7NvQ8YMdACiF1V-
"""

import yaml
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import tabula
import requests

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
    return response.json()['number_of_stores']

  def retrieve_stores_data(self, number_of_stores):
    df_storesdata = []
    for store_number in range(number_of_stores):
      url = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
      header = self.x_api_key()
      response = requests.get(url, headers=header)
      df_storesdata.append(pd.json_normalize(response.json()))
    return pd.concat(df_storesdata)