import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
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
COOLING = load_data('Cons_jr2.xlsx', 'COOLING')

st.dataframe(COOLING)

# Add table data
selected_columns = ['LABEL', 'L1 current', 'L2 current','L3 current']
# Initialize a figure with ff.create_table(table_data)
fig_0 = ff.create_table(COOLING[selected_columns], height_constant=60)

# Add graph data
Label = COOLING['LABEL']
L1_current = COOLING['L1 current']
L2_current = COOLING['L2 current']
L3_current = COOLING['L3 current']
# Make traces for graph
trace1 = go.Bar(x=Label, y=L1_current, xaxis='x2', yaxis='y2',
                marker=dict(color='#0099ff'),
                name='L1 current')
trace2 = go.Bar(x=Label, y=L2_current, xaxis='x2', yaxis='y2',
                marker=dict(color='#404040'),
                name='L2 current')
trace3 = go.Bar(x=Label, y=L3_current, xaxis='x2', yaxis='y2',
                marker=dict(color='purple'),
                name='L3 current')

# Add trace data to figure
fig_0.add_traces([trace1, trace2,trace3])

# initialize xaxis2 and yaxis2
fig_0['layout']['xaxis2'] = {}
fig_0['layout']['yaxis2'] = {}
# Edit layout for subplots
fig_0.layout.yaxis.update({'domain': [0, .45]})
fig_0.layout.yaxis2.update({'domain': [.6, 1]})

# The graph's yaxis2 MUST BE anchored to the graph's xaxis2 and vice versa
fig_0.layout.yaxis2.update({'anchor': 'x2'})
fig_0.layout.xaxis2.update({'anchor': 'y2'})
fig_0.layout.yaxis2.update({'title': 'Current'})

# Update the margins to add a title and see graph x-labels.
fig_0.layout.margin.update({'t':75, 'l':50})
fig_0.layout.update({'title': 'graphique de la consommation par phase'})

# Update the height because adding a graph vertically will interact with
# the plot height calculated for the table
fig_0.layout.update({'height':900})
# Plot with Streamlit
st.plotly_chart(fig_0)
 


# Add table data
selected_columns = ['LABEL', 'Apparent Power L1', 'Apparent Power L2','Apparent Power L3']
# Initialize a figure with ff.create_table(table_data)
fig_1 = ff.create_table(COOLING[selected_columns], height_constant=60)

# Add graph data
Label = COOLING['LABEL']
Apparent_Power_L1 = COOLING['Apparent Power L1']
Apparent_Power_L2 = COOLING['Apparent Power L2']
Apparent_Power_L3 = COOLING[ 'Apparent Power L3']
# Make traces for graph
trace1 = go.Bar(x=Label, y=Apparent_Power_L1, xaxis='x2', yaxis='y2',
                marker=dict(color='#0099ff'),
                name= 'Apparent Power L1')
trace2 = go.Bar(x=Label, y=Apparent_Power_L2, xaxis='x2', yaxis='y2',
                marker=dict(color='#404040'),
                name= 'Apparent Power L2')
trace3 = go.Bar(x=Label, y=Apparent_Power_L3, xaxis='x2', yaxis='y2',
                marker=dict(color='purple'),
                name= 'Apparent Power L3')

# Add trace data to figure
fig_1.add_traces([trace1, trace2,trace3])

# initialize xaxis2 and yaxis2
fig_1['layout']['xaxis2'] = {}
fig_1['layout']['yaxis2'] = {}
# Edit layout for subplots
fig_1.layout.yaxis.update({'domain': [0, .45]})
fig_1.layout.yaxis2.update({'domain': [.6, 1]})

# The graph's yaxis2 MUST BE anchored to the graph's xaxis2 and vice versa
fig_1.layout.yaxis2.update({'anchor': 'x2'})
fig_1.layout.xaxis2.update({'anchor': 'y2'})
fig_1.layout.yaxis2.update({'title': 'Current'})

# Update the margins to add a title and see graph x-labels.
fig_1.layout.margin.update({'t':75, 'l':50})
fig_1.layout.update({'title': 'graphique de la consommation par Apparent Power L1'})

# Update the height because adding a graph vertically will interact with
# the plot height calculated for the table
fig_1.layout.update({'height':900})
# Plot with Streamlit
st.plotly_chart(fig_1)


Total_Apparent_Power = COOLING['Total Apparent Power']

# Create a Figure object
fig_3 = go.Figure(data=go.Bar(x=Label, y=Total_Apparent_Power, xaxis='x2', yaxis='y2',
                                 marker=dict(color='#0099ff'),
                                 name='Total_Apparent_Power'))

# Display the figure with Streamlit
st.plotly_chart(fig_3)
