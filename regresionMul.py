import streamlit as st 
from sklearn.linear_model import LinearRegression
import pandas as pd 
from sklearn.metrics import r2_score,mean_squared_error
import openpyxl

#Titulo para el app
st.title('Regresion Lineal Multiple con Streamlit')
#Elegir archivo a subir
archivo_subido = st.file_uploader("Selecciona un archivo: Excel o CSV", type=["csv", "xlsx"])
try:
    #VEr Archivo
    if archivo_subido is not None:
        extension = archivo_subido.name.split('.')[-1]
        if extension == 'csv':
            df = pd.read_csv('archivo_subido')
            st.write('Haz subido un archivo Excel')
            st.dataframe(df)

        elif extension == 'xlsx':
            df = pd.read_excel('archivo_subido')
            st.write('Haz subido un archivo CSV')
            st.dataframe(df)
            
        else:
            st.write('Tipo de archivo no soportado')
except Exception as e:
    st.error(f'Error al leer el archivo: {e}')
