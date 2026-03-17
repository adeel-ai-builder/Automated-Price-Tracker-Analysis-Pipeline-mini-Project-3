from sqlalchemy import create_engine, text
engine=create_engine("sqlite:///price_tracker.db")

def create_table():
    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS prices (
            title TEXT,
            price REAL,
            date TEXT,
            UNIQUE(title, date)
        )
        """))

def save_to_db(df):
    df.to_sql("prices", engine, if_exists="append", index=False)