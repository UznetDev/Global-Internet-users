import streamlit as st
import matplotlib.pyplot as plt
from loader import df

def cellular_vs_internet():
    st.title('Cellular Subscription vs Internet Users(%)')

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Cellular Subscription'], df['Internet Users(%)'], alpha=0.5)
    plt.title('Cellular Subscription vs Internet Users(%)')
    plt.xlabel('Cellular Subscription')
    plt.ylabel('Internet Users(%)')
    plt.grid(True)
    st.pyplot(plt)

    st.write("""
        ### Analysis
        This scatter plot shows the relationship between cellular subscriptions and the percentage of internet users.
    """)


if __name__ == '__main__':
    cellular_vs_internet()
