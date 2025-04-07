import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title='Gurugram Real state	')

st.title('Analytics')

new_df = pd.read_csv('datasets/data_viz1.csv')

group_df = new_df.groupby('sector').agg({col: 'mean' for col in new_df.select_dtypes(
	include=np.number).columns})[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']]

fig = px.scatter_mapbox(group_df, lat = 'latitude', lon ='longitude', color='price_per_sqft', 
	size='built_up_area', color_continuous_scale=px.colors.cyclical.IceFire,
	zoom=10, mapbox_style = 'open-street-map', width=1200, height= 700, hover_name=group_df.index)

st.plotly_chart(fig, use_container_width=True)