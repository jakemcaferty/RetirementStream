import streamlit as st
from datetime import datetime

from model import project_pension

# Title of the app
st.title("Retirement Projection Calculator")

with st.sidebar:
    st.header("Enter your details")

    birth_date = st.date_input("Birth Date", datetime(1967, 1, 1))
    start_date = st.date_input(
        "Employment Start Date", datetime(1987, 1, 1), min_value=datetime(1975, 1, 1)
    )
    retirement_date = st.date_input(
        "Retirement Date", datetime(2030, 1, 1), min_value=datetime.today()
    )

    st.header("Retirement Assumptions")
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
    if retirement_date <= start_date:
        st.error("Retirement date must be after the start date.")
    else:
        years_of_service = (retirement_date - start_date).days / 365.25
    annual_cola = st.number_input(
        "Cost of Living Adjustment",
        value=0.025,
        min_value=0.0,
        max_value=0.0301,
        step=0.001,
        format="%.5f",
    )

    average_salary = sum(salaries) / len(salaries)
    annual_pension = average_salary * years_of_service * 0.02
    retirement_age = int((retirement_date - birth_date).days / 365.25)

# Display results
st.header("Retirement Projection Results")
st.write(f"Years of Service: {years_of_service:.2f} years")
st.write(f"Average Salary (Last 5 Years): ${average_salary:,.2f}")
st.write(f"Estimated Annual Pension: ${annual_pension:,.2f}")

pension_df = project_pension(annual_pension, retirement_age, annual_cola)
st.line_chart(pension_df, x="age", y="benefit_amount")
st.dataframe(pension_df)

st.write(
    "_Disclaimer: This tool is for educational purposes only and should not be used for financial planning or relied on for accurate modeling.  You should consult a financial professional when making retirement decisions."
)
