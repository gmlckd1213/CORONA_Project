country_df['date'] = country_df['date'].apply(str)
country_df['confirmed_log1p'] = np.log1p(country_df['confirmed'])
country_df['fatalities_log1p'] = np.log1p(country_df['fatalities'])
fig = px.scatter_geo(country_df, locations="country", locationmode='country names', 
                     color="confirmed", size='confirmed', hover_name="country",
                     hover_data=['confirmed', 'fatalities'], 
                     range_color= [0, country_df['confirmed'].max()],
                     projection="natural earth", animation_frame="date",
                     title='COVID-19: Confirmed cases spread Over Time', 
                     color_continuous_scale="portland") # fig.update(layout_coloraxis_showscale=False) 
fig.show()


