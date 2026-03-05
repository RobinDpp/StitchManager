import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="StitchManager - Pro Dashboard", layout="wide")

# --- NAVIGATION ---
st.sidebar.title("🧵 StitchManager")
menu = st.sidebar.radio("Navigation", ["Tableau de Bord", "Statistiques Avancées", "Nouveau Listing", "Inventaire"])

# --- PAGE : DASHBOARD (Vue d'ensemble) ---
if menu == "Tableau de Bord":
    st.title("🏠 Aperçu de la Boutique")
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Chiffre d'Affaires (30j)", "245.80 €", "+15%")
    col2.metric("Commandes", "38", "+5")
    col3.metric("Visites", "1,240", "-2%")
    col4.metric("Taux de Conv.", "3.1%", "+0.4%")

    st.divider()
    
    # Graphique rapide
    st.subheader("📈 Évolution des ventes (7 derniers jours)")
    chart_data = pd.DataFrame(
        np.random.randn(7, 1) + [10],
        columns=['Ventes (€)'],
        index=[(datetime.now() - timedelta(days=i)).strftime('%d/%m') for i in range(6, -1, -1)]
    )
    st.line_chart(chart_data)

# --- PAGE : STATISTIQUES AVANCÉES (Le "Cerveau" du Business) ---
elif menu == "Statistiques Avancées":
    st.title("📊 Analyse de Performance")
    
    tab1, tab2, tab3 = st.tabs(["💰 Revenus & Profits", "🎯 Performance Designs", "🌍 Trafic & Tags"])
    
    with tab1:
        st.subheader("Décomposition des Revenus")
        c1, c2 = st.columns(2)
        with c1:
            # Simulation données mensuelles
            months = ["Jan", "Fev", "Mar", "Avr", "Mai", "Juin"]
            revs = [150, 210, 180, 310, 280, 420]
            st.bar_chart(pd.DataFrame(revs, index=months, columns=["Revenu Mensuel (€)"]))
        with c2:
            st.write("**Récapitulatif financier :**")
            st.write(f"- Panier moyen : **6.80 €**")
            st.write(f"- Frais Etsy estimés : **-42.50 €**")
            st.write(f"- Profit net estimé : **377.50 €**")

    with tab2:
        st.subheader("Top 5 des Designs les plus vendus")
        top_designs = pd.DataFrame({
            'Design': ['Gothic Raven', 'Vintage Rose', 'Starry Night', 'Cute Bat', 'Steampunk Owl'],
            'Ventes': [45, 32, 28, 25, 18],
            'Favoris': [120, 85, 92, 110, 55]
        })
        st.table(top_designs)
        
    with tab3:
        st.subheader("Analyse des Tags (Mots-clés)")
        st.write("Quels tags génèrent le plus de clics ?")
        tags_data = pd.DataFrame({
            'Tag': ['cross stitch pattern', 'modern embroidery', 'gothic decor', 'pdf download', 'dmc colors'],
            'Efficacité (%)': [95, 82, 75, 68, 45]
        }).set_index('Tag')
        st.bar_chart(tags_data)

# --- PAGE : NOUVEAU LISTING ---
elif menu == "Nouveau Listing":
    st.title("📦 Créer une annonce")
    # (Le code précédent de création reste ici...)
    st.info("Utilisez cette page pour glisser-déposer les éléments depuis l'App Factory.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.file_uploader("Fichiers (Images/PDFs)", accept_multiple_files=True)
    with col2:
        st.text_input("Titre")
        st.text_area("Description", height=200)
    
    if st.button("Publier en Brouillon"):
        st.success("Données prêtes pour l'envoi API.")

# --- PAGE : INVENTAIRE ---
elif menu == "Inventaire":
    st.title("📋 Gestion de l'Inventaire")
    st.write("Liste de tous vos patrons numériques actifs.")
    # Simulation liste
    inventory = pd.DataFrame({
        'ID': ['001', '002', '003'],
        'Nom': ['Gothic Raven', 'Vintage Rose', 'Cute Bat'],
        'Prix': [6.50, 7.20, 5.90],
        'Status': ['En ligne', 'En ligne', 'Brouillon']
    })
    st.dataframe(inventory, use_container_width=True)