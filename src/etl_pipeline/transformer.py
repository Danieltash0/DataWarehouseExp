# -----------------------------
# Constants
# -----------------------------
BOOLEAN_COLS = [
    "schoolsup", "famsup", "paid", "activities",
    "nursery", "higher", "internet", "romantic"
]


# -----------------------------
# Transform raw data
# -----------------------------
def transform_data(raw_df):
    df = raw_df.copy()

    for col in BOOLEAN_COLS:
        if col in df.columns:
            df[col] = (
                df[col].str.lower().map({"yes": 1, "no": 0}).astype("Int64")
            )
        else:
            print(f"Warning: Column '{col}' not found, skipping")

    return df


# -----------------------------
# Dimension builders
# -----------------------------
def build_dim_student(df):
    return (
        df[["sex", "age", "address", "guardian", "romantic"]].drop_duplicates().reset_index(drop=True)
    )


def build_dim_subject(df):
    return (
        df[["subject_name"]].drop_duplicates().reset_index(drop=True)
    )


def build_dim_family(df):
    return (
        df[[
            "famsize", "Pstatus", "Medu", "Fedu",
            "Mjob", "Fjob", "famrel", "famsup"
        ]].drop_duplicates().rename(columns={"Pstatus": "pstatus"}).reset_index(drop=True)
    )


def build_dim_school(df):
    return (
        df[[
            "school", "reason", "schoolsup", "paid",
            "activities", "nursery", "higher", "internet"
        ]].drop_duplicates().rename(columns={
            "school": "school_code",
            "reason": "reason"
        }).reset_index(drop=True)
    )
