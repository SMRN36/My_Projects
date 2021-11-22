from logging import info
import pickle
import streamlit as st



model = pickle.load(open("spam.pkl", 'rb'))
feature_extraction = pickle.load(open("feature.pkl", 'rb'))

def main():
    st.title("SPAM DETECTION WEB APP")
    st.subheader("Built with streamlit and Python")
    Enter = st.text_input("Enter Text")
    if st.button("Predict"):
        data = [Enter]
        input_features = feature_extraction.transform(data)
        prediction = model.predict(input_features)
        result = prediction[0]
        if(result == 1):
            st.success("NOT SPAM")
        else:
            st.error("SPAM")
            



main()