import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Title Section
# -----------------------------
st.markdown(
    """
    <h1 style='text-align: center;'>📊 Sales Analytics Dashboard</h1>
    <p style='text-align: center; color: gray;'>
    Interactive sales insights using Streamlit
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# Sample Sales Data
# -----------------------------
np.random.seed(42)

data = {
    "Date": pd.date_range(start="2025-01-01", periods=30),
    "Region": np.random.choice(["North", "South", "East", "West"], 30),
    "Product": np.random.choice(["Laptop", "Mobile", "Tablet"], 30),
    "Sales": np.random.randint(5000, 50000, 30),
    "Quantity": np.random.randint(1, 20, 30)
}

df = pd.DataFrame(data)

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.title("🔎 Filter Options")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

product_filter = st.sidebar.multiselect(
    "Select Product",
    options=df["Product"].unique(),
    default=df["Product"].unique()
)

filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Product"].isin(product_filter))
]

# -----------------------------
# KPI Section
# -----------------------------
st.subheader("📌 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    "💰 Total Sales",
    f"₹ {filtered_df['Sales'].sum():,}"
)

col2.metric(
    "📦 Total Quantity",
    f"{filtered_df['Quantity'].sum():,}"
)

col3.metric(
    "📊 Average Sale",
    f"₹ {int(filtered_df['Sales'].mean()):,}"
)

st.markdown("---")

# -----------------------------
# Charts Section
# -----------------------------
col4, col5 = st.columns(2)

with col4:
    st.subheader("🏷 Sales by Region")
    region_sales = filtered_df.groupby("Region")["Sales"].sum()
    st.bar_chart(region_sales)

with col5:
    st.subheader("📈 Sales Trend Over Time")
    daily_sales = filtered_df.groupby("Date")["Sales"].sum()
    st.line_chart(daily_sales)

st.markdown("---")

# -----------------------------
# Product-wise Sales
# -----------------------------
st.subheader("📦 Product-wise Sales Distribution")
product_sales = filtered_df.groupby("Product")["Sales"].sum()
st.area_chart(product_sales)

st.markdown("---")

# -----------------------------
# Data Table
# -----------------------------
st.subheader("📄 Sales Data Table")
st.dataframe(
    filtered_df,
    use_container_width=True
)

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray;'>
    Built with ❤️ using Streamlit | Python
    </p>
    """,
    unsafe_allow_html=True
)
