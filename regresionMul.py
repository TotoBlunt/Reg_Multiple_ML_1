import streamlit as st 
from sklearn.linear_model import LinearRegression
import pandas as pd 
from sklearn.metrics import r2_score,mean_squared_error

#Titulo para el app
st.title('Regresion Lineal Multiple con Streamlit')
#Elegir archivo a subir
archivo_subido = st.multiselect('Selecciona el tipo de archivo a trabajarar','1 -> CSV','2 -> Excel')
#Subir un archivo
upload_file = st.file_uploader('Sube un archivo CSV', type=['csv'])