import streamlit as st

st.set_page_config(
    page_title="Retail Business Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Business Intelligence Dashboard")

st.markdown("""
Welcome to the Retail Business Intelligence Platform.

This application provides:

- 📈 Sales analytics
- 📦 Inventory monitoring
- 💰 Profitability analysis
- 📤 CSV upload analysis
- 📊 Interactive business insights
""")

st.divider()

st.subheader("🚀 Platform Features")

col1, col2, col3 = st.columns(3)

col1.info(
    "Analyze sales performance and profitability trends."
)

col2.info(
    "Monitor inventory and detect low-stock products."
)

col3.info(
    "Upload custom CSV datasets for quick analysis."
)

st.divider()

st.success(
    "Use the sidebar to navigate through dashboard pages."
)