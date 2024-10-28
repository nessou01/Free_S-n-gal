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
    df = df.rename(index={0: 'PHASE A', 1: 'PHASE B', 2: 'PHASE C'})
    return df

# Charger les fichiers Excel
Cons_Jr = load_data('Cons_jr.xlsx', 'Sheet1')
L80 = load_data('Cons_jr2.xlsx', 'L80')
L60 = load_data('Cons_jr2.xlsx', 'L60')
ELTEK_1 = pd.read_excel('Cons_jr2.xlsx', 'ELTEK1')
ELTEK_VALERE = pd.read_excel('Cons_jr2.xlsx', 'ELTEK2')

# Créer des tabs
tab1, tab2, tab3 = st.tabs(["Consommation Journalière", "Onduleurs", "Redresseurs"])

with tab1:
    st.header("Consommation journalière Almadie Bureau")
    Cons_Jr = st.data_editor(Cons_Jr)
    fig = px.line(Cons_Jr, x=Cons_Jr.index, y=Cons_Jr.columns, title="Consommation par phase")
    st.plotly_chart(fig)
    



with tab2:
    st.title('Visualisation des données des onduleurs')
    st.subheader("Onduleur L80 ")
    st.dataframe(L80)
    fig2 = px.line(L80, x=L80.index, y=L80.columns, title="Consommation journalière par phase")
    st.plotly_chart(fig2)
    st.subheader("Onduleur L60 ")
    st.dataframe(L60)
    fig3 = px.line(L60, x=L60.index, y=L60.columns, title="Consommation journalière par phase")
    st.plotly_chart(fig3)


with tab3:
    st.title("Visualisation des données des redresseurs")
    st.subheader("Tableau recapitulatif des Rectifiers ")
    # Concaténation et ajout de la colonne Équipement
    RECTIFIER = pd.concat([ELTEK_1, ELTEK_VALERE])
    # Renommage des index
    RECTIFIER.index = ['ELTEK1', 'ELTEK_VALERE']
    st.dataframe(RECTIFIER)
    import plotly.graph_objects as go

    fig5 = go.Figure()
    fig5.add_trace(go.Scatter(x=RECTIFIER.index, y=RECTIFIER['LOAD (kW)'], name='Consommation en kW'))
    fig5.add_trace(go.Scatter(x=RECTIFIER.index, y=RECTIFIER['V OUT'], name='Tension de sortie'))
    fig5.update_layout(title='Puissances et tension des redresseurs')

    st.plotly_chart(fig5)
    #vISIUALITION AVEC PLOTLY
    fig4 = px.line(RECTIFIER, x=RECTIFIER.index, y=RECTIFIER.columns, title= "Consommation des redresseurs")
    st.plotly_chart(fig4)
    # Création d'un diagramme en barres groupées
    fig6 = px.bar(
        RECTIFIER,
        x=RECTIFIER.index,
        y=RECTIFIER.columns,
        title="Consommation des redresseurs",
        barmode='group'
    )
    st.plotly_chart(fig6)
    