import streamlit as st

st.title ("Analítica de Datos")

uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
   df1=pd.read_csv(uploaded_file)
   st.write(df1)
   st.subheader('Estadísticos básicos de los sensores')
   st.dataframe(df1["temperatura ESP32"].describe())
else:
 st.warning('Necesitas cargar un archivo csv excel.')
