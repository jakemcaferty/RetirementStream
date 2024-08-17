import streamlit as st
from datetime import datetime

# Title of the app
st.title("Retirement Projection Calculator")

with st.sidebar:
    st.header("Enter your details")
    with st.expander("Salary History"):
        salaries = [
            st.number_input(
                f"Year {i} Salary",
                min_value=0.0,
                value=round(75000.0 * 1.03 ** (i - 1), 0),
                step=1000.0,
            )
            for i in range(1, 6)
        ]

    start_date = st.date_input(
        "Employment Start Date", datetime(2000, 1, 1), min_value=datetime(1975, 1, 1)
    )
    retirement_date = st.date_input(
        "Retirement Date", datetime(2030, 1, 1), min_value=datetime.today()
    )
    if retirement_date <= start_date:
        st.error("Retirement date must be after the start date.")
    else:
        years_of_service = (retirement_date - start_date).days / 365.25

    average_salary = sum(salaries) / len(salaries)
    annual_pension = average_salary * years_of_service * 0.02

# Display results
st.header("Retirement Projection Results")
st.write(f"Years of Service: {years_of_service:.2f} years")
st.write(f"Average Salary (Last 5 Years): ${average_salary:,.2f}")
st.write(f"Estimated Annual Pension: ${annual_pension:,.2f}")
