import streamlit as st
import matplotlib.pyplot as plt
from loader import df

def broadband_subscription():
    st.title('Average Broadband Subscription Over Selected Years')

    sort_df = df[df['Year'].isin([1990, 1995, 2000, 2005, 2010])]
    broadband = sort_df.groupby('Year')['Broadband Subscription'].mean()

    plt.figure(figsize=(10, 6))
    broadband.plot(kind='bar', color='y')
    plt.title('Average Broadband Subscription for Selected Years')
    plt.xlabel('Year')
    plt.ylabel('Average Broadband Subscription')
    plt.grid(True)
    st.pyplot(plt)

    st.write("""
        ### Analysis
        This bar chart shows the average broadband subscription for selected years.
    """)

if __name__ == '__main__':
    broadband_subscription()