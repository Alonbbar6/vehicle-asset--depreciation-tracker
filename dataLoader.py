# dataLoader.py

import pandas as pd
from sqlalchemy import create_engine

def load_data():
    # 1. Load CSV
    df = pd.read_csv('/Users/user/Desktop/zoilas_project/Snippet.csv', encoding='latin1')

    # 2. Create connection string
    db_user = "root"
    db_password = "Pocholo10"
    db_host = "localhost"
    db_name = "asset_tracker"

    # 3. SQLAlchemy connection string
    engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

    # 4. Upload data to MySQL
    df.to_sql('assets', con=engine, if_exists='replace', index=False)

    print("✅ Data imported successfully!")
    return df


