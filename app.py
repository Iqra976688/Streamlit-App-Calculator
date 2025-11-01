# app.py
import streamlit as st

# App title
st.set_page_config(page_title="Simple Calculator 🧮", page_icon="🧮")
st.title("🧮 Simple Calculator")
st.write("A basic calculator built with Streamlit")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox("Select operation", ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"])

# Perform calculation
if st.button("Calculate"):
    if operation == "Add (+)":
        result = num1 + num2
    elif operation == "Subtract (-)":
        result = num1 - num2
    elif operation == "Multiply (×)":
        result = num1 * num2
    elif operation == "Divide (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("❌ Cannot divide by zero!")
            result = None
    
    if result is not None:
        st.success(f"✅ Result: {result}")
