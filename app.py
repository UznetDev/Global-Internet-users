import streamlit as st
from loader import navigate_page
from pages import *


st.sidebar.title('Navigation')
page = st.sidebar.selectbox('Select a page: ', navigate_page)

if page == 'Home':
    st.title('Data Visualization Web App')
    st.write("""
        ## Overview
        This web application provides various visualizations based on the dataset containing information about cellular subscriptions, internet users, and broadband subscriptions.

        ### Pages
        - Cellular vs Internet Users: Scatter plot showing the relationship between cellular subscriptions and internet users percentage.
        - Internet Users Distribution: Histogram showing the distribution of internet users percentage.
        - Broadband Subscription: Bar chart showing the average broadband subscription for selected years.
        - Internet Users Timeline: Line plot showing the count of countries that started using the internet each year.
        - 2020 Internet Users Map: Choropleth map showing the number of internet users per country for the year 2020.

        Navigate through the pages using the sidebar to explore the visualizations.""")

elif page == 'Cellular vs Internet Users':
    cellular_vs_internet()

elif page == 'Internet Users Distribution':
    internet_users_distribution()

elif page == 'Broadband Subscription':
    broadband_subscription()

elif page == 'Internet Users Timeline':
    internet_users_timeline()

elif page == '2020 Internet Users Map':
    internet_users_map()
