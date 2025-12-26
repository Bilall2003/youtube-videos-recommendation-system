import pandas as pd
import os
import time
import logging
from sqlalchemy import types,inspect
from config import ENGINE,TABLE_NAME

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Data_Loading:
    """Load CSV data and store it to MySQL"""

    def __init__(self, engine=ENGINE):
        self.engine = engine

    def load_csv_to_sql(self, file_path):
        """Load CSV, convert NaN → None, and store to MySQL"""
        if not os.path.exists(file_path):
            logging.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"{file_path} does not exist")

        try:
            df = pd.read_csv(file_path)
            df = df.where(pd.notnull(df), None)  # Convert NaN → None
            
            rename_col=["title","channel_title"]
            df.rename(columns={rename_col[0]:"Video_title",rename_col[1]:"channel_name"},inplace=True)

            inspector = inspect(ENGINE)  #inspect database

            if not inspector.has_table("your table name"):  # check if table exist or not  
                df.to_sql(
                    name="your table name",
                    con=ENGINE,
                    if_exists="fail",
                    index=False
                )
                logging.info("Table created and data loaded in MYSQL")
            else:
                logging.info("Table already exists. Skipping load.")

            logging.info(f"Data stored successfully in table '{TABLE_NAME}' at {time.asctime()}")
            return df

        except Exception as e:
            logging.error(f"Error while loading CSV to SQL: {e}")
            raise
