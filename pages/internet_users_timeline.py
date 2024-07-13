import streamlit as st
import seaborn as sns
from loader import df


def internet_users_timeline():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title('Timeline of Internet Users Adoption')


    on_world = df[(df['Code'] != 'Region') & (df['Entity'] != 'World') & (df['No. of Internet Users'] > 0)]
    mini_year = on_world.groupby('Entity')[['Year']].agg('min')
    year_count = mini_year[['Year']].value_counts().reset_index(name='count')

    sns.relplot(x='Year', y='count', data=year_count, kind='line')
    st.pyplot()

    st.write("""
        ### Analysis
        This line plot shows the count of countries that started using the internet each year.
    """)

if __name__ == '__main__':
    internet_users_timeline()