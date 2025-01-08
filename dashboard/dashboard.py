import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from function import generate_seasonal_data, generate_hourly_data, date_num_to_string

df = pd.read_csv("dashboard/final_cleaned_data.csv")

# Side bar
with st.sidebar:
    st.write("Choose the period to be analyzed")
    col1, col2 = st.columns(2)
    
    with col1:
        start_year = st.selectbox("Starting Year", [2011, 2012])
        start_month = st.selectbox("Starting Month", df["mnth"].unique())
    
    with col2:
        end_year = st.selectbox("Ending Year", [2011, 2012], index=1)
        end_month = st.selectbox("Ending Month", df["mnth"].unique(), index=11)
        
# Filtering dataframe by period 
main_df = df[
    (df["yr"] >= start_year%2011) & (df["mnth"] >= start_month) & 
    (df["yr"] <= end_year%2011) & (df["mnth"] <= end_month)
]

start_month, end_month = date_num_to_string(start_month, end_month)

# Main content
st.header("Bike Sharing Analysis")
st.subheader(f"Period {start_month} {start_year} - {end_month} {end_year}")
col1, col2 = st.columns(2)

with col1:
    st.write(f"Number of columns: {main_df.shape[1]} columns")
with col2:
    st.write(f"Number of rows: {main_df.shape[0]} rows")

tab1, tab2, tab3 = st.tabs(["Data", "Visualizations", "Correlation"])

with tab1:
    st.dataframe(main_df.head(20))
    
    with st.expander("Column Description"):
        st.write(
            """
            - **instant:** Record index
            - **dteday:** Date
            - **season:** Season 
                - 1: Spring
                - 2: Summer
                - 3: Fall
                - 4: Winter
            - **yr:** Year 
                - 0: 2011
                - 1: 2012
            - **mnth:** Month (1 to 12)
            - **hr:** Hour (0 to 23)
            - **holiday:** Indicates if the day is a holiday (extracted from [holiday schedule](http://dchr.dc.gov/page/holiday-schedule))
            - **weekday:** Day of the week
            - **workingday:** Indicates if the day is neither a weekend nor a holiday
                - 1: Working day
                - 0: Non-working day

            ### Weather Situation (weathersit):
            - 1: Clear, Few clouds, Partly cloudy
            - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
            - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
            - 4: Heavy Rain + Ice Pellets + Thunderstorm + Mist, Snow + Fog

            ### Normalized Features:
            - **temp:** Temperature in Celsius, normalized by dividing by 41 (max value)
            - **atemp:** Feels-like temperature in Celsius, normalized by dividing by 50 (max value)
            - **hum:** Humidity, normalized by dividing by 100 (max value)
            - **windspeed:** Wind speed, normalized by dividing by 67 (max value)

            ### User Counts:
            - **casual:** Count of casual users
            - **registered:** Count of registered users
            - **cnt:** Total count of rental bikes, including both casual and registered users
            """
        )

    
with tab2:
    # Visualize hourly data
    st.subheader("Hourly Data Analysis")
    hourly_data = generate_hourly_data(main_df)
    
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(x='hr', y='cnt', data=hourly_data)
    plt.title('The Average Bicycle Users Per Hour', pad=20, weight='bold', size=15)
    plt.xlabel('Hour')
    plt.ylabel('Average Bicycle Users')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)
    
    # Visualize seasonal data
    st.subheader("Seasonal Data Analysis")
    seasonal_data = generate_seasonal_data(main_df)
    
    fig = plt.figure(figsize=(8, 4))
    sns.barplot(x='season', y='cnt', data=seasonal_data)
    plt.title('The Average Bicycle Users Per Season', pad=20, weight='bold', size=12)
    plt.xlabel('Season')
    plt.ylabel('Average Bicycle Users')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)
    
with tab3:
    # Correlation analysis
    st.subheader("Correlation Analysis")
    correlation = main_df[['temp', 'hum', 'windspeed', 'cnt']].corr()

    fig = plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
    st.pyplot(fig)
    
st.caption('by Kevin Andreas 2025')
    
