import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://localhost:27017")

DATABASE_NAME = 'aps'
COLLECTION_NAME = 'sensor'

DATA_FILE_PATH = 'aps_failure_training_set1.csv'

if __name__ == '__main__':
    df = pd.read_csv(DATA_FILE_PATH)
    print(f'rows and columns: {df.shape}')
    print(df.head(2))
    # Convert DataFrame to JSON to insert into MongoDB
    df.reset_index(drop=True, inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

