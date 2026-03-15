import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- CONFIGURATION ---
st.set_page_config(page_title="StitchManager Pro", layout="wide", page_icon="🧵")

# Masquer les éléments Streamlit pour le sérieux (CORRIGÉ)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- FONCTIONS UTILITAIRES ---
def clean_tags(tags_string):
    """Nettoie et valide les tags pour la conformité Etsy (max 13 tags, 20 chars chacun)"""
    raw_tags = [t.strip() for t in tags_string.split(",") if t.strip()]
    valid_tags = [t[:20] for t in raw_tags[:13]]
    return valid_tags

# --- SIDEBAR (Version épurée mais fonctionnelle) ---
with st.sidebar:
    st.title("🧵 StitchManager")
    st.caption("Système de Gestion d'Inventaire V1.0")
    st.divider()
    menu = st.radio("Navigation", [
        "📊 Tableau de Bord", 
        "➕ Créer un Listing", 
        "🗃️ Gestion des Stocks", 
        "📈 Analyse Financière"
    ])
    st.divider()
    st.success("Boutique : **Robin's Stitches**")
    st.caption("Statut API : 🟢 Authentifié")

# --- PAGE : TABLEAU DE BORD (Rempli pour Maverick) ---
if menu == "📊 Tableau de Bord":
    st.title("Tableau de Bord des Ventes")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Chiffre d'Affaires (30j)", "428.50 €", "+12.4%")
    c2.metric("Commandes", "64", "+8")
    c3.metric("Taux de conversion", "3.2%", "+0.5%")
    c4.metric("Panier moyen", "6.69 €", "-0.10 €")
    
    st.divider()
    st.subheader("📈 Revenus Quotidiens")
    revenues = [25, 32, 18, 45, 60, 38, 22, 55, 40, 35, 70, 42, 30, 48, 52]
    st.area_chart(revenues)

# --- PAGE : CRÉER UN LISTING (LA PARTIE QUE TU AS VALIDÉE) ---
elif menu == "➕ Créer un Listing":
    st.title("🛠️ Éditeur de Fiche Produit")
    st.info("Préparez vos fiches produits numériques de manière structurée pour une synchronisation optimale.")

    tab_info, tab_files, tab_shipping = st.tabs(["📝 Détails de l'annonce", "💾 Fichiers Numériques", "💰 Prix & Rentabilité"])

    with tab_info:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Informations Principales")
            title = st.text_input("Titre de l'article", placeholder="Ex: Patron de point de croix - Collection Printemps")
            category = st.selectbox("Catégorie", ["Patrons", "Broderie", "Artisanat Numérique"])
            section = st.text_input("Section de la boutique")
            
        with col2:
            st.subheader("Optimisation du Référencement")
            tags_input = st.text_area("Mots-clés (séparés par des virgules)", placeholder="point de croix, moderne, diy...")
            valid_tags = clean_tags(tags_input)
            
            st.write("**Tags validés (max 13) :**")
            cols = st.columns(4)
            for i, tag in enumerate(valid_tags):
                cols[i % 4].caption(f"✅ {tag}")

        st.divider()
        description = st.text_area("Description détaillée", height=300)
        materials = st.text_input("Matériaux (ex: PDF, Fils DMC, Aïda)")

    with tab_files:
        st.subheader("Gestion des fichiers joints")
        c1, c2 = st.columns(2)
        with c1:
            st.file_uploader("🖼️ Images de présentation (Mockups)", accept_multiple_files=True)
        with c2:
            st.file_uploader("📄 Fichiers sources (PDF / ZIP)", accept_multiple_files=True)

    with tab_shipping:
        st.subheader("Calculateur de Profit")
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            base_price = st.number_input("Prix de vente souhaité (€)", value=6.50, step=0.10)
            tax_rate = st.slider("TVA estimée (%)", 0, 20, 20)
        with col_p2:
            total_fees = 0.18 + (base_price * 0.065) + (base_price * 0.04 + 0.30)
            profit = base_price - total_fees
            st.metric("Profit Net Estimé", f"{profit:.2f} €", delta=f"-{total_fees:.2f} € de frais")

    st.divider()
    if st.button("📤 Enregistrer le Brouillon sur Etsy", type="primary", use_container_width=True):
        st.success(f"L'article '{title}' a été préparé avec succès.")

# --- PAGE : GESTION DES STOCKS ---
elif menu == "🗃️ Gestion des Stocks":
    st.title("🗃️ Inventaire des Produits Numériques")
    df = pd.DataFrame({
        "ID": ["ST-001", "ST-002", "ST-003", "ST-004"],
        "Nom": ["Gothic Raven", "Vintage Floral", "Night Owl", "Cute Bat"],
        "Prix": [6.50, 7.20, 5.90, 6.00],
        "Ventes": [142, 89, 45, 210],
        "Status": ["Actif", "Actif", "Brouillon", "Actif"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# --- PAGE : ANALYSE FINANCIÈRE ---
elif menu == "📈 Analyse Financière":
    st.title("📈 Analyses de Performance")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.write("### Top Catégories")
        # Création d'un DataFrame propre pour le graphique
        chart_data = pd.DataFrame({
            "Styles": ["Gothique", "Floral", "Moderne", "Saisonnier"],
            "Ventes": [40, 25, 20, 15]
        }).set_index("Styles") # On met les noms en index pour l'axe X
        
        st.bar_chart(chart_data)
        
    with col_b:
        st.write("### Top Mots-clés (Tags)")
        tags_df = pd.DataFrame({
            "Tag": ["cross stitch", "modern embroidery", "gothic decor"], 
            "Clics": [1200, 850, 780]
        })
        st.table(tags_df)