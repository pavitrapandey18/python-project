import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Sales Dashboard")

df = pd.read_csv("Project_csv.csv", encoding="latin1")
df["Year-Month"] = pd.to_datetime(df["Year-Month"])

st.success("Data loaded successfully!")

st.subheader("Raw Data")
st.dataframe(df)

profit_by_date=df.groupby("Year-Month")["Profit"].sum()
sales_by_category=df.groupby("Category")["Amount"].sum()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Profit Over Time")

    fig1, ax1 = plt.subplots()
    ax1.plot(profit_by_date.index, profit_by_date.values, marker='o')
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Profit")
    ax1.set_title("Profit Trend")

    st.pyplot(fig1)

with col2:
    st.subheader("Sales by Category")

    fig2, ax2 = plt.subplots()
    ax2.bar(sales_by_category.index, sales_by_category.values)
    ax2.set_xlabel("Category")
    ax2.set_ylabel("Total Sales")
    ax2.set_title("Sales by Category")

    st.pyplot(fig2)