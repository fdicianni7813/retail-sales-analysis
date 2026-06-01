import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Retail Business Dashboard",
    page_icon="📊",
    layout="wide"
)

# Main title
st.title("📊 Retail Business Dashboard")

# Introduction
st.markdown("""
Welcome to the Retail Sales & Inventory Analysis Dashboard.

This application provides business insights related to:
- Sales performance
- Product profitability
- Inventory monitoring
- Trend analysis
""")

# Sidebar
st.sidebar.success("Select a page above.")