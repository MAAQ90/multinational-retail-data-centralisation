import yaml
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import inspect

class DatabaseConnector:

  # contruct class
    def __init__(self):
        pass

    def read_db_creds(self, filename):
        with open(filename, "r") as db_creds:
            return yaml.safe_load(db_creds)

    def init_db_engine(self, cred):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{cred['RDS_USER']}:{cred['RDS_PASSWORD']}@{cred['RDS_HOST']}:{cred['RDS_PORT']}/{cred['RDS_DATABASE']}")
        return engine

    def list_db_tables(self, engine):
        inspector = inspect(engine)
        return inspector.get_table_names()

    def upload_to_db(self, df, table_name, engine):
        df.to_sql(table_name, engine, if_exists='replace', index=False)