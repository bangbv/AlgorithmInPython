import pandas as pd
import os


data_list = pd.read_json(os.path.join("/Users/bangbui/workspace/TSandLanguage/data/processed/", 'TS_Dataset_2.jsonl'), lines=True)
print(f"data_list: {data_list}")