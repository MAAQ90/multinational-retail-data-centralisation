import database_utils
import data_extraction
import data_cleaning

# **************
# INITIALISATION
# **************

my_instance 	= database_utils.DatabaseConnector()
my_data_extract = data_extraction.DataExtractor()
my_data_clean   = data_cleaning.DataCleaning()


db_cred		= my_instance.read_db_creds('db_creds.yaml')
db_engine 	= my_instance.init_db_engine(db_cred)
table_name 	= my_instance.list_db_tables(db_engine)

print(f'table_name: {table_name}')

# *********
# USER DATA
# *********

# EXTRACT

df_userdata	= my_data_extract.read_rds_table(db_engine, table_name[1])

print(df_userdata.info())
print(df_userdata.head())

# CLEAN

df_userdata	= my_data_clean.clean_user_data(df_userdata)

# OUTPUT

print(df_userdata.info())
print(df_userdata.head())

my_instance.upload_to_db(df_userdata, 'dim_users', db_engine)

exit()

# *********
# CARD DATA 
# *********

df_carddata	= my_data_extract.retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
print(df_carddata.head())

# T4_S3 CLEAN df_carddata

# ***********
# STORES DATA
# ***********

number_of_stores = my_data_extract.list_number_of_stores()
print(f'number of stores:{number_of_stores}')

# T5_S3 DF storedata

# T5_S4 CLEAN df_storedata

# T5_S4 UPLOAD df_storedata in dim_store_details

# *************
# PRODUCTS DATA
# *************

df_productsdata = my_data_ext.extract_from_s3()
print(df_productsdata)

# T6_S2 CLEAN convert_product_weight

# T6_S3 CLEAN clean_products_data

# T6_S4 UPLOAD sales_data using upload_to_db

