import pandas as pd

def create_schedule(row):
    """
    Create a depreciation schedule for one asset using straight-line method.
    """
    years = int(row['Vida útil estimada (años)'])
    cost = row['Costo de adquisición']
    residual = row['Valor residual']
    annual_dep = (cost - residual) / years
    start_year = int(row['Año de adquisición'])
    
    schedule = []
    book_value = cost
    
    for i in range(years):
        year = start_year + i
        end_book_value = max(book_value - annual_dep, residual)
        schedule.append({
            'ID del vehículo': row['ID del vehículo'],
            'Año': year,
            'Valor inicial': book_value,
            'Depreciación anual': annual_dep,
            'Valor final': end_book_value
        })
        book_value = end_book_value
        
    return pd.DataFrame(schedule)

def create_all_schedules(df):
    """
    Generate depreciation schedules for all assets in the DataFrame.
    """
    schedules = []
    for _, row in df.iterrows():
        schedules.append(create_schedule(row))
    return pd.concat(schedules, ignore_index=True)


