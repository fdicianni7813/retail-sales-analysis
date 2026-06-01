import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from components.filters import apply_filters


# =========================
# LOAD DATA
# =========================

df = load_data()

# Apply sidebar filters
filtered_df = apply_filters(df)


# =========================
# PAGE TITLE
# =========================

st.title("📈 Sales Dashboard")


# =========================
# KPI SECTION
# =========================

total_revenue = (
    filtered_df["price"]
    * filtered_df["quantity_sold"]
).sum()

total_profit = (
    filtered_df["profit"]
).sum()

total_orders = (
    filtered_df["order_id"]
).nunique()

average_order_value = (
    total_revenue / total_orders
)

# Create KPI columns
col1, col2, col3, col4 = st.columns(4)

# KPI cards
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
# TOP PRODUCTS CHART
# =========================

top_products = (
    filtered_df.groupby("product_name")
    ["quantity_sold"]
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

st.plotly_chart(
    fig_top_products,
    use_container_width=True
)

st.divider()


# =========================
# PROFIT BY CATEGORY
# =========================

category_profit = (
    filtered_df.groupby("category")
    ["profit"]
    .sum()
    .reset_index()
)

fig_category_profit = px.bar(
    category_profit,
    x="category",
    y="profit",
    title="Profit by Category"
)

st.plotly_chart(
    fig_category_profit,
    use_container_width=True
)

st.divider()


# =========================
# MONTHLY PROFIT TREND
# =========================

filtered_df["order_date"] = pd.to_datetime(
    filtered_df["order_date"]
)

filtered_df["month"] = (
    filtered_df["order_date"]
    .dt.month
)

monthly_profit = (
    filtered_df.groupby("month")
    ["profit"]
    .sum()
    .reset_index()
)

fig_monthly_profit = px.line(
    monthly_profit,
    x="month",
    y="profit",
    title="Monthly Profit Trend"
)

st.plotly_chart(
    fig_monthly_profit,
    use_container_width=True
)