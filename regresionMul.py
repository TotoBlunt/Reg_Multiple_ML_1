import streamlit as st 
from sklearn.linear_model import LinearRegression
import pandas as pd 
from sklearn.metrics import r2_score,mean_squared_error

#Titulo para el app
st.title('Regresion Lineal Multiple con Streamlit')
#Elegir archivo a subir
archivo_subido = st.file_uploader("Selecciona un archivo", type=["csv", "xlsx"])

upload_file = st.file_uploader('Sube un archivo CSV', type=['csv'])