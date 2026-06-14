import ticketSales

def ProgrammeSales():
    """Calculate total programme sales."""
    return 0  # Placeholder value for programme sales

def MerchandiseSales():
    """Calculate total merchandise sales."""
    return 0  # Placeholder value for merchandise sales

def FoodAndDrinkSales():
    """Calculate total food and drink sales."""
    return 0  # Placeholder value for food and drink sales

def calculateIncome():
    """Calculate total income."""

    ticket_sales = ticketSales.CalculateTicketSales()
    programme_sales = ProgrammeSales()
    merchandise_sales = MerchandiseSales()
    food_and_drink_sales = FoodAndDrinkSales()
    return ticket_sales + programme_sales + merchandise_sales + food_and_drink_sales



def calculateCosts():
    """Calculate total costs."""
    return 75000  # Placeholder value for costs


def calculateProfit(income, costs):
    """Calculate profit from income and costs."""
    return income - costs


def __main__(*args, **kwargs):
    """Main function to execute financial calculations."""
    income = calculateIncome()
    costs = calculateCosts()
    profit = calculateProfit(income, costs)
    print(f"Total Income: {income}")
    print(f"Total Costs: {costs}")
    print(f"Profit: {profit}")

if __name__ == '__main__':
    __main__()
