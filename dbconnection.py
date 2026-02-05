import pandas as pd
from sqlalchemy import create_engine, text
engine = create_engine(
    "postgresql+psycopg2://username:password@localhost:5432/student_dw"
)

mat_df = pd.read_csv("student-mat.csv", sep=";")
por_df = pd.read_csv("student-por.csv", sep=";")

mat_df["subject_name"] = "Math"
por_df["subject_name"] = "Portuguese"

raw_df = pd.concat([mat_df, por_df], ignore_index=True)
