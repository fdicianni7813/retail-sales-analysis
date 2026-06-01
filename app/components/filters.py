import streamlit as st


def apply_filters(df):

    st.sidebar.header("🔎 Dashboard Filters")

    # Category filter
    categories = df["category"].unique()

    selected_categories = st.sidebar.multiselect(
        "Select Category",
        categories,
        default=categories
    )

    # Payment method filter
    payment_methods = df[
        "payment_method"
    ].unique()

    selected_payments = st.sidebar.multiselect(
        "Select Payment Method",
        payment_methods,
        default=payment_methods
    )

    # Apply filters
    filtered_df = df[
        (df["category"].isin(selected_categories))
        &
        (
            df["payment_method"]
            .isin(selected_payments)
        )
    ]

    return filtered_df