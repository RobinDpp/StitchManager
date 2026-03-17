import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- CONFIGURATION ---
st.set_page_config(page_title="StitchManager Pro", layout="wide", page_icon="🧵")

# CSS FIX: Forced contrast for Tabs and professional UI
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Tabs styling for high visibility */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #f0f2f6; /* Light grey background for the bar */
        padding: 5px;
        border-radius: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        background-color: #ffffff; /* White tabs */
        border-radius: 5px;
        color: #31333F !important; /* Force dark text */
        font-weight: 600;
        padding: 10px 20px;
        border: 1px solid #dfe1e5;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff4b4b !important; /* Red highlight for active tab */
        color: white !important; /* White text for active tab */
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- UTILITY FUNCTIONS ---
def clean_tags(tags_string):
    raw_tags = [t.strip() for t in tags_string.split(",") if t.strip()]
    valid_tags = [t[:20] for t in raw_tags[:13]]
    return valid_tags

# --- SIDEBAR ---
with st.sidebar:
    st.title("🧵 StitchManager")
    st.caption("Inventory Management System V1.0")
    st.divider()
    menu = st.radio("Navigation", [
        "📊 Dashboard", 
        "➕ Create Listing", 
        "🗃️ Inventory Manager", 
        "📈 Financial Analytics"
    ])
    st.divider()
    st.success("Shop: **Robin's Stitches**")
    st.caption("API Status: 🟠 Pending Review")

# --- PAGE: DASHBOARD ---
if menu == "📊 Dashboard":
    st.title("Shop Performance Overview")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Revenue (30d)", "428.50 €", "+12.4%")
    c2.metric("Orders", "64", "+8")
    c3.metric("Conversion Rate", "3.2%", "+0.5%")
    c4.metric("Avg. Order Value", "6.69 €", "-0.10 €")
    
    st.divider()
    st.subheader("📈 Daily Revenue Evolution")
    chart_data = pd.DataFrame({
        'Day': [f"March {i}" for i in range(1, 16)],
        'Revenue': [25, 32, 18, 45, 60, 38, 22, 55, 40, 35, 70, 42, 30, 48, 52]
    }).set_index('Day')
    st.area_chart(chart_data)

# --- PAGE: CREATE LISTING ---
elif menu == "➕ Create Listing":
    st.title("🛠️ Listing Editor")
    st.info("Prepare your digital product metadata and assets for seamless shop synchronization.")

    # TABS WITH FIXED COLORS
    tab_info, tab_files, tab_shipping = st.tabs(["📝 Listing Details", "💾 Digital Files", "💰 Pricing & Profit"])

    with tab_info:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("General Information")
            title = st.text_input("Listing Title", value="Modern Floral Cross Stitch Pattern - PDF Download")
            category = st.selectbox("Category", ["Embroidery Patterns", "Digital Art", "Craft Supplies"])
            section = st.text_input("Shop Section", value="Floral Collection")
            
        with col2:
            st.subheader("SEO & Optimization")
            tags_input = st.text_area("Tags (comma separated)", value="cross stitch, modern embroidery, diy gift, floral pattern, nursery decor")
            valid_tags = clean_tags(tags_input)
            
            st.write(f"**Validated Tags ({len(valid_tags)}/13):**")
            cols = st.columns(4)
            for i, tag in enumerate(valid_tags):
                cols[i % 4].caption(f"✅ {tag}")

        st.divider()
        description = st.text_area("Full Description", height=200, value="This is a high-quality digital PDF pattern for cross-stitch enthusiasts...")
        materials = st.text_input("Materials", value="Digital PDF, DMC Color Chart, Instant Download")

    with tab_files:
        st.subheader("Digital Asset Management")
        c1, c2 = st.columns(2)
        with c1:
            st.file_uploader("🖼️ Listing Images (Mockups)", accept_multiple_files=True)
        with c2:
            st.file_uploader("📄 Product Files (PDF / ZIP)", accept_multiple_files=True)

    with tab_shipping:
        st.subheader("Profit Calculator")
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            base_price = st.number_input("Retail Price (€)", value=6.50, step=0.10)
        with col_p2:
            total_fees = 0.18 + (base_price * 0.065) + (base_price * 0.04 + 0.30)
            profit = base_price - total_fees
            st.metric("Estimated Net Profit", f"{profit:.2f} €", delta=f"-{total_fees:.2f} Etsy Fees")

    st.divider()
    if st.button("📤 Save as Draft on Etsy", type="primary", use_container_width=True):
        st.success(f"Listing '{title}' successfully prepared.")

# --- PAGE: INVENTORY MANAGER ---
elif menu == "🗃️ Inventory Manager":
    st.title("🗃️ Digital Product Inventory")
    inventory_df = pd.DataFrame({
        "SKU ID": ["ST-001", "ST-002", "ST-003", "ST-004"],
        "Product Name": ["Gothic Raven Pattern", "Vintage Floral Set", "Night Owl Series", "Cute Bat Edition"],
        "Price (€)": [6.50, 7.20, 5.90, 6.00],
        "Units Sold": [142, 89, 45, 210],
        "Status": ["Active", "Active", "Draft", "Active"]
    })
    st.dataframe(inventory_df, use_container_width=True, hide_index=True)

# --- PAGE: FINANCIAL ANALYTICS ---
elif menu == "📈 Financial Analytics":
    st.title("📈 Detailed Analytics")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### Sales by Category")
        chart_data = pd.DataFrame({"Styles": ["Gothic", "Floral", "Modern", "Seasonal"], "Sales": [40, 25, 20, 15]}).set_index("Styles")
        st.bar_chart(chart_data)
    with col_b:
        st.write("### Top Performing Tags")
        tags_df = pd.DataFrame({"Tag Keyword": ["cross stitch", "modern embroidery", "gothic decor"], "Clicks": [1200, 850, 780]})
        st.table(tags_df)