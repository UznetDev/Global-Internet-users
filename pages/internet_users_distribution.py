import streamlit as st
import matplotlib.pyplot as plt
from loader import df


def internet_users_distribution():
    st.title('Internet Users(%) Distribution')

    plt.figure(figsize=(10, 6))
    plt.hist(df['Internet Users(%)'], bins=30, alpha=0.7)
    plt.title('Internet Users(%) Distribution')
    plt.xlabel('Internet Users(%)')
    plt.ylabel('Frequency')
    plt.grid(True)
    st.pyplot(plt)

    st.write("""
        ### Analysis
        This histogram shows the distribution of internet users percentage across different regions.
    """)


if __name__ == '__main__':
    internet_users_distribution()