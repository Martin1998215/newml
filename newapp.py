


import streamlit as st
import pickle
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open("C:/Users/Dell/Desktop/appml/diabetes_model.sav","rb"))
heart_model = pickle.load(open("C:/Users/Dell/Desktop/appml/heart_model.sav","rb"))


#setup sidebar
with st.sidebar:
    selected = option_menu("Menu List",
    ["Home","Diabetes Analysis","Diabetes Model","Heart Disease Analysis","Heart Model"],
    icons=["house-door","file-bar-graph","activity","file-bar-graph","heart"],
    default_index=0)

st.sidebar.write('''
**AI For Medicine**

Predicitive Modeling

Automating Medical Diagnosis

**Martin Sichibeya**.

''') 


if selected == "Home":
    st.title("Home section")
    st.header("Machine learning")
    st.subheader("Welcome to our ML App")

    st.write("**AI For Medicine ML App**")
    st.write('''
    
    **Here we will make two predictions:**
    1. On Diabetes Dataset
    2. On Heart Disease Dataset 

    ''')


# Add image
    from PIL import Image
    img = Image.open("mlcover.jpg")
    st.write("**Profile Photo**")
    st.image(img,caption="ML Cover Photo")

    with open("mlcover.jpg", "rb") as file:
        
        btn = st.download_button(
             label="Download image",
             data=file,
             file_name="cover.jpg",
             mime="image/jpg"
           )


if selected == "Diabetes Analysis":
    st.title("Diabetes Analysis")
    st.header("show dataset here")


if selected == "Diabetes Model":
    st.header("Diabetes Model")
    st.subheader("Input Features Here..")

    #input features
    pregnancies = st.text_input("Pregnancies")
    glucose = st.text_input("Glucose")
    bp = st.text_input("Blood Pressure")
    skin_t = st.text_input("Skin Thickness")
    insulin = st.text_input("Insulin")
    bmi = st.text_input("BMI")
    pdf = st.text_input("Diabetes Pedigree Function")
    age = st.text_input("Age")


        # Enter button
    if st.button("Enter For Prediction"):
        # make predictions on input data
        diabetes_predict = diabetes_model.predict([[pregnancies,glucose,bp,skin_t,insulin,bmi,pdf,age]])

        # prediction probability
        diabetes_predict_proba = diabetes_model.predict_proba([[pregnancies,glucose,bp,skin_t,insulin,bmi,pdf,age]])
        if diabetes_predict[0] == 1:
            st.subheader("Results")
            st.success("You have Diabetes..")
            st.subheader("Prediction Probability")
            st.write("0 = Not Diabetic; 1 = Diabetic")
            st.write(diabetes_predict_proba)
        else:
            st.subheader("Results")
            st.success("You dont have Diabetes..")
            st.subheader("Prediction Probability")
            st.write("0 = Not Diabetic [%]; 1 = Diabetic [%]")
            st.write(diabetes_predict_proba * 100) 


if selected == "Heart Disease Analysis":
    st.title("Heart Analysis")
    st.header("show dataset here")  


if selected == "Heart Model":
    st.header("Heart Model")
    st.subheader("Input Features Here..")   

    #input features
    age = st.text_input("Age")
    sex = st.text_input("Sex: Male:1, Female:0")
    cpt = st.text_input("Chest Pain Type (4 values)")
    rbp = st.text_input("Resting Blood Pressure")
    sc = st.text_input("Serum Cholestoral in mg/dl")
    fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")
    rer = st.text_input("Rest Electrocardiographic Results")
    mhra = st.text_input("Maximum Heart Rate Achieved")
    eia = st.text_input("Exercise Induced Angina")
    oldpeak = st.text_input("Oldpeak")
    slope = st.text_input("Slope of the peak Exercise")
    numb = st.text_input("Number of Blood Vessels colered by flourosopy")
    thal = st.text_input("Thal: 3 = Normal; 6 = Fixed Defect; 7 = Reversable Defect")  

    if st.button("Enter Button"):


        heart_predict = heart_model.predict([[age,sex,cpt,rbp,sc,fbs,rer,mhra,eia,oldpeak,slope,numb,thal]])

        heart_predict_proba = heart_model.predict_proba([[age,sex,cpt,rbp,sc,fbs,rer,mhra,eia,oldpeak,slope,numb,thal]])


        if heart_predict[0] == 1:
            st.subheader("Results")
            st.success("You have heart disease")
            st.subheader("Predicition Probability")
            st.write("0 = No Heart Disease[%], 1 = Heart Disease [%]")
            st.write(heart_predict_proba * 100)
        else:
            st.subheader("Results")
            st.success("You DONT have heart disease")
            st.subheader("Prediction Probability")
            st.write("0 = No Heart Disease[%], 1 = Heart Disease [%]")
            st.write(heart_predict_proba * 100) 
