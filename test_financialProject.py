import pytest
from financialProject import calculateProfit, calculateIncome, calculateCosts

def test_calculate_profit_positive():
    income = 1000
    assert calculateProfit(income, 300) == 700

def test_calculate_profit_zero():
    assert calculateProfit(100, 100) == 0

def test_calculate_profit_negative():
    assert calculateProfit(100, 500) == -400