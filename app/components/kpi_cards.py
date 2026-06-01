import streamlit as st


def display_kpi_cards(
    revenue,
    profit,
    orders,
    average_order_value
):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Total Revenue",
        f"€{revenue:,.2f}"
    )

    col2.metric(
        "📈 Total Profit",
        f"€{profit:,.2f}"
    )

    col3.metric(
        "🧾 Total Orders",
        orders
    )

    col4.metric(
        "🛒 Avg Order Value",
        f"€{average_order_value:,.2f}"
    )