import streamlit as st
import pandas as pd
import joblib

# Load pre-trained model
@st.cache_data(persist=True)
def load_model(model_path):
    model = joblib.load(model_path)
    return model

# Streamlit UI
def main():
    st.title('Diabetes Prediction App')
    st.write('Enter patient details to predict diabetes')

    # User input for prediction
    st.subheader('Enter Patient Details:')
    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=3, step=1)
    glucose = st.number_input('Glucose', min_value=0, max_value=200, value=117, step=1)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=150, value=72, step=1)
    skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, value=23, step=1)
    insulin = st.number_input('Insulin', min_value=0, max_value=900, value=30, step=1)
    bmi = st.number_input('BMI', min_value=0.0, max_value=100.0, value=32.0, step=0.1)
    diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.3725, step=0.0001)
    age = st.number_input('Age', min_value=0, max_value=120, value=29, step=1)

    # Prepare user input for prediction
    input_data = pd.DataFrame({
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [skin_thickness],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [diabetes_pedigree],
        "Age": [age]
    })

    # Make prediction
    model = load_model("C:/Users/sahil/OneDrive/Desktop/Diabetes prediction/diabetes_prediction_model.pkl")
    if st.button('Predict'):
        prediction = model.predict(input_data)
        result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"
        st.success(f'Prediction: {result}')

if __name__ == '__main__':
    main()
