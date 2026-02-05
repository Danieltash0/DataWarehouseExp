from sqlalchemy import create_engine
engine = create_engine("sqlite:///data/database/Student_Alc_DB.db")

def load_dimension(raw_df, table_name):
    raw_df.to_sql(table_name, engine, if_exists='append', index=False)

def load_fact(raw_df):
    raw_df.to_sql("fact_student_performance", engine, if_exists='append', index=False)