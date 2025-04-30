import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("🎈 Polish Flats and Houses Rent and Sales Market Analysis")

# Welcome text
st.write("""
    Welcome to the Polish Flats and Houses Rent and Sales Market Analysis App! 
    This app provides detailed insights into the rent and sales market across various cities in Poland. 
    You can analyze data related to market activity, room counts, price percentiles, and much more.

    Widgets are provided for easy navigation and allow you to sort and filter the data interactively. 
    Additionally, various visualizations are available to help you better understand trends and relationships in the data.
    """)

st.write("""
    **Note:** 
    All prices are in polish Zloty (95 percentile - means pnly 5 percent of data is higher).
    Data for some cities, such as Bydgoszcz, Gdynia, and Szczecin, is limited or missing due to their smaller real estate markets. 
    As a result, there may be gaps or differences in the graphs for these cities.
""")

# CSV data for widgets
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
    
    # Title of widget
    st.subheader(f"📊 {display_name_formatted}")

    # Load data from the CSV URL
    data = pd.read_csv(url)
    st.dataframe(data)
    
    # Add graphs based on percentiles (Median and 95th Percentile)
    if 'median_price' in data.columns and 'percentile_95_price' in data.columns:
        # Create a plot for Median and 95th Percentile
        st.write(f"### Median vs 95th Percentile for {display_name_formatted}")
        
        # Line plot for Percentile comparison
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=data, x="city", y="median_price", label="Median Price", ax=ax)
        sns.lineplot(data=data, x="city", y="percentile_95_price", label="95th Percentile Price", ax=ax)
        
        ax.set_title(f"Price Comparison by City: Median vs 95th Percentile")
        ax.set_xlabel("City")
        ax.set_ylabel("Price")
        ax.legend()
        
        st.pyplot(fig)
    
    # Additional visualization based on "total_listings" and "average_price" (if available)
    if 'total_listings' in data.columns and 'average_price' in data.columns:
        st.write(f"### Total Listings vs Average Price for {display_name_formatted}")
        
        # Bar chart for listings and average price
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=data, x="city", y="total_listings", color="blue", label="Total Listings", ax=ax)
        sns.barplot(data=data, x="city", y="average_price", color="orange", label="Average Price", ax=ax)
        
        ax.set_title(f"Market Activity by City: Listings and Average Price")
        ax.set_xlabel("City")
        ax.set_ylabel("Values")
        ax.legend()
        
        st.pyplot(fig)

    # Line Chart for Rent vs Sale Price Comparison (for rent-related files)
    if 'rent_price' in data.columns and 'sale_price' in data.columns:
        st.write(f"### Rent vs Sale Price Comparison for {display_name_formatted}")
        
        # Line plot for Rent vs Sale Price
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=data, x="city", y="rent_price", label="Rent Price", ax=ax)
        sns.lineplot(data=data, x="city", y="sale_price", label="Sale Price", ax=ax)
        
        ax.set_title(f"Rent vs Sale Price Comparison")
        ax.set_xlabel("City")
        ax.set_ylabel("Price")
        ax.legend()
        
        st.pyplot(fig)