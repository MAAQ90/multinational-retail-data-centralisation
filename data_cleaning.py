import pandas as pd
import numpy as np

class DataCleaning:

  # contruct class
    def __init__(self):
        
        pass
    
    def clean_user_data(self, df):
        
        print('FUNCTION CALLED: CLEAN_USER_DATA')
        
        df.to_csv("user_data_original.csv", mode='w', index=False)
        
        # Remove the index column (due to duplication):
        df.drop(columns = ['index'], inplace=True)
        # Uniform reformatting of dates columns, set to datetime type, and remove those with missing data:
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors = 'coerce')
        df['join_date']     = pd.to_datetime(df['join_date'], errors = 'coerce')
        df                  = df.dropna(subset=['date_of_birth', 'join_date'], how='all')
        # Uniform reformatting of phone numbers:
        df.loc[:, "phone_number"] = df["phone_number"].str.replace(r'[^\d+()-]', '', regex=True)
        df.loc[:, "phone_number"] = df["phone_number"].str.strip().str.replace(r'\s+', ' ', regex=True)
        
        df.to_csv("user_data_cleaned.csv", mode='w', index=False)

        return df

    def clean_card_data(self, df):
        
        print('FUNCTION CALLED: CLEAN_CARD_DATA')
        df.to_csv("card_data_original.csv", mode='w', index=False)
        
        
        df.replace('NULL', np.nan, inplace=True)
        df[df['card_number'] != 'NULL']
        #df.drop_duplicates(subset=['card_number'], keep='first', inplace=True)
        df['card_number'] = df['card_number'].apply(str)
        df['card_number'] = df['card_number'].str.replace(r'\D', '', regex=True)
        # Correct  dates format:
        df['expiry_date'] = pd.to_datetime(df['expiry_date'], format='%m/%y', errors='coerce')
        df['date_payment_confirmed'] = df['date_payment_confirmed'].str.strip()
        df['date_payment_confirmed'] = df['date_payment_confirmed'].apply(lambda x: pd.to_datetime(x, errors='ignore'))
        #pd.to_datetime(df['date_payment_confirmed'], format='%B %Y %d', errors='coerce')
        df.dropna(how='any',inplace= True)
        
        df.to_csv("card_data_cleaned.csv", mode='w', index=False)
        
        return df

    def clean_store_data(self, df):
        
        print('FUNCTION CALLED: CLEAN_STORE_DATA')
        
        df.to_csv("store_data_original.csv", mode='w', index=False)
        
        df = df.drop(columns=['index','lat'], errors = 'coerce')
        df['address'] = df['address'].str.replace('\n', ' ', regex=False)
        df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
        df['staff_numbers'] = df['staff_numbers'].str.extract('(\d+\.?\d*)')
        df['staff_numbers'] = pd.to_numeric(df['staff_numbers'], errors='coerce')
        df['opening_date'] = df['opening_date'].apply(lambda x: pd.to_datetime(x, errors='ignore'))
        df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
        df['continent'] = df['continent'].str.replace('^ee', '', regex=True)
        df = df.dropna(subset=['staff_numbers', 'longitude', 'opening_date', 'latitude'], how='all')
        
        df.to_csv("store_data_cleaned.csv", mode='w', index=False)
               
        return df
   
    def convert_product_weights(self, df, column_name):
        
        print('FUNCTION CALLED: CONVERT_PRODUCT_WEIGHTS')
        
        # Replace unit 'ml' with 'g' as 1ml = 1g:
        df[column_name] = df[column_name].str.replace('ml', 'g')     
        # Slice out the numerical data:
        numeric_values = df[column_name].str.extract('(\d+\.?\d*)').astype(float)
        units = df[column_name].str.extract('([a-zA-Z]+)')        
        # Unit coversion:
        mask = units[0] == 'g'
        numeric_values.loc[mask] *= 0.001  # Apply the conversion factor to grams        
        df[column_name] = numeric_values

        return df
    
    def clean_products_data(self, df):
        
        print('FUNCTION CALLED: CLEAN_PRODUCTS_DATA')
        
        df.to_csv("products_data_original.csv", mode='w', index=False)
        
        df.to_csv("products_original.csv", mode='w', index=False)
        df = df.drop(columns='Unnamed: 0', axis=1, errors = 'coerce')
        df.reset_index(drop=True)
        df.dropna(how='any', inplace=True)
        df['date_added'] = pd.to_datetime(df['date_added'], errors='ignore')
        
        df.to_csv("products_data_cleaned.csv", mode='w', index=False)
        
        return df
    
    def clean_orders_data(self, df):
        
        print('FUNCTION CALLED: CLEAN_ORDERS_DATA')
        
        df.to_csv("orders_data_original.csv", mode='w', index=False)
        
        df = df.drop(columns=['level_0', 'index', 'first_name', 'last_name', '1'], axis=1, errors = 'coerce') 
        df.dropna(how='any', inplace=True)
        df.reset_index(drop=True)
        #df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
        
        df.to_csv("orders_data_cleaned.csv", mode='w', index=False)
        
        return df

    def clean_dates_data(self, df):
        
        print('FUNCTION CALLED: CLEAN_DATES_DATA')
        
        df.to_csv("dates_data_original.csv", mode='w', index=False)
        
        df.dropna(how='any', inplace=True)
        df['month'] = pd.to_numeric(df['month'], errors='coerce', downcast='integer').astype('Int64')
        df['year'] = pd.to_numeric(df['year'], errors='coerce', downcast='integer').astype('Int64')
        df['day'] = pd.to_numeric(df['day'], errors='coerce', downcast='integer').astype('Int64')
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='%H:%M:%S', errors='coerce')
        df.reset_index(drop=True)
        
        df.to_csv("dates_data_cleaned.csv", mode='w', index=False)
        
        return df

            
  










