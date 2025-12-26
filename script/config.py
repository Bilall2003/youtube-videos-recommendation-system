import pandas as pd
import os
from sqlalchemy import create_engine 
from urllib.parse import quote_plus


DB_USERNAME="your user_name"
DB_PASSWORD="your password"
DB_HOST="your host"
DB_NAME="your dbms name"

PASSWORD=quote_plus(DB_PASSWORD)

ENGINE = create_engine(
   "create your connection Here"
)

CSV_FILE_PATH=r"your file path"

TABLE_NAME="your table name"
