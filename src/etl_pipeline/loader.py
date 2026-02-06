from sqlalchemy import create_engine
from etl_pipeline.db_config import DB_CONFIG

MYSQL_URL = {
    f"mysql+pymysql://{DB_CONFIG['user']}:"
    f"{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:"
    f"{DB_CONFIG['port']}/"
    f"{DB_CONFIG['database']}"
}
engine = create_engine(MYSQL_URL, echo=False, pool_pre_ping=True)

def load_table(df, table_name):
    with engine.begin() as conn:
     df.to_sql(table_name, conn, if_exists='append', index=False, method='multi', chunksize=500)

'''
def load_dimension(raw_df, table_name):
    raw_df.to_sql(table_name, engine, if_exists='append', index=False)

def load_fact(raw_df):
    raw_df.to_sql("fact_student_performance", engine, if_exists='append', index=False)
'''
print("Writing to MySQL database at " + MYSQL_URL)
