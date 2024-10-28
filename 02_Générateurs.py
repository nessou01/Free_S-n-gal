import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Ajouter du CSS pour un arrière-plan en couleur
st.markdown("""
    <style>
    .stApp {
        background-color: #ADD8E6;  /* Code hexadécimal pour une couleur bleue légère */
    }
    </style>
    """, unsafe_allow_html=True)

# Charger une image depuis un fichier local
logo = Image.open('Free.png')

# Resize the image to your desired size (width, height)
resized_logo = logo.resize((200, 50))  # Adjust these values as needed

# Display the resized logo with st.logo
st.logo(resized_logo, link=None, icon_image=None)


def load_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

# Charger les fichiers Excel
GENERATEUR_A = load_data('Cons_jr2.xlsx', 'GENERATEUR_A')
GENERATEUR_B = load_data('Cons_jr2.xlsx', 'GENERATEUR_B')

st.dataframe(GENERATEUR_A)
st.dataframe(GENERATEUR_B)

# Exemple de DataFrame
data = {'Total server_Power': [100, 200, 150],
        'Total_Consommation(KWh)': [300, 500, 450],
        'PUE': [1.5, 2.0, 2.1]}

df = pd.DataFrame(data)
# Appliquer un dégradé de couleur sur les colonnes numériques
styled_df = df.style.background_gradient(cmap='RdYlGn')

# Afficher le DataFrame stylisé avec Streamlit
st.dataframe(styled_df)