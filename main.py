#!/usr/bin/env python
# coding: utf-8

import database_utils
import data_extraction
import data_cleaning

# **************
# INITIALISATION
# **************

my_instance 	= database_utils.DatabaseConnector()
my_data_extract = data_extraction.DataExtractor()
my_data_clean   = data_cleaning.DataCleaning()

rds_cred		= my_instance.read_db_creds('rds_creds.yaml')
mydb_cred = my_instance.read_db_creds('mydb_creds.yaml')

'''
# *************
# T3: USER DATA
# *************

print(f'\nPROCESSING: USER DATA\n')

# --------------------------
# EXTRACT FROM REMOTE SOURCE
# --------------------------

print('initiating remote engine')
db_engine = my_instance.init_db_engine(rds_cred)
db_engine.connect()

print('extracting data')
table_name = my_instance.list_db_tables(db_engine)
#print(f'table_name: {table_name}')
df_userdata = my_data_extract.read_rds_table(db_engine, table_name[1])

print('closing remote engine')
db_engine.dispose()

#print(df_userdata.head())

# --------------------
# CLEAN EXTRACTED DATA
# --------------------

print('cleaning extracted data')
df_userdata = my_data_clean.clean_user_data(df_userdata)

#print(df_userdata.head())

# ------------------------
# UPLOAD TO LOCAL DATABASE
# ------------------------

print('initiating local engine')
db_engine = my_instance.init_db_engine(mydb_cred)
db_engine.connect()

print('uploading to local database')
my_instance.upload_to_db(df_userdata, 'dim_users', db_engine)

print('closing local engine')
db_engine.dispose()

#exit()

# *************
# T4: CARD DATA 
# *************

print('\nPROCESSING: CARD DATA\n')

# --------------------------
# EXTRACT FROM REMOTE SOURCE
# --------------------------

print('initiating remote engine')
db_engine = my_instance.init_db_engine(rds_cred)
db_engine.connect()

print('extracting card data')
df_carddata	= my_data_extract.retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
print(df_carddata.info())
print(df_carddata.describe())

print('closing remote engine')
db_engine.dispose()

# --------------------
# CLEAN EXTRACTED DATA
# --------------------

print('cleaning extracted data')
df_carddata = my_data_clean.clean_card_data(df_carddata)

# ------------------------
# UPLOAD TO LOCAL DATABASE
# ------------------------

print('initiating local engine')
db_engine = my_instance.init_db_engine(mydb_cred)
db_engine.connect()

print('uploading to local database')
my_instance.upload_to_db(df_carddata, 'dim_card_details', db_engine)

print('closing local engine')
db_engine.dispose()

print(df_carddata.info())
print(df_carddata.describe())

#exit()



# ***************
# T5: STORES DATA
# ***************

print('\nPROCESSING: STORES DATA\n')

# --------------------------
# EXTRACT FROM REMOTE SOURCE
# --------------------------

print('initiating remote engine')
db_engine = my_instance.init_db_engine(rds_cred)
db_engine.connect()

print('extracting stores data')
number_of_stores = my_data_extract.list_number_of_stores()
print(f'number of stores:{number_of_stores}')

df_storedata = my_data_extract.retrieve_stores_data(number_of_stores)
print(df_storedata.info())
print(df_storedata.describe())

print('closing remote engine')
db_engine.dispose()

# --------------------
# CLEAN EXTRACTED DATA
# --------------------

print('cleaning extracted data')
df_storedata = my_data_clean.clean_store_data(df_storedata)

# ------------------------
# UPLOAD TO LOCAL DATABASE
# ------------------------

print('initiating local engine')
db_engine = my_instance.init_db_engine(mydb_cred)
db_engine.connect()

print('uploading to local database')
my_instance.upload_to_db(df_storedata, 'dim_store_details', db_engine)

print('closing local engine')
db_engine.dispose()

'''

# *****************
# T6: PRODUCTS DATA
# *****************
'''
print(f'\nPROCESSING: PRODUCT DETAILS\n')

# --------------------------
# EXTRACT FROM REMOTE SOURCE
# --------------------------

print('initiating remote engine')
db_engine = my_instance.init_db_engine(rds_cred)
db_engine.connect()

print('extracting data')
df_productdetails = my_data_extract.extract_from_s3()
print(df_productdetails)

print('closing remote engine')
db_engine.dispose()

# --------------------
# CLEAN EXTRACTED DATA
# --------------------

# T6_S2 CLEAN convert_product_weight

print('cleaning extracted data')

# T6_S3 CLEAN clean_products_data

df_productdetails = my_data_clean.convert_product_weights(df_productdetails, 'weight')
df_productdetails = my_data_clean.clean_products_data(df_productdetails)
print(df_productdetails)

# ------------------------
# UPLOAD TO LOCAL DATABASE
# ------------------------

print('initiating local engine')
db_engine = my_instance.init_db_engine(mydb_cred)
db_engine.connect()

print('uploading to local database')
my_instance.upload_to_db(df_productdetails, 'dim_products', db_engine)

print('closing local engine')
db_engine.dispose()
'''


# **********
# T7: ORDERS
# **********
'''
print(f'\nPROCESSING: ORDERS DATA\n')

# --------------------------
# EXTRACT FROM REMOTE SOURCE
# --------------------------

print('initiating remote engine')
db_engine = my_instance.init_db_engine(rds_cred)
db_engine.connect()

print('extracting data')
table_name = my_instance.list_db_tables(db_engine)
#print(f'table_name: {table_name}')
df_ordersdata = my_data_extract.read_rds_table(db_engine, table_name[2])

print('closing remote engine')
db_engine.dispose()

print(df_ordersdata.head())
print(df_ordersdata.tail())
print('******************************************************************')
print(df_ordersdata.info())
print('******************************************************************')
print(df_ordersdata.describe())
print('******************************************************************')

# --------------------
# CLEAN EXTRACTED DATA
# --------------------

print('cleaning extracted data')

df_ordersdata = my_data_clean.clean_orders_data(df_ordersdata)
print(df_ordersdata)

# ------------------------
# UPLOAD TO LOCAL DATABASE
# ------------------------

print('initiating local engine')
db_engine = my_instance.init_db_engine(mydb_cred)
db_engine.connect()

print('uploading to local database')
my_instance.upload_to_db(df_ordersdata, 'orders_table', db_engine)

print('closing local engine')
db_engine.dispose()
'''


# ***************
# T7: EVENTS DATA
# ***************

# --------------------------
# EXTRACT FROM REMOTE SOURCE
# --------------------------

print('initiating remote engine')
db_engine = my_instance.init_db_engine(rds_cred)
db_engine.connect()

print('extracting data')
df_datesdata = my_data_extract.extract_dates_data()

print('closing remote engine')
db_engine.dispose()

print(df_datesdata)

print('******************************************************************')
print(df_datesdata.info())
print('******************************************************************')
print(df_datesdata.describe())
print('******************************************************************')

# --------------------
# CLEAN EXTRACTED DATA
# --------------------

print('cleaning extracted data')

df_datesdata = my_data_clean.clean_dates_data(df_datesdata)
print(df_datesdata)

print('******************************************************************')
print(df_datesdata.info())
print('******************************************************************')
print(df_datesdata.describe())
print('******************************************************************')

# ------------------------
# UPLOAD TO LOCAL DATABASE
# ------------------------

print('initiating local engine')
db_engine = my_instance.init_db_engine(mydb_cred)
db_engine.connect()

print('uploading to local database')
my_instance.upload_to_db(df_datesdata, 'dim_date_times', db_engine)

print('closing local engine')
db_engine.dispose()
