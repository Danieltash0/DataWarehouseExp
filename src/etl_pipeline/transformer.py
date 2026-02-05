def transform_data(raw_df):
    binary_cols = ["schoolsup", "famsup", "paid", "activities", "nursery",
        "higher", "internet", "romantic"]
    
    for col in binary_cols:
        raw_df[col] = raw_df[col].map({"yes": True, "no": False})

        return raw_df
    
def build_dim_student(raw_df):
    return raw_df[["sex", "age", "address", "guardian", "romantic"]].drop_duplicates()

def build_dim_subject(raw_df):
    return raw_df[["subject_name"]].drop_duplicates()

def build_dim_family(raw_df):
    dim_family = raw_df[["famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "famrel", "famsup"]].drop_duplicates()
    return dim_family.rename(columns={"Pstatus": "pstatus"})

def build_dim_school(raw_df):
    dim = raw_df[["school", "reason", "schoolsup", "paid", "activities", "nursery", "higher", "internet"]].drop_duplicates()
    return dim.rename(columns={"reason": "school_reason", "schoolsup": "school_support", "paid": "paid_classes", "activities": "extracurricular_activities", "nursery": "nursery_attendance"})
