import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Hide Streamlit menu
st.set_page_config(page_title="Sales Dashboard", layout="wide")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Sales Data Analysis Dashboard")
st.write("Retail sales data visualization and insights")
st.write("")

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('sales_data.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        df['TotalSales'] = df['Quantity'] * df['UnitPrice']
        return df
    except:
        return None

df = load_data()

if df is not None:
    # Sidebar filters
    st.sidebar.header("Filters")
    
    # Region filter
    regions = ['All'] + list(df['Region'].unique())
    selected_region = st.sidebar.selectbox("Select Region", regions)
    
    # Category filter
    categories = ['All'] + list(df['Category'].unique())
    selected_category = st.sidebar.selectbox("Select Category", categories)
    
    # Filter data
    filtered_df = df.copy()
    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    if selected_category != 'All':
        filtered_df = filtered_df[filtered_df['Category'] == selected_category]
    
    # Key Metrics
    st.subheader("Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Sales", f"Rs {filtered_df['TotalSales'].sum():,.0f}")
    with col2:
        st.metric("Total Orders", f"{len(filtered_df):,}")
    with col3:
        st.metric("Avg Order Value", f"Rs {filtered_df['TotalSales'].mean():,.0f}")
    with col4:
        st.metric("Total Quantity", f"{filtered_df['Quantity'].sum():,}")
    
    st.write("")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sales by Category")
        category_sales = filtered_df.groupby('Category')['TotalSales'].sum().sort_values(ascending=False)
        
        fig, ax = plt.subplots(figsize=(8, 5))
        category_sales.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_xlabel('Category')
        ax.set_ylabel('Total Sales (Rs)')
        ax.set_title('Sales by Category')
        plt.xticks(rotation=45)
        st.pyplot(fig)
    
    with col2:
        st.subheader("Sales by Region")
        region_sales = filtered_df.groupby('Region')['TotalSales'].sum().sort_values(ascending=False)
        
        fig, ax = plt.subplots(figsize=(8, 5))
        region_sales.plot(kind='bar', ax=ax, color='lightgreen')
        ax.set_xlabel('Region')
        ax.set_ylabel('Total Sales (Rs)')
        ax.set_title('Sales by Region')
        plt.xticks(rotation=45)
        st.pyplot(fig)
    
    st.write("")
    
    # Sales Trend
    st.subheader("Sales Trend Over Time")
    daily_sales = filtered_df.groupby('Date')['TotalSales'].sum().reset_index()
    
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(daily_sales['Date'], daily_sales['TotalSales'], marker='o', linewidth=2, color='purple')
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Sales (Rs)')
    ax.set_title('Daily Sales Trend')
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    st.write("")
    
    # Top Products
    st.subheader("Top 10 Products by Sales")
    top_products = filtered_df.groupby('Product')['TotalSales'].sum().sort_values(ascending=False).head(10)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    top_products.plot(kind='barh', ax=ax, color='coral')
    ax.set_xlabel('Total Sales (Rs)')
    ax.set_ylabel('Product')
    ax.set_title('Top 10 Products')
    st.pyplot(fig)
    
    st.write("")
    
    # Raw Data
    if st.checkbox("Show Raw Data"):
        st.subheader("Sales Data")
        st.dataframe(filtered_df)

else:
    st.error("Sales data file not found. Please upload 'sales_data.csv' file.")
    st.info("Upload your CSV file with columns: OrderID, Date, Product, Category, Quantity, UnitPrice, Region")
