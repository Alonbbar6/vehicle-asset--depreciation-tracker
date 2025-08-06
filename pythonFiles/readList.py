# readList.py

from db_functions import list_assets

if __name__ == "__main__":
    assets_df = list_assets()
    print(assets_df)
