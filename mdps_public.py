# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:20:18 2024

@author: Lenovo
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

#sidebar for navigate
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons = ['activity','heart'],
                           default_index = 0)

#Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using Ml')
    #getting the input data from the users
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregrancies = st.text_input("Number of Pregrancies")
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPredigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input("Age of the person")
    
    
    

    #code for Prediction
    diab_diagnosis =''
    
    #creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregrancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_prediction[0]==1):
            diab_diagnosis ='The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is not Diabetic'
    st.success(diab_diagnosis)
    #getting the input data from the users
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregrancies = st.text_input("Number of Pregrancies")
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPredigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input("Age of the person")
    

if(selected == 'Heart Disease Prediction using Ml'):
  #page title
  st.title('Heart Disease Prediction using Ml')


  #getting the input data from the users
  col1, col2, col3 = st.columns(3)
  with col1:
      age = st.text_input("Your age: ")
  with col2:
      sex = st.text_input('Your sex: ')
  with col3:
      cp = st.text_input('Enter your cp: ')
  with col1:
      Trestbps = st.text_input('Enter your TrestBPS: ')
  with col2:
      chol = st.text_input('Enter your Chloestrol level: ')
  with col3:
      BMI = st.text_input('Enter your BMI Value: ')
  with col1:
      FBS = st.text_input('Enter the FBS value: ')
  with col2:
      Restecg = st.text_input('Enter your Restecg: ')
  with col3:
      thalach = st.text_input('Enter your thalach: ')
  with col1:
      exang = st.text_input('Enter your Exang: ')
  with col2:
      oldpeak = st.text_input('Enter your oldpeak: ')
  with col3:
      oldpeak = st.text_input('Enter your oldpeak: ')
  with col1:
      slope = st.text_input('Enter your slope: ')
  with col2:
      ca = st.text_input('Enter your ca value: ')
  with col3:
      thal = st.text_input('Enter your thal value: ')
      
      #code for Prediction
      heart_diagnosis =''

#crating a button for prediction
 if st.button('Heart Diseases Test Result'):
     heart_prediction = heart_model.predict([[Age, Sex, Cp, Trestbps, Chol, Fbs, Restcg, Thalach, Exang, Oldpeak, Slope, Ca, Thal]])
     if (heart_prediction[0]==1):
         heart_diagnosis ='The Person is has high rate of Heart Disease'
     else:
         heart_diagnosis = 'The Person has not high rate of Heart Disease'
 st.success(heart_diagnosis)
 #getting the input data from the users
 col1, col2, col3 = st.columns(3)
  with col1:
      age = st.text_input("Your age: ")
  with col2:
      sex = st.text_input('Your sex: ')
  with col3:
      cp = st.text_input('Enter your cp: ')
  with col1:
      Trestbps = st.text_input('Enter your TrestBPS: ')
  with col2:
      chol = st.text_input('Enter your Chloestrol level: ')
  with col3:
      BMI = st.text_input('Enter your BMI Value: ')
  with col1:
      FBS = st.text_input('Enter the FBS value: ')
  with col2:
      Restecg = st.text_input('Enter your Restecg: ')
  with col3:
      thalach = st.text_input('Enter your thalach: ')
  with col1:
      exang = st.text_input('Enter your Exang: ')
  with col2:
      oldpeak = st.text_input('Enter your oldpeak: ')
  with col3:
      oldpeak = st.text_input('Enter your oldpeak: ')
  with col1:
      slope = st.text_input('Enter your slope: ')
  with col2:
      ca = st.text_input('Enter your ca value: ')
  with col3:
      thal = st.text_input('Enter your thal value: ')
 

      
      #creating a button for Prediction
      if st.button('Heart Diseases Result'):
          diab_prediction = diabetes_model.predict([[Age, Sex, p, trestbps, chol, ]])
          if (diab_prediction[0]==1):
              diab_diagnosis ='The Person is Diabetic'
          else:
              diab_diagnosis = 'The Person is not Diabetic'
      st.success(diab_diagnosis)
      #getting the input data from the users
      col1, col2, col3 = st.columns(3)
      with col1:
          Pregrancies = st.text_input("Number of Pregrancies")
      with col2:
          Glucose = st.text_input('Glucose level')
      with col3:
          BloodPressure = st.text_input('Blood Pressure Value')
      with col1:
          SkinThickness = st.text_input('Skin Thickness Value')
      with col2:
          Insulin = st.text_input('Insulin Level')
      with col3:
          BMI = st.text_input('BMI Value')
      with col1:
          DiabetesPredigreeFunction = st.text_input('Diabetes Pedigree Function value')
      with col2:
          Age = st.text_input("Age of the person")
  
  