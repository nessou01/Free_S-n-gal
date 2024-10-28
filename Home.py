import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px


# Ajouter du CSS pour un arrière-plan en couleur
st.markdown("""
    <style>
    .stApp {
        background-color: #ADD8E6;  /* Code hexadécimal pour une couleur bleue légère */
    }
    </style>
    """, unsafe_allow_html=True)

# Fonction pour charger les données Excel
def load_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

# Charger une image (logo) et la redimensionner
logo = Image.open('Free.png')
resized_logo = logo.resize((200, 50))  # Ajuster la taille du logo
st.image(resized_logo, caption="", use_column_width=False)

# Titre principal avec une taille et une couleur personnalisées
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏠 HOME PAGE</h1>", unsafe_allow_html=True)

# Ajouter un sous-titre ou une description pour un meilleur accueil
st.markdown("<p style='text-align: center; font-size: 20px;'>Bienvenue dans notre tableau de bord interactif !</p>", unsafe_allow_html=True)

# Ajouter une barre de séparation pour structurer la page
st.markdown("---")

# Charger les fichiers Excel
PUE = load_data('Cons_jr2.xlsx', 'PUE')

# Vérifier que la colonne PUE existe et qu'elle contient des données
if 'PUE' in PUE.columns:
    # Pourcentage PUE
    pue_percentage = 4  # Valeur fixe de 4% pour le PUE
    remaining_percentage = 100 - pue_percentage

    # Créer un DataFrame pour le diagramme circulaire
    pie_data = pd.DataFrame({
        'Valeur': ['PUE', 'Reste'],
        'Pourcentage': [pue_percentage, remaining_percentage]
    })

    # Créer le diagramme circulaire avec plotly
    fig_pie = px.pie(
        pie_data, 
        values='Pourcentage', 
        names='Valeur', 
        title='Visualisation du Power Usage Effectiveness du datacenter',
        color_discrete_sequence=px.colors.sequential.Blues_r  # Palette de couleurs
    )

    # Afficher le graphique interactif
    st.plotly_chart(fig_pie)
else:
    st.error("La colonne 'PUE' n'est pas présente dans le fichier.")

# Faire la transposition de notre dataframe PUE
PUE = PUE.T
PUE.columns = ['Puissance en KWh']

# Filtrer les données pour exclure PUE
filtered_data = PUE[PUE.index != 'PUE']

# Ajouter une fonctionnalité d'interaction utilisateur pour ajouter des valeurs
st.markdown("### 🔢 Ajouter de nouvelles valeurs")

# Interface utilisateur pour ajouter une nouvelle valeur pour une ligne donnée
new_value = st.number_input("Ajouter une nouvelle valeur de puissance (KWh)", min_value=0.0, step=1.0, format="%.2f")
selected_row = st.selectbox("Sélectionner une charge pour laquelle ajouter la valeur", filtered_data.index)

# Mettre à jour le tableau avec la nouvelle valeur entrée par l'utilisateur
if st.button("Ajouter la valeur"):
    filtered_data.loc[selected_row, 'Puissance en KWh'] = new_value
    st.success(f"La valeur {new_value} KWh a été ajoutée pour la charge '{selected_row}'.")

# Afficher les données dans un tableau mis à jour
st.markdown("### 📊 Analyse des Données PUE")
st.write("Voici les données de puissance énergétique (PUE) pour aujourd'hui.")
st.dataframe(filtered_data, width=700, height=400)

# Graphique interactif mis à jour avec Plotly
fig = px.line(filtered_data, y='Puissance en KWh', title='Évolution de la puissance (KWh)', labels={'index': 'Charges', 'value': 'Puissance (KWh)'})
st.plotly_chart(fig)

# Création d'un diagramme en barres groupées
fig6 = px.bar(
    filtered_data,
    x=filtered_data.index,
    y=filtered_data.columns,
    title="Diagramme en barres de la puissance (hors PUE)",
    barmode='group',
    labels={'index': 'Charges', 'Puissance en KWh': 'Puissance (KWh)'}
)
st.plotly_chart(fig6)


# Footer ou texte de conclusion
st.markdown("<footer style='text-align: center;'>© 2024 Free Sénégal. Tous droits réservés.</footer>", unsafe_allow_html=True)
