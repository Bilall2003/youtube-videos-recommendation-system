import numpy as np
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s - line:%(lineno)d - %(funcName)s"
)


class Clean:
    
    def process(self,df):
        
        if df is None:
            
            logging.error("Empty Dataframe..........")
            raise ValueError("Dataframe is empty or none......")
        
        try:
         
            null_val=df.isnull().sum()/len(df)*100  #detect 570 null values in description column
            dup_val=df.duplicated().sum()/len(df)*100 # detect 48 duplicate rows
            
            df_clean = df.dropna().drop_duplicates().reset_index(drop=True)
            
            null_drop=df_clean.isnull().sum()/len(df)*100
            dupl_drop=df_clean.duplicated().sum()/len(df)*100 
            
            logging.info(f"Data cleaning completed. Nulls before: {null_val.sum():.2f}%, after: {null_drop.sum():.2f}%")
            logging.info(f"Duplicates before: {dup_val}, after: {dupl_drop}")
            
            return df_clean
        
        except Exception as e:
            
            logging.error(f"Something Went Wrong{e}")
            raise
   
