import pandas as pd
from sqlalchemy import create_engine, text
from etl_pipeline.db_config import DB_CONFIG

MYSQL_URL = (
    f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

engine = create_engine(MYSQL_URL, echo=False, pool_pre_ping=True, future=True)

# -----------------------------
# Generic loader for any table
# -----------------------------
def load_table(df, table_name, unique_cols=None):
    """
    Load a DataFrame into a MySQL table, inserting only new rows.
    :param df: DataFrame to load
    :param table_name: target table name
    :param unique_cols: list of columns to check for duplicates (optional)
    """
    if df.empty:
        print(f"⚠️ DataFrame for {table_name} is empty. Skipping load.")
        return

    df = df.drop_duplicates()
    print(f"Loading {len(df)} rows into {table_name}")

    if unique_cols:
        # Read existing rows based on unique_cols
        existing_df = pd.read_sql(f"SELECT {', '.join(unique_cols)} FROM {table_name}", engine)
        # Filter only new rows
        df = df.merge(existing_df, how="left", indicator=True, on=unique_cols)
        df = df[df["_merge"] == "left_only"].drop(columns="_merge")

        if df.empty:
            print(f"⚠️ No new rows to insert into {table_name}")
            return

    df.to_sql(
        table_name,
        con=engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=500
    )

    print(f"✅ Finished loading {table_name}")

# -----------------------------
# Load fact table safely
# -----------------------------
def load_fact_student_performance(df):
    """
    Build the fact_student_performance table with foreign keys.
    """
    print("Preparing fact_student_performance table...")

    # Load dimension tables
    dim_student = pd.read_sql("SELECT * FROM dim_student", engine)
    dim_family  = pd.read_sql("SELECT * FROM dim_family", engine)
    dim_school  = pd.read_sql("SELECT * FROM dim_school", engine)
    dim_subject = pd.read_sql("SELECT * FROM dim_subject", engine)

    fact_df = df.copy()

    fact_df = fact_df.rename(columns={"school": "school_code"})
    # Merge to get student_id
    fact_df = fact_df.merge(
        dim_student,
        on=['sex','age','address','guardian','romantic'],
        how='left'
    )

    # Merge to get family_id
    fact_df = fact_df.merge(
        dim_family,
        left_on=['famsize','pstatus','medu','fedu','mjob','fjob','famrel','famsup'],
        right_on=['famsize','pstatus','medu','fedu','mjob','fjob','famrel','famsup'],
        how='left'
    )

    # Merge to get school_id
    fact_df = fact_df.merge(
        dim_school,
        left_on=['school_code','reason','schoolsup','paid','activities','nursery','higher','internet'],
        right_on=['school_code','reason','schoolsup','paid','activities','nursery','higher','internet'],
        how='left'
    )

    # Merge to get subject_id
    fact_df = fact_df.merge(
        dim_subject,
        on='subject_name',
        how='left'
    )

    # Select only the columns needed for fact table
    fact_final = fact_df[[
        'student_id', 'family_id', 'school_id', 'subject_id',
        'traveltime', 'studytime', 'failures', 'freetime', 'goout',
        'dalc', 'walc', 'health', 'absences', 'g1', 'g2', 'g3'
    ]]

    # Load fact table
    load_table(fact_final, "fact_student_performance")
