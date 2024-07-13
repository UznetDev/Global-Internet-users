# Display DataFrame
st.write("First few rows of the dataset")
st.write(df.head())

st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Home", "Scatter Plot", "Histogram", "Bar Plot", "Line Plot", "Choropleth Map"])

# Histogram
st.write("## Internet Users(%) taqsimoti")
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['Internet Users(%)'], bins=30, alpha=0.7)
ax.set_title('Internet Users(%) taqsimoti')
ax.set_xlabel('Internet Users(%)')
ax.set_ylabel('Chastota')
ax.grid(True)
st.pyplot(fig)

# Bar Plot
st.write("## Tanlangan yillar uchun urtacha Broadband Subscription")
selected_years = st.multiselect("Select Years", options=[1990, 1995, 2000, 2005, 2010],
                                default=[1990, 1995, 2000, 2005, 2010])
if selected_years:
    sort_df = df[df['Year'].isin(selected_years)]
    broadband = sort_df.groupby('Year')['Broadband Subscription'].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    broadband.plot(kind='bar', color='y', ax=ax)
    ax.set_title('Tanlangan yillar uchun urtacha Broadband Subscription')
    ax.set_xlabel('Yil')
    ax.set_ylabel('Urtacha Broadband Subscription')
    ax.grid(True)
    st.pyplot(fig)

# Line Plot using Seaborn
st.write("## Year-wise Internet Users Count")
on_world = df[(df['Code'] != 'Region') & (df['Entity'] != 'World') & (df['No. of Internet Users'] > 0)]
mini_year = on_world.groupby('Entity')[['Year']].agg('min')
year_count = mini_year[['Year']].value_counts().reset_index(name='count')
fig = sns.relplot(x='Year',
                  y='count',
                  data=year_count,
                  kind='line')
st.pyplot(fig)

# Choropleth Map using Plotly
st.write("## 2020 chi yil uchun internet foydalanuvchilari soni")
df_2020 = df[(df['Year'] == 2020) & (df['Code'] != 'Region')]
mini_count = df_2020['No. of Internet Users'].min()
fig = px.choropleth(df_2020,
                    locations='Code',
                    color='No. of Internet Users',
                    hover_name='Entity',
                    color_continuous_scale='YlGnBu',
                    range_color=(mini_count, 1000000000))

fig.update_layout(
    title_text='2020 chi yil uchun internet foydalanuvchilari soni',
    coloraxis_colorbar=dict(
        title='Internet foydalanavchilari soni',
        dtick=50000000))

st.plotly_chart(fig)

# from pages.internet_users_map import internet_users_map
# from pages.internet_users_timeline import internet_users_timeline
# from pages.broadband_subscription import broadband_subscription
# from pages.internet_users_distribution import internet_users_distribution
# from pages.cellular_vs_internet import cellular_vs_internet