import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

main_df = pd.read_csv("dashboard/main_data.csv")
customers_df = pd.read_csv("data/olist_customers_dataset.csv")

st.title("Submisson Data Analys Dicoding")

st.markdown(
    """

#My First Submission, i hope i can get better
    
    """
)

st.caption('Muhammad Ali Yahya ML-02')

st.title("Hasil Analisa data pertama")
st.header("Customer Demographics")

customer_demographics = customers_df.groupby('customer_state').agg({
    'customer_id':'count'
}).rename(columns={'customer_id':'count'})

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(customer_demographics.index, customer_demographics['count'])
ax.set_xlabel("State")
ax.set_ylabel("Number of Customers")
ax.set_title("Customer Demographics by State")
ax.set_xticks(customer_demographics.index)
ax.set_xticklabels(customer_demographics.index, rotation=45, ha='right')

st.pyplot(fig)

st.text("Bagaimana demografi pelanggan yang kita miliki?")
st.markdown("""
            kita dapat menyimpulkan bahwa sebagian besar pelanggan kita berasal dari state SP dengan total lebih dari 40.000 customers, diikuti state RJ dan State MG, dengan data yang ada kita dapat meningkatkan promosi di state yang masih memiliki customer sedikit agar semakin banyak customer yang berlangganan, untuk daerah yang sudah tinggi kita harus me maintenance atau bahkan meningkatkan customer."""
            )

st.header("Monthly Performance")

monthly_performance = company_revenue_df.groupby('month').agg({
    'order_id':'count', 'payment_value':'sum'
}).rename(columns={'order_id':'sales', 'payment_value':'revenue'})

fig, ax = plt.subplots(figsize=(10, 8))

ax.plot(monthly_performance.index, monthly_performance['sales'], marker='o', label='Sales')
ax.plot(monthly_performance.index, monthly_performance['revenue'], marker='o', label='Revenue')

ax.set_xlabel("Month")
ax.set_ylabel("Count / Value")
ax.set_title("Sales and Revenue Performance Over Time")
ax.legend()

st.pyplot(fig)