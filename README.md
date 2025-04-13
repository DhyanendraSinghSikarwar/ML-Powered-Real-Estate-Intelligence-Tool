# ML-Powered-Real-Estate-Intelligence-Tool 

## Project Overview  
This project aims to predict real estate prices in Gurugram using machine learning. It leverages property data scraped from **99acres.com**, followed by comprehensive data preprocessing, exploratory analysis (EDA), and feature engineering. The system includes a **price prediction module** as its first core feature (with 2 additional features to be detailed in future updates).  

---

## Process Flow  
### 1. Data Collection & Preprocessing  
- **Source**: Extracted structured real estate data (location, area, BHK, amenities, etc.) from 99acres.com.  
- **Cleaning**: Handled missing values, duplicates, and irrelevant entries.  
- **Outlier Treatment**: Identified and mitigated outliers using IQR and domain-specific thresholds.  

### 2. Exploratory Data Analysis (EDA)  
- Analyzed distributions of key variables (price, area, BHK).  
- Visualized correlations between features and target (price).  
- Identified trends in premium pricing for specific locations/amenities.  

### 3. Feature Engineering  
- Created new features (e.g., price/sqft, proximity to landmarks).  
- Encoded categorical variables using **One-Hot Encoding**, **Label Encoding**, and **Target Encoding**.  
- Applied **PCA** for dimensionality reduction in specific model pipelines.  

### 4. Model Development    
- Developed  models for different applications.  

---


## Feature 1: Price Prediction System  
### Technical Implementation
1. **Model Selection**:
 -  Model Development for Price Prediction  
    - Key Steps:  
        - **Algorithm Comparison**: Tested 11 regression models (Linear Regression, SVR, Random Forest, XGBoost, etc.).  
        - **Encoding Strategy Evaluation**: Compared performance across 3 encoding techniques.  
        - **Hyperparameter Tuning**: Optimized Random Forest using **GridSearchCV** with 5-fold cross-validation.  

  
### Model Performance Summary  
| **Encoding Type**         | **Best Model**   | **R² Score** | **MAE**  |  
|---------------------------|------------------|--------------|----------|  
| Ordinal Encoding          | Random Forest    | 0.867        | 0.541    |  
| One-Hot Encoding          | Extra Trees      | 0.885        | 0.481    |  
| One-Hot Encoding + PCA    | MLP              | 0.866        | 0.530    |  
| **Target Encoding**       | **Random Forest**| **0.901**    | **0.116**|  

**Final Model**: Random Forest Regressor with **Target Encoding** demonstrated the highest accuracy (R² = 0.901) and lowest error (MAE = 0.116).  

1. **Selected Model**:  
   - Random Forest outperformed other models due to its robustness to non-linear relationships and feature interactions.  
   - Target Encoding preserved categorical information while minimizing overfitting.  

2. **Hyperparameter Tuning**:  
   - Optimized via `GridSearchCV` with 5-fold cross-validation.  
   - Best parameters:  
     ```python  
     {'n_estimators': 100, 'max_depth': 30,  
      'min_samples_split': 0.1, 'min_samples_leaf': 0.1,  
      'max_features': 'sqrt'}  
     ```  
   - Achieved cross-validated R² score: **0.660**.  

3. **Pipeline**:  
   - Integrated preprocessing, encoding, and model inference into a single `sklearn.pipeline.Pipeline`.  
   - Ensures reproducibility and ease of deployment.  

### Outcome  
- Users can input property features (e.g., location, area, BHK) to receive instant price predictions.  
- System accuracy: **90.1%** (R²) with **<0.12 MAE** error margin.  

---

## Feature 2: Interactive Analytics Dashboard  
This module provides actionable insights into Gurugram’s real estate market through dynamic visualizations.it includes:  

### 1. **Sector-Wise Geomap**  
- **Visualization**: Interactive map plotting property prices per sqft across sectors.  
- **Features**:  
  - **Color Gradient**: Reflects `price_per_sqft` (darker = higher price).  
  - **Bubble Size**: Represents `built_up_area`.  
  - **Data**: Aggregated sector-level averages for price, area, and coordinates.  
  - **Tool**: `Plotly` integrated with OpenStreetMap.  
- **Use Case**: Identify premium sectors and compare area-price relationships geographically.  

![Geomap Demo](link_to_gif_or_image_if_available)  

---

### 2. **Amenities Word Cloud**  
- **Functionality**: Generates a word cloud of frequently listed property amenities.  
- **Filters**:  
  - Sector-specific or aggregated ("All Sectors").  
  - Derived from cleaned `features` column (e.g., "swimming pool", "parking").  
- **Insight**: Highlights sought-after amenities influencing pricing in specific areas.  

![Word Cloud Demo](link_to_image)  

---

### 3. **Interactive Plots**  
#### A. **Area vs Price Analysis**  
- **Scatter Plot**: Explore how `built_up_area` correlates with `price`.  
- **Filters**:  
  - Property type: `All`, `Flat`, or `House`.  
  - Color-coded by `BHK` configuration.  
- **Use Case**: Detect outliers and trends for specific property types.  

#### B. **BHK Distribution Pie Chart**  
- **Visualization**: Sector-wise or overall distribution of BHK configurations.  
- **Filters**:  
  - Sector selector (e.g., Sector 50, Sector 70).  
- **Insight**: Understand demand for 1BHK vs 3BHK units in specific regions.  

#### C. **BHK Price Comparison**  
- **Box Plot**: Compare price ranges across 1BHK to 4BHK configurations.  
- **Filters**:  
  - Sector-specific or aggregated view.  
- **Use Case**: Evaluate affordability by BHK size.  

#### D. **Property Type Price Distribution**  
- **KDE Plot**: Side-by-side density distributions for `Flat` and `House` prices.  
- **Insight**: Compare pricing trends between property types.  

---

## Technical Implementation  
- **Tools**: Streamlit (frontend), Plotly (interactive plots), WordCloud, Matplotlib/Seaborn.  
- **Data Pipeline**:  
  1. Load preprocessed CSV datasets (`data_viz1.csv`, `wordcloud.csv`).  
  2. Dynamically filter data based on user inputs (sector, property type).  
  3. Render visualizations in real-time using cached data.  

---

## How to Use the Dashboard  
1. **Launch**: Run `streamlit run analytics.py` (or your script name).  
2. **Navigate**:  
   - Select sectors/property types using dropdowns.  
   - Hover over map/plots for detailed metrics.  
3. **Interpret**: Use visualizations to guide investment decisions or market analysis.  

---

## Key Insights Delivered  
- **Premium Sectors**: Identify high-price/sqft zones (e.g., Golf Course Road).  
- **Amenity Trends**: Swimming pools and gyms dominate luxury properties.  
- **BHK Demand**: 3BHK units are most prevalent in suburban sectors.  

---  

## Feature 3: Hybrid Property Recommendation System  
This intelligent system suggests properties using a **weighted combination of 3 key factors**: amenities, pricing, and location proximity. Built for personalized recommendations, it helps users discover properties aligned with their priorities.

---

### Key Components  
1. **Facility-Based Recommendations**  
   - **TF-IDF Vectorization**: Convert amenities (pool, gym, security) into numerical vectors  
   - **Cosine Similarity**: Match properties with similar facility profiles  
   - *Example*: Properties with "swimming pool + clubhouse" recommended together  

2. **Price-Based Recommendations**  
   - **Feature Engineering**: Extract BHK configurations, area ranges, and price brackets  
   - **Standard Scaling**: Normalize numerical features for fair comparison  
   - **Similarity Metric**: Identify properties with comparable price/sqft ratios  

3. **Location-Based Recommendations**  
   - **Proximity Matrix**: Calculate distances to 1,070+ landmarks (schools, metro stations, hospitals)  
   - **Distance Normalization**: Standardize values using Z-score scaling  
   - **Location Similarity**: Prioritize properties in similar geographic profiles  

---

### Hybrid Algorithm  
**Combined Score** = `30×Facility Similarity` + `20×Price Similarity` + `8×Location Similarity`  

```python
# Weighted similarity calculation
cosine_sim_matrix = 30*cosine_sim1 + 20*cosine_sim2 + 8*cosine_sim3
```

---

### Implementation Workflow  
1. **Data Preparation**  
   - Clean and standardize 246 property records  
   - Process nested JSON structures in `PriceDetails` and `LocationAdvantages`  

2. **Feature Engineering**  
   - One-Hot Encode property types (Apartment/Villa/Independent Floor)  
   - Extract numerical ranges from price/area fields (e.g., "1.2-1.8 Cr" → [1.2, 1.8])  

3. **Similarity Computation**  
   - Generate 3 similarity matrices (246x246 dimensions each)  
   - Combine using customizable weights for scenario-specific recommendations  

4. **Recommendation Generation**  
   ```python
   def recommend_properties(property_name):
       # Hybrid similarity calculation
       combined_scores = get_weighted_similarity(property_name)
       return top 5 properties with highest combined scores
   ```

---

### System Capabilities  
- **Context-Aware Suggestions**:  
  - Luxury properties → Higher facility similarity weight  
  - Budget properties → Higher price similarity weight  
- **Dynamic Weight Adjustment**: Easily modify factor priorities via weight parameters  
- **Cold Start Handling**: Works with partial data through matrix factorization  

---

### Sample Output  
**Input**: "DLF The Camellias" (Premium Property)  
**Recommendations**:  
1. DLF The Crest (Facility Score: 0.92 | Price Score: 0.88)  
2. M3M Golf Hills (Location Score: 0.95 | Facility Score: 0.89)  
3. Ireo Victory Valley (Price Score: 0.91 | Location Score: 0.84)  

---

*Data Source: 99acres.com | Models: Scikit-Learn, Pandas*  
  
