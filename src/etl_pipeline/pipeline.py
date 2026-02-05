from json import load
from extractor import extract_raw_data
from transformer import (transform_data, build_dim_student, build_dim_subject, build_dim_family, build_dim_school)
from loader import (load_dimension, load_fact)

def run_pipeline():
    # Extract
    raw_df = extract_raw_data()
    
    # Transform
    clean_df = transform_data(raw_df)
    
    load_dimension(build_dim_student(clean_df), "dim_student")
    load_dimension(build_dim_subject(clean_df), "dim_subject")
    load_dimension(build_dim_family(clean_df), "dim_family")
    load_dimension(build_dim_school(clean_df), "dim_school")

    load_fact(clean_df)

    if __name__ == "__main__":
        run_pipeline()