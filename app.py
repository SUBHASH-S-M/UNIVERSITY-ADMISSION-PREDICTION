import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("Admission_predict.pkl","rb")
admis_predicter=pickle.load(pickle_in)
#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def admisssion_chance(GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research,Tancet,GATE):
    prediction=admis_predicter.predict([[GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research,Tancet,GATE]])
    print(prediction)
    return prediction



def main():
    st.title("ADMISSSION PREDICTOR")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">ADMISSION PREDICTION BY SUBHASH ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    GRE_Score = st.text_input("GRE Score","Type Here")
    TOEFL_Score = st.text_input("TOEFL_Score","Type Here")
    University_Rating = st.text_input(",University_Rating","Type Here")
    SOP= st.text_input("SOP","Type Here")
    LOR= st.text_input("lOR","Type Here")
    CGPA= st.text_input("CGPA","Type Here")
    Research= st.text_input("Research","Type Here")
    Tancet= st.text_input("Tancet","Type Here")
    GATE=st.text_input("gate score","Type Here")    
    result="YET TO BE PREDICTED"
    if st.button("Predict"):
        result=admisssion_chance(GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research,Tancet,GATE)
    st.success('THE PROBABILITY TO ADMIT IS IS {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built BY SUBHASH")

if __name__=='__main__':
    main()
    