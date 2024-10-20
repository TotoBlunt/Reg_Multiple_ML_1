import streamlit as st 
from sklearn.linear_model import LinearRegression
import pandas as pd 
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split,cross_val_score
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
        st.write('### Variables No numericas')
        no_numericas = df.select_dtypes(include='object').columns
        st.write(no_numericas)
        if no_numericas == 0 :
            df_num = df
            pass
        else:
            df_num = df.drop(list(no_numericas),axis=1)

        st.dataframe(df_num)


        #Seleccionar variable Objetivo o Target
        target = st.selectbox('Selecciona la Variable Objetivo o Target :', df_num.columns)
        st.write(target)

        #Selecionar Variables independientes o predictoras
        predictoras = st.multiselect('Selecionar variables predictoras o independientes:' , df_num.columns)
        st.write(predictoras)

        #Definir variables
        X = df_num[list(predictoras)]
        y = df_num[target]

        #Crear variables de entrenamiento y test
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

        #Crear Modelo
        model_RegL = LinearRegression()
        #Entrenar modelo
        model_RegL.fit(X_train,y_train)
        #Hacer prediccion
        y_pred = model_RegL.predict(X_test)
        #Metricas de medicion
        r2 = r2_score(y_test,y_pred)
        mse = mean_squared_error(y_test,y_pred)
        st.write(f'R2: {r2}')
        st.write(f'MSE: {mse}')

        #Validacion cruzada
        cv_model = cross_val_score(model_RegL,X,y,cv=5,scoring='r2')
        print(f'Mediana de Validacion Cruzada: {cv_model.mean()}')

except Exception as e:
    st.error(f'Error al leer el archivo: {e}')
