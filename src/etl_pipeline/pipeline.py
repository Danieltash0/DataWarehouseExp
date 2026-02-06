
from json import load
from etl_pipeline.extractor import extract_raw_data
from etl_pipeline.transformer import (transform_data, build_dim_student, build_dim_subject, build_dim_family, build_dim_school)
from etl_pipeline.loader import (load_table)

def run_pipeline():
    print("Starting ETL pipeline")
    # Extract 
    raw_df = extract_raw_data()
    
    # Transform
    clean_df = transform_data(raw_df)
    
    load_table(build_dim_student(clean_df), "dim_student")
    load_table(build_dim_subject(clean_df), "dim_subject")
    load_table(build_dim_family(clean_df), "dim_family")
    load_table(build_dim_school(clean_df), "dim_school")

    load_table(clean_df, "fact_student_performance")

print("ETL pipeline completed")
if __name__ == "__main__":
        run_pipeline()

