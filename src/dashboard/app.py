from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine
from etl_pipeline.db_config import DB_CONFIG

engine = create_engine(
    f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}/{DB_CONFIG['database']}"
)

app = Flask(__name__)

@app.route("/")
def index():
    subject = request.args.get("subject", "Math")

    query = f"""
        SELECT sex, AVG(g3) AS avg_grade
        FROM mart_student_performance
        WHERE subject_name = '{subject}'
        GROUP BY sex;
    """

    df = pd.read_sql(query, engine)
    return render_template("dashboard.html", table=df.to_html(index=False))

if __name__ == "__main__":
    app.run(debug=True)
