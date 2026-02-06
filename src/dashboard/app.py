import sqlite3
import pandas as pd

conn = sqlite3.connect("data/database/student_dw.db")
clean_df = pd.read_sql("SELECT * FROM fact_student_performance", conn)
