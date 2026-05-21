import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.header("Aplicación web de proyecto de Sprint 7")

# Leer los datos del archivo CSV
car_data = pd.read_csv('notebooks/vehicles_us.csv')

# Crear un botón en la aplicación Streamlit para construir un histograma
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects, darle título y mostrarlo en la aplicación web
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, width='stretch')

# Crear un botón en la aplicación Streamlit para construir un gráfico de dispersión
disp_button = st.button('Construir gráfico de dispersión')

# Lógica a ejecutar cuando se hace clic en el botón
if disp_button:

    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un scatter plot utilizando plotly.graph_objects, darle título y mostrarlo en la aplicación web
    fig = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig, width='stretch')
