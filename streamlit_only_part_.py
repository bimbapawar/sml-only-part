# -*- coding: utf-8 -*-
"""streamlit only part .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/182A6_ezgboBUn5h4ZW8_ZU-rX7wqbte9
"""

import streamlit as st

st.title('Identifying links between monsoon variability and different types of grains')
col1, col2, col3 = st.columns((1, 8, 1))
with col2:
    st.text('Rice, Wheat, Pearl Millet, Maize, Barley')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔎 Overview", "📃 Dataset", "📅 Exploratory Data Analysis", "📈 Model Performance", "✏️ References"])


with tab1:
    # overview
    st.markdown("<h5 style='text-align: center; color: #DA0C81;'>Why this topic?</h5>", unsafe_allow_html=True)

    st.write("Studying the links between monsoon variability and different types of grains is crucial for understanding and addressing the intricate relationship between climate patterns and agricultural outcomes. Monsoons play a pivotal role in determining rainfall levels, directly impacting grain production, food security, and economic stability. Investigating these connections allows for the development of informed agricultural strategies, climate change adaptation measures, and effective policies to manage risks and optimize crop yields. This research not only contributes to scientific knowledge about climate-agriculture interactions but also holds practical implications for farmers, policymakers, and stakeholders involved in ensuring food security and sustainable agricultural practices.")

    st.image("Screenshot 2023-11-27 101055.png", width=700)

with tab2:
    # dataset
    st.markdown("<h5 style='text-align: center; color: #DA0C81;'>The Data</h5>", unsafe_allow_html=True)

    st.write("For this investigation, we used an open-source dataset made accessible by Link for the ICRISAT")

    st.markdown("<h5 style='text-align: center; color: #DA0C81;'>Features</h5>", unsafe_allow_html=True)
    st.write("Data Preprocessing steps")
    st.write("Aggregating Data: The data is  merged by comparing  name of the state, name of  district and year using merge function from Pandas Library.")

    st.write("Handling Missing Values: In cases where dataset contained missing values, we addressed this issue by dropping it. Visualization of our dataset is performed using seaborn library.\
    Descriptive Statistics: To summaries the features of data Set , descriptive Statistics is used.\
     Using dataframe.describe(), we were able to fetch the central tendency of the data.\
     Univariate Analysis: This Analysis describes the data distribution across one column. \
     In this paper Annual rainfall column is consider , which highlights, the distribution of rainfall data.")

    st.write("Skewness and Kurtosis: The asymmetry of a probability distribution is measured by its skewness. Kurtosis is a probability distribution's sharpness metric. \
    We compute the skewness and Kurtosis for annual rainfall in this work.\
    Skewness of final_annual: 1.9858183460792491\
    Kurtosis of final_annual: 4.6794278771189575")

    st.write("Bivariate Analysis: Checks the relationship between two variables")

    st.write("Analyzing Variations Across Different States or Years: In this paper , Variations Across different States and Years are visualized using box plot and line plot.")


with tab3:
    col1, col2, col3 = st.columns((1, 3, 1))
    with col1:
        st.write(' ')
    with col2:
       st.image("Screenshot 2023-11-27 101418.png", width=500)

       st.divider()
       st.image("Screenshot 2023-11-27 101418.png", width=500)

    with col3:
        st.write(' ')


with tab4:

    col1, col2, col3 = st.columns((1, 3, 1))
    with col1:
        st.write(' ')
    with col2:
       st.subheader("ROC Curve and Confusion matrix")

       st.text("ROC Curve:")
       st.image("Screenshot 2023-11-27 101556.png", width=500)

       st.divider()

       st.text("Confusion Matrix:")
       st.image("Screenshot 2023-11-27 101517.png", width=500)

    with col3:
        st.write(' ')
