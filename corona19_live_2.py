country_df.loc[country_df['new_case'] < 0, 'new_case'] = 0. 
fig = px.scatter_geo(country_df, locations="country", locationmode='country names', 
        color="new_case", size='new_case', 
        hover_name="country", hover_data=['confirmed', 'fatalities'], 
        range_color= [0, country_df['new_case'].max()],
         projection="natural earth", animation_frame="date",
          title='COVID-19: Daily NEW cases over Time', color_continuous_scale="portland") 
fig.show()

