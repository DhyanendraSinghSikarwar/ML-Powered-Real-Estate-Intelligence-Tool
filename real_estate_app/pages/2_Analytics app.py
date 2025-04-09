import streamlit as st
import pandas as pd
import numpy as np
import pickle
import ast
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

st.set_page_config(page_title='Gurugram Real state	')

st.title('Analytics')

st.header("Sector Price per Sqft Geomap")
new_df = pd.read_csv('datasets/data_viz1.csv')

group_df = new_df.groupby('sector').agg({col: 'mean' for col in new_df.select_dtypes(
	include=np.number).columns})[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']]

fig = px.scatter_mapbox(group_df, lat = 'latitude', lon ='longitude', color='price_per_sqft', 
	size='built_up_area', color_continuous_scale=px.colors.cyclical.IceFire,
	zoom=10, mapbox_style = 'open-street-map', width=1200, height= 700, hover_name=group_df.index)

st.plotly_chart(fig, use_container_width=True)

##########  Word Cloud   ################
st.header('Features WordCloud')

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

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8), facecolor=None)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
fig.tight_layout(pad=0)
st.pyplot(fig)

##########  Plots   ################
st.header('Area vs Price')

property_type = st.selectbox('Select Property Type', ['All', 'flat', 'house'])

if property_type == 'All':
	
	fig1 = px.scatter(new_df, x="built_up_area", y="price", color="bedRoom", title="Area Vs Price" )

elif property_type == 'flat':
	
	fig1 = px.scatter(new_df[new_df['property_type']=='flat'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price" )

else:
	fig1 = px.scatter(new_df[new_df['property_type']=='house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price" )
st.plotly_chart(fig1, use_container_width=True)


##########  Plots   ################
st.header('BHK Pie Chart')

selector_options = new_df['sector'].unique().tolist()
selector_options.insert(0, 'overall')

selected_sector = st.selectbox('Select Sector', selector_options)

if selected_sector == 'overall':
	fig2 = px.pie(new_df, names='bedRoom')
else:
	fig2 = px.pie(new_df[new_df['sector']==selected_sector], names='bedRoom')
st.plotly_chart(fig2, use_container_width=True)


##########  Plots   ################
st.header('Side by Side BHK price comparison')
temp_df = new_df.copy()
sector_selected = sorted(temp_df['sector'].unique().tolist())
sector_selected.insert(0, "All Sectors")
sector_name_received = st.selectbox('Sector', sector_selected, index=0)
if not (sector_name_received == "All Sectors"):
    temp_df = temp_df[temp_df['sector'] == sector_name_received]

fig3 = px.box(temp_df[temp_df['bedRoom']<=4], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig3, use_container_width=True)


##########  Plots   ################
st.header('Side by Side Distplot for property type')

fig4 = plt.figure(figsize=(10,4))

sns.kdeplot(data=new_df[new_df['property_type']=='house']['price'], label='House')
sns.kdeplot(data=new_df[new_df['property_type']=='flat']['price'], label='Flat')
plt.legend()
st.pyplot(fig4)