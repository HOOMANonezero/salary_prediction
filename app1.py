import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('xgbpipef.joblib')
st.title('Computrt science field salary prediction in 2025')
st.write("""### We need some information to predict the salary""")

countries = (
'United States of America',
'Germany',
'Ukraine',
'United Kingdom of Great Britain and Northern Ireland' ,
'India',                                                    
'France',
'Canada',                                                   
'Brazil',                                                   
'Poland' ,                                                  
'Netherlands',                                              
'Spain',                                                   
'Italy',                                                    
'Australia',                                                
'Sweden',                                                   
'Switzerland',                                              
'Austria',                                                  
'Czech Republic',                                           
'Russian Federation',                                       
'Norway',                                                   
'Israel',                                                   
'Turkey',                                                   
'Denmark',                                                  
'Belgium',                                                  
'Portugal',                                                 
'Romania',                                                  
'Finland',                                                  
'Mexico',                                                   
'South Africa',                                             
'Hungary',                                                  
'Greece',                                                   
'New Zealand',                                              
'Pakistan',                                                 
'Argentina',                                                
'Iran, Islamic Republic of...',                             
'Ireland'         

)

education = (
    "Less than a Bachelors",
    "Bachelor’s degree",
    "Master’s degree" , 
    "PHD"
)

Employment = (
    'Employed, full-time'
)

DevType = (
    'AI scientist',
    'Site_Developer',
    'IT scientist'
)

Age = (
    '35-44 years old', '45-54 years old', '25-34 years old',
       '55-64 years old', '18-24 years old', '65 years or older',
       'Under 18 years old'
)


country = st.selectbox("Country", countries)
education = st.selectbox("Education Level", education)
expericence = st.slider("Years of Experience", 0, 50, 3)
Employment = Employment
DevType = st.selectbox('DevType',DevType)
Age = st.selectbox('Age',Age)

columns = ['Country', 'EdLevel', 'YearsCodePro','Employment','DevType','Age']

ok = st.button("Calculate Salary")
if ok:
    X_new = np.array([country,education,expericence,Employment,DevType,Age])
    X_new_df = pd.DataFrame([X_new], columns = columns)
    salary = model.predict(X_new_df)
    
    st.subheader(f"The estimated salary is ${salary[0]:.2f}")\

