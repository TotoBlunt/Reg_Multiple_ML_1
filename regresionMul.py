import streamlit as st 
from sklearn.linear_model import LinearRegression
import pandas as pd 
from sklearn.metrics import r2_score,mean_squared_error
import openpyxl

#Titulo para el app
st.title('Regresion Lineal Multiple con Streamlit')
#Elegir archivo a subir
archivo_subido = st.file_uploader("Selecciona un archivo: Excel o CSV", type=["csv", "xlsx"])

#VEr Archivo
if archivo_subido is not None:
    extension = archivo_subido.split('.')[-1]
    if extension == 'csv':
        df = pd.read_csv('archivo_subido')
        st.write(df.head())
    elif extension == 'xlsx':
        df = pd.read_excel('archivo_subido')
        st.write(df.head())
    else:
        st.write('Tipo de archivo no soportado')

