import streamlit as st
import pandas as pd

# Title of the app
st.title("🎈 My new app")

# Welcome text
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

# CSV data for widgets
# List of CSV files to be loaded from GitHub (add links to your files)
files = [
    "comparison_of_sale_and_rent_market_activity_by_city.csv",
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
    url = f"https://raw.githubusercontent.com/elgrassa/Data-engineering-professional-certificate/main/dbt_data_for_widgets_in_csv/{file}"
    st.subheader(f"Displaying: {file}")
    data = pd.read_csv(url)  # Load the data from the CSV URL
    st.dataframe(data)  # Display data as a table in the app