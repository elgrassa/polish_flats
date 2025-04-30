import streamlit as st
import pandas as pd

# Title of the app
st.title("🎈 Polish flats and houses rent and sales market analysis")

# Welcome text
st.write(    """
    Welcome to the Polish Flats and Houses Rent and Sales Market Analysis App! 
    This app provides detailed insights into the rent and sales market across various cities in Poland. 
    You can analyze data related to market activity, room counts, price percentiles, and much more.

    Widgets are provided for easy navigation and allow you to sort and filter the data interactively. 
    Additionally, various visualizations are available to help you better understand trends and relationships in the data.
    """)

# CSV data for widgets
# List of CSV files to be loaded from GitHub (add links to your files)
files = [
    "comparison_of_sale_and_rent_market_activity_by_city.csv",
    "rent_market_activity_by_rooms_city_price_percentiles.csv",
    "sale_market_activity_by_rooms_city_price_percentiles.csv",
    "rent_market_activity_by_city_with_average_price_and_price_percentiles.csv",
    "rent_market_activity_by_city_with_average_rent_and_price_percentiles.csv",
    "rent_price_dynamics_by_city.csv",
    "sale_market_activity_by_city_with_median_and_price_percentiles.csv",
    "sale_market_activity_by_city_with_price_percentiles_and_average.csv",
    "sale_market_listings_count_by_city_with_price_percentiles.csv",
    "top_15_cities_by_rental_price_with_percentiles.csv"
]
# Loop through the files and display them
for file in files:
    display_name = file.replace('.csv', '')
    display_name_formatted = display_name.replace('_', ' ')
    url = f"https://raw.githubusercontent.com/elgrassa/Data-engineering-professional-certificate/main/dbt_data_for_widgets_in_csv/{file}"
    st.subheader(f"{display_name_formatted}")
    data = pd.read_csv(url)  
    st.dataframe(data)