#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "Fully_Cleaned_BSS_Retail_Data.csv"
data = pd.read_csv(file_path)

# Set the title of the dashboard
st.title("Interactive Sales Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
price_range = st.sidebar.slider("Select Price Range", 
                                 min_value=float(data['price'].min()), 
                                 max_value=float(data['price'].max()), 
                                 value=(float(data['price'].min()), float(data['price'].max())))
selected_sku = st.sidebar.multiselect("Select SKU", options=data['sku'].unique(), default=data['sku'].unique())

# Apply filters
filtered_data = data[(data['price'] >= price_range[0]) & (data['price'] <= price_range[1])]
if selected_sku:
    filtered_data = filtered_data[filtered_data['sku'].isin(selected_sku)]

# Visualization 1: Scatter plot (Ad Spend vs Sales)
st.subheader("Ad Spend vs Sales")
fig1, ax1 = plt.subplots()
sns.scatterplot(x='adspend', y='sales', data=filtered_data, ax=ax1)
ax1.set_title("Ad Spend vs Sales")
st.pyplot(fig1)

# Visualization 2: Box plot (Profit Distribution by SKU)
st.subheader("Profit Distribution by SKU")
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.boxplot(x='sku', y='profit', data=filtered_data, ax=ax2)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
ax2.set_title("Profit Distribution by SKU")
st.pyplot(fig2)

# Visualization 3: Correlation Heatmap
st.subheader("Correlation Heatmap")
fig3, ax3 = plt.subplots(figsize=(10, 8))
corr_matrix = filtered_data.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True, ax=ax3)
ax3.set_title("Correlation Heatmap")
st.pyplot(fig3)

# Display filtered dataset
st.subheader("Filtered Dataset")
st.write(filtered_data)


# In[ ]:




