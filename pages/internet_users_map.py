import streamlit as st
import plotly.express as px
from loader import df


def internet_users_map():
    st.title('2020 Internet Users Map')

    df_2020 = df[(df['Year'] == 2020) & (df['Code'] != 'Region')]
    mini_count = df_2020['No. of Internet Users'].min()
    fig = px.choropleth(df_2020,
                        locations='Code',
                        color='No. of Internet Users',
                        hover_name='Entity',
                        color_continuous_scale='YlGnBu',
                        range_color=(mini_count, 1000000000))

    fig.update_layout(
        title_text='Number of Internet Users in 2020',
        coloraxis_colorbar=dict(
            title='Number of Internet Users',
            dtick=50000000))

    st.plotly_chart(fig)

    st.write("""### Analysis\nThis choropleth map shows the number of internet users per country for the year 2020.""")

if __name__ == '__main__':
    internet_users_map()