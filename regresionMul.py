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
            df = pd.read_csv(archivo_subido)
            st.write('Haz subido un archivo CSV')
            st.dataframe(df)

        elif extension == 'xlsx':
            df = pd.read_excel(archivo_subido)
            st.write('Haz subido un archivo Excel')
            st.dataframe(df)

        else:
            st.write('Tipo de archivo no soportado')
        
        #Opciones Adicionales
        st.write('### Informacion adicional del DataFrame:')
        st.write(f'Numero de Filas:  {df.shape[0]}')
        st.write(f'Numero de Columnas:  {df.shape[1]}')
        #Selecionando variables no numericas
        no_numericas = df.select_dtypes(include='object').columns
        st.write(no_numericas)
        #Seleccionar variable Objetivo o Target
        target = st.selectbox('Selecciona la Variable Objetivo o Target :', df.columns)
        st.write(target)

        #Selecionar Variables independientes o predictoras
        predictoras = st.multiselect('Selecionar variables predictoras o independientes:' , df.columns)
        st.write(predictoras)

except Exception as e:
    st.error(f'Error al leer el archivo: {e}')
