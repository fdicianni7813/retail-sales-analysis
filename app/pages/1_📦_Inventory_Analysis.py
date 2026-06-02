import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

# Load dataset
df = load_data()

# Page title
st.title("📦 Inventory Analysis")

# =========================
# LOW STOCK ALERTS
# =========================

st.subheader("⚠️ Low Stock Products")

low_stock = df[df["stock_remaining"] < 15]

low_stock_products = (
    low_stock[
        ["product_name", "category", "stock_remaining"]
    ]
    .drop_duplicates()
    .sort_values("stock_remaining")
)

st.dataframe(
    low_stock_products,
    use_container_width=True
)

st.divider()

# =========================
# STOCK DISTRIBUTION
# =========================

stock_distribution = (
    df.groupby("category")["stock_remaining"]
    .mean()
    .reset_index()
)

fig_stock_distribution = px.bar(
    stock_distribution,
    x="category",
    y="stock_remaining",
    title="Average Stock Remaining by Category"
)

st.plotly_chart(
    fig_stock_distribution,
    use_container_width=True
)

# =========================
# CRITICAL INVENTORY
# =========================

st.subheader("🚨 Critical Inventory Products")

critical_inventory = df[
    df["stock_remaining"] < 5
]

critical_inventory = (
    critical_inventory[
        [
            "product_name",
            "stock_remaining",
            "category"
        ]
    ]
    .drop_duplicates()
)

if critical_inventory.empty:

    st.success(
        "No critical inventory issues detected."
    )

else:

    st.error(
        "Some products are critically low on stock."
    )

    st.dataframe(
        critical_inventory,
        use_container_width=True
    )