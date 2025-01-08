def generate_seasonal_data(df):
    seasonal_data = df.groupby('season').agg({
        'cnt': 'mean'
    }).reset_index()

    season = ['Spring', 'Summer', 'Fall', 'Winter']
    for i in range(4):
        seasonal_data['season'].replace(i + 1, season[i], inplace=True)
    
    return seasonal_data

def generate_hourly_data(df):
    hourly_data = df.groupby('hr').agg({
        'cnt': 'mean'
    }).reset_index()

    return hourly_data

def date_num_to_string(start_month, end_month):
    months = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    
    start_month = months[start_month - 1]
    end_month = months[end_month - 1]
    
    return start_month, end_month