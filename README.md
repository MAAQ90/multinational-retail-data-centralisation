# Multinational Retail Data Centralistaion

## Table of contents:
1. About
2. Data contents and sources
3. Usage instructions
4. File structure
5. License information

## 1. About

This project assumes sales data of a multinational organisation spread across different sources, which analysis difficult for the business. Therefore, it aims to centralise all the data in a single open-source database.

It was carried out in 3 ETL phases:

**Phase 1: Data (E)xtraction from different sources**

In this phase, the data was extracted using various python-based tools:

- YAML: Reads credentials from YAML format file;

- psycopg2: Connects to the PostgreSQL remote database;

- SQLAlchemy: The software library is used to connect to various database systems and execute SQL queries to extract data, and its 'create_engine' function is used in establishing a connection to a database;

- requests: This library helps in making HTTP requests;

- tabula: This library extracts the tables from PDFs into pandas dataframes;

- boto3: Allows the user to interact with the Amazon Web Services (AWS) like S3 for data extraction;

- concurrent.futures: This library helps in parallelization during the extraction process;

- pandas: Helps in establishing dataframe of the extracted data.

**Phase 2: Data (T)ransformation (cleaning, reformatting, etc)**

The transformation phase is the most important, where it is used to clean and uniformly reformat the data, before loading it to the target destination.

- pandas: Play the vital role in cleaning process of the data, e.g., clearing out any 'null' data rows, dropping unnecessary columns, correcting the date/time formats, writing outputs to csv using 'to_csv()' for immediate inspection of data, etc.

**Phase 3: Data (L)oading (into centralised database)**

After the tranformation phase, the data is uploaded to the target database(s) or a centralised database, where it can readily be analysed. The following python libraries are reused from the extraction phase, to help connect with the desired database(s):

- YAML;
 
- psycopg2;

- SQLAlchemy.

## 2. Data contents and sources

The contents and source of each data category is given below:

**1. Users data:**
* Contents: Name; Date of Birth; Company; Email; Address; Country, Country code, Phone number, Join date, User UUID
* Source: AWS Cloud (Postgres Database)
 
**2. Payment card data:**
* Contents: Card number; Expiry data; Provider; Payment date
* Source: AWS S3 (PDF document)

**3. Stores data:**
* Contents: Address; Geographic coordinates (Lat, Long); Locality; Staff numbers; Type; Country code; Continent
* Source: restful-API

**4. Products data:**
* Contents: Product name; Price; Weight; Weight class; Category; EAN; Date added; UUID; Availabilty; Code
* Source: AWS S3

**5. Orders data:**
* Contents: Date UUID; User UUID; Card number; Store code; Product code; Product quantity
* Source: AWS Cloud (Postgres Database)

