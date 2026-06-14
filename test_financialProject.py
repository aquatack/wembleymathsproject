import pytest
from financialProject import calculateProfit, calculateIncome, calculateCosts
import ticketSales

# Test cases for financialProject.py
def test_Band1AvilablePrices():
    """Test available prices for Band 1."""
    expected_prices = {50, 65, 90, 100, 110, 120}
    assert set(ticketSales.GetBandPrices(1)) == expected_prices

def test_Band2AvilablePrices():
    """Test available prices for Band 2."""
    expected_prices = {40, 50, 75, 80, 90, 100}
    assert set(ticketSales.GetBandPrices(2)) == expected_prices

def test_Band3AvilablePrices():
    """Test available prices for Band 3."""
    expected_prices = {25, 40, 60, 70, 85, 100}
    assert set(ticketSales.GetBandPrices(3)) == expected_prices

def test_Band4AvilablePrices():
    """Test available prices for Band 4."""
    expected_prices = {10, 15, 35, 45, 50, 60}
    assert set(ticketSales.GetBandPrices(4)) == expected_prices

def test_Band1Sales_100pc():
    """Test Band 1 sales calculation."""
    """Capacity: 20000, Price: 50, Percentage Sold: 100%"""
    """Expected sales: 50 * 20000 * 100%= 1000000"""
    band1_sales = ticketSales.CalculateBandSales(50, 1)
    assert band1_sales == 1000000  # Replace with the expected value based on your calculation

def test_Band1Sales_85pc():
    """Test Band 1 sales calculation."""
    """Capacity: 20000, Price: 65, Percentage Sold: 85%"""
    """Expected sales: 65 * 20000 * 85%= 1105000"""
    band1_sales = ticketSales.CalculateBandSales(65, 1)
    assert band1_sales == 1105000  # Replace with the expected value based on your calculation

