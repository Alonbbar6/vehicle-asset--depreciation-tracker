from depreciation import create_all_schedules
from dataLoader import load_data


# Load asset data
df_assets = load_data()

# Generate depreciation schedules
df_depreciation = create_all_schedules(df_assets)

# Check the results
print(df_depreciation.head())

# Optionally, save to CSV
df_depreciation.to_csv('depreciation_schedule.csv', index=False)


