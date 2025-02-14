import os
import sys
import json
import pandas as pd
import numpy as np
import pymongo

from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")

'''A Python package that provides trusted SSL certificates.To Ensures secure SSL/TLS connections to MongoDB.'''
import certifi
ca=certifi.where()


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    """In mongodb we insert data of type JSON so we have to first convert the DF into JSON then push it into the MongoDb"""
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True) #Removes the old index that is creataed by default when you make it a df
            records=list(json.loads(data.T.to_json()).values()) #to convert the df into json
            return records #All Records Are Converted Into List Of JSON(Each record is in KEY-VALUE PAIRS)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            mongo_client = pymongo.MongoClient(MONGO_DB_URL) #creating connection with the mongodb
            database = mongo_client[database]               #Selects The given database from the mongodb databases
            database[collection].insert_many(records)       #Inserts all records into the MongoDB collection
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

        
if __name__=='__main__':
    FILE_PATH="NetworkData\phisingData.csv"
    DATABASE="DivyamTalwar"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)
        


