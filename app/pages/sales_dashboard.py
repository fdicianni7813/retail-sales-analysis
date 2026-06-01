import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data

# Load dataset
df = load_data()

# Page title
st.title("📈 Sales Dashboard")

# =========================
# KPI SECTION
# =========================

total_revenue = (
    df["price"] * df["quantity_sold"]
).sum()

total_profit = df["profit"].sum()

total_orders = df["order_id"].nunique()

average_order_value = total_revenue / total_orders

# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Total Revenue",
    f"€{total_revenue:,.2f}"
)

col2.metric(
    "📈 Total Profit",
    f"€{total_profit:,.2f}"
)

col3.metric(
    "🧾 Total Orders",
    total_orders
)

col4.metric(
    "🛒 Avg Order Value",
    f"€{average_order_value:,.2f}"
)

st.divider()

# =========================
# TOP PRODUCTS
# =========================

top_products = (
    df.groupby("product_name")["quantity_sold"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_top_products = px.bar(
    top_products,
    x="product_name",
    y="quantity_sold",
    title="Top Selling Products"
)

st.plotly_chart(fig_top_products, use_container_width=True)

# =========================
# PROFIT BY CATEGORY
# =========================

category_profit = (
    df.groupby("category")["profit"]
    .sum()
    .reset_index()
)

fig_category_profit = px.bar(
    category_profit,
    x="category",
    y="profit",
    title="Profit by Category"
)

st.plotly_chart(fig_category_profit, use_container_width=True)

# =========================
# MONTHLY PROFIT TREND
# =========================

df["order_date"] = pd.to_datetime(df["order_date"])

df["month"] = df["order_date"].dt.month

monthly_profit = (
    df.groupby("month")["profit"]
    .sum()
    .reset_index()
)

fig_monthly_profit = px.line(
    monthly_profit,
    x="month",
    y="profit",
    title="Monthly Profit Trend"
)

st.plotly_chart(fig_monthly_profit, use_container_width=True)