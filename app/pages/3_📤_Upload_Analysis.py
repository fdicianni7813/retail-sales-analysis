import streamlit as st
import pandas as pd

# Page title
st.title("📤 Upload Analysis")

st.markdown("""
Upload a CSV dataset to generate a quick analysis preview.
""")

# =========================
# FILE UPLOADER
# =========================

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

# =========================
# FILE ANALYSIS
# =========================

if uploaded_file is not None:

    # Load uploaded dataset
    uploaded_df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")

    st.balloons()

    st.divider()

    # =========================
    # DATA PREVIEW
    # =========================

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        uploaded_df.head(),
        use_container_width=True
    )

    st.divider()

    # =========================
    # DATASET INFO
    # =========================

    st.subheader("📊 Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Rows",
        uploaded_df.shape[0]
    )

    col2.metric(
        "Columns",
        uploaded_df.shape[1]
    )

    col3.metric(
        "Missing Values",
        uploaded_df.isnull().sum().sum()
    )

    st.divider()

    # =========================
    # COLUMN TYPES
    # =========================

    st.subheader("🧾 Column Data Types")

    dtypes_df = pd.DataFrame({
        "Column": uploaded_df.columns,
        "Data Type": uploaded_df.dtypes.astype(str)
    })

    st.dataframe(
        dtypes_df,
        use_container_width=True
    )

    st.divider()

    # =========================
    # QUICK INSIGHTS
    # =========================

    st.subheader("💡 Quick Insights")

    numeric_columns = uploaded_df.select_dtypes(
        include="number"
    ).columns

    if len(numeric_columns) > 0:

        st.write(
            "Numeric columns detected:"
        )

        st.write(list(numeric_columns))

        st.write(
            uploaded_df[numeric_columns]
            .describe()
        )

    else:

        st.warning(
            "No numeric columns detected."
        )

else:

    st.info(
        "Upload a CSV dataset to begin analysis."
    )
    