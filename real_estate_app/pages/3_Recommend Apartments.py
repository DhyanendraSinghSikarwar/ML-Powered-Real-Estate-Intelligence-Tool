import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Recommend Apartments")

location_df = pickle.load(open('datasets/location_distance.pkl', 'rb'))
link_df = pickle.load(open('datasets/main_df.pkl', 'rb'))

cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl', 'rb'))

def recommend_properties_with_scores(property_name, top_n=247):
    
    cosine_sim_matrix = 0.5*cosine_sim1 + 0.8*cosine_sim2 + 1*cosine_sim3
    # cosine_sim_matrix = cosine_sim3
    
    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    
    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    
    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()
    
    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })
    
    return recommendations_df


st.title('Select Location and radius')

selected_location = st.selectbox('Location', sorted(location_df.columns.tolist()))

radius = st.number_input('Radius in Kms')

if st.button('Search'):
  result_ser = location_df[location_df[selected_location]<radius*1000][selected_location].sort_values()

  for key, value in result_ser.items():
    st.text(str(key) + " " + str(round(value/1000)) + ' kms')


st.title('Recommend Apartments')

selected_apartment = st.selectbox('Select an appartment', sorted(location_df.index.to_list()))



if st.button('Recommend'):
  recommended_df = recommend_properties_with_scores(selected_apartment)
  recommended_df = recommended_df.merge(link_df, how='left', on='PropertyName')
else:
  recommended_df = pd.DataFrame()

# Convert URLs to clickable HTML
def make_clickable(url, text):
    return f'<a target="_blank" href="{url}">{text}</a>'
if not recommended_df.empty:
  recommended_df['URL'] = recommended_df.apply(lambda x: make_clickable(x['Link'], x['PropertyName']), axis=1)

  recommended_df = recommended_df[['URL','SimilarityScore']].iloc[:5,:]

  st.write(recommended_df.to_html(escape=False), unsafe_allow_html=True)