import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from components.filters import apply_filters
from components.kpi_cards import display_kpi_cards


# =========================
# LOAD DATA
# =========================

df = load_data()

# Apply sidebar filters
filtered_df = apply_filters(df)

if filtered_df.empty:

    st.warning(
        "No data available for selected filters."
    )

    st.stop()


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

display_kpi_cards(
    total_revenue,
    total_profit,
    total_orders,
    average_order_value
)

# =========================
# BUSINESS KPI SECTION
# =========================

profit_margin = (
    (total_profit / total_revenue) * 100
)

best_category = (
    filtered_df.groupby("category")["profit"]
    .sum()
    .idxmax()
)

inventory_risk_count = (
    filtered_df[
        filtered_df["stock_remaining"] < 10
    ]["product_name"]
    .nunique()
)

top_payment_method = (
    filtered_df["payment_method"]
    .mode()[0]
)

st.markdown("## 📊 BUSINESS PERFORMANCE OVERVIEW")

col1, col2 = st.columns(2)

with col1:

    st.info(
        f"""
        ### 💰 PROFIT MARGIN

        **{profit_margin:.2f}%**

        Percentage of revenue converted into profit.
        """
    )

    st.info(
        f"""
        ### 📦 INVENTORY RISK

        **{inventory_risk_count} products**

        Products currently running low on stock.
        """
    )

with col2:

    st.info(
        f"""
        ### 🏆 BEST CATEGORY

        **{best_category}**

        Highest performing category by total profit.
        """
    )

    st.info(
        f"""
        ### 💳 TOP PAYMENT METHOD

        **{top_payment_method}**

        Most frequently used payment method.
        """
    )

st.divider()

# =========================
# BUSINESS INSIGHT MESSAGE
# =========================

if total_profit > 15000:

    st.success(
        "📈 Business performance is strong with high profitability."
    )

else:

    st.warning(
        "⚠️ Profitability could be improved."
    )

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
    title="Top Selling Products",
    color="quantity_sold",
    template="plotly_dark"
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
    title="Profit by Category",
    template="plotly_dark"
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
    title="Monthly Profit Trend",
    template="plotly_dark"
)

st.plotly_chart(
    fig_monthly_profit,
    use_container_width=True
)