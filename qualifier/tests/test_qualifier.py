# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

# def test_save_csv():
#     # @TODO: Your code here!
#     # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
def test_save_csv():
    csvpath = Path('./tests/data/output/qualifying_loans.csv')
    test_loans = [
        ["Bank of Big - Premier Option",300000,0.85,0.47,740,3.6],
        ["West Central Credit Union - Premier Option",400000,0.9,0.35,760,2.7],
        ["FHA Fredie Mac - Premier Option",600000,0.9,0.43,790,3.6],
        ["FHA Fannie Mae - Premier Option",500000,0.9,0.47,780,3.6],
        ["General MBS Partners - Premier Option",400000,0.95,0.35,790,3.0],
        ["Bank of Fintech - Premier Option",300000,0.9,0.47,740,3.15]
    ]
    fileio.save_csv(csvpath, test_loans)
    assert csvpath.exists()