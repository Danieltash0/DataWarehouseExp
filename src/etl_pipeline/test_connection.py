from sqlalchemy import create_engine, text
from etl_pipeline.db_config import DB_CONFIG

MYSQL_URL = (
    f"mysql+pymysql://{DB_CONFIG['user']}:"
    f"{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/"
    f"{DB_CONFIG['database']}"
)

def test_connection():
    try:
        engine = create_engine(MYSQL_URL)

        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("Database connection successful")
            print("Test query result:", result.scalar())

    except Exception as e:
        print("Database connection failed")
        print(e)


if __name__ == "__main__":
    test_connection()
