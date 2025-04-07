import streamlit as st
import pandas as pd
import numpy as np
import pickle
import ast
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title='Gurugram Real state	')

st.title('Analytics')

new_df = pd.read_csv('datasets/data_viz1.csv')

group_df = new_df.groupby('sector').agg({col: 'mean' for col in new_df.select_dtypes(
	include=np.number).columns})[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']]

fig = px.scatter_mapbox(group_df, lat = 'latitude', lon ='longitude', color='price_per_sqft', 
	size='built_up_area', color_continuous_scale=px.colors.cyclical.IceFire,
	zoom=10, mapbox_style = 'open-street-map', width=1200, height= 700, hover_name=group_df.index)

st.plotly_chart(fig, use_container_width=True)

##########  Word Cloud   ################
wordcloud_df = pd.read_csv('datasets/wordcloud.csv')

# sector
sectors = sorted(wordcloud_df['sector'].unique().tolist())
sectors.insert(0, "All Sectors")  # Add "All Sectors" option at the beginning

# Set index=0 to select "All Sectors" by default
sector_name = st.selectbox('Sector', sectors, index=0)

if not (sector_name == "All Sectors"):
    wordcloud_df = wordcloud_df[wordcloud_df['sector'] == sector_name]


main =[]
# Loop through each entry in the 'features' column (after dropping NaN values)
for item in wordcloud_df['features'].dropna().apply(ast.literal_eval):
    main.extend(item)

feature_text = ' '.join(main)

plt.rcParams["font.family"] = "Arial"

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8), facecolor=None)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
fig.tight_layout(pad=0)
st.pyplot(fig)
