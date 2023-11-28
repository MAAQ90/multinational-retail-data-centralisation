# Multinational Retail Data Centralistaion

## Table of contents:
1. About
2. Data contents and sources
3. Usage instructions
4. File structure
5. License information

## 1. About

This project assumes sales data of a multinational organisation spread across different sources. This made analysis difficult.

So, in the first phase, the data was extracted rom those sources, cleaned, and centralised in a single SQL database.

In the second phase

## 2. Data contents and sources

The contents and source of each data category is given below:


**1. Users data:**
* Contents: Name; Date of Birth; Company; Email; Address
* Source: AWS Cloud (Postgres Database)
 
**2. Payment card data:**
* Contents: Card number; Expiry data; Provider; Payment date
* Source: AWS S3 (PDF document)

**3. Stores data:**
* Contents: Address; Coordinates (Lat, Long); Locality; Staff numbers; Type; Country code; Continent

