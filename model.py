import pandas as pd


def project_pension(start_amount, retirement_age, cola, max_age=110):
    ages = range(retirement_age, max_age + 1)
    benefit_amount = [
        start_amount * (1 + cola) ** i for i in range(max_age - retirement_age + 1)
    ]
    return pd.DataFrame({
        "age": ages,
        "benefit_amount": benefit_amount
    })
