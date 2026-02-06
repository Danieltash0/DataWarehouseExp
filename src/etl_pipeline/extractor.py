import pandas as pd

def extract_raw_data():
    mat_df = pd.read_csv("data/raw/student-mat.csv", sep=";")
    por_df = pd.read_csv("data/raw/student-por.csv", sep=";")

    mat_df["subject_name"] = "Math"
    por_df["subject_name"] = "Portuguese"

    raw_df = pd.concat([mat_df, por_df], ignore_index=True)
   # print(raw_df.columns.tolist())
    return raw_df
    
