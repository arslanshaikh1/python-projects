# Advanced Student Grade Predictor (Excellence Level)
import streamlit as st

st.title("🧮 Advanced Calculator App")

# Input numbers
num1 = st.number_input("Pehla number enter karein:", value=0.0)
num2 = st.number_input("Dusra number enter karein:", value=0.0)

# Operation selection
operation = st.selectbox(
    "Operation select karein:",
    ("Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)")
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication (*)":
        result = num1 * num2
        st.success(f"Result: {num1} * {num2} = {result}")
    elif operation == "Division (/)":
        if num2 == 0:
            st.error("Error: Zero (0) se divide karna sambhav nahi hai!")
        else:
            result = num1 / num2
            st.success(f"Result: {num1} / {num2} = {result}")


   
