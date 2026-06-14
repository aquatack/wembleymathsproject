


def calculateIncome():
    """Calculate total income."""

    def TicketSales():
        """Calculate total ticket sales."""
        def SeatsAvailable():
            return {1:20000,
                    2:30000,
                    3:10000,
                    4:20000}  
        
        def GetBand1PriceOptions():
            return {50: 100, 65:85, 90:60, 100:40, 110:20, 120:10}  # Price to percentage mapping for Band 1 tickets
        def GetBand2PriceOptions():
            return {40: 100, 50:85, 75:60, 80:40, 90:20, 100:10}  # Price to percentage mapping for Band 2 tickets
        def GetBand3PriceOptions():
            return {25: 100, 40:85, 60:60, 70:40, 85:20, 100:10}  # Price to percentage mapping for Band 3 tickets
        def GetBand4PriceOptions():
            return {10: 100, 15:85, 35:60, 45:40, 50:20, 60:10}  # Price to percentage mapping for Band 4 tickets
        
        
        def CalculateBandSales(price, priceOptions, availableSeats):
            salesPercentage = priceOptions.get(price, 0)  # Get the percentage of tickets sold for the given price   
            return price * (salesPercentage / 100) * availableSeats  # Calculate sales based on available seats

        band1Sales = CalculateBandSales(50, GetBand1PriceOptions(), SeatsAvailable()[1])
        band2Sales = CalculateBandSales(40, GetBand2PriceOptions(), SeatsAvailable()[2])
        band3Sales = CalculateBandSales(25, GetBand3PriceOptions(), SeatsAvailable()[3])
        band4Sales = CalculateBandSales(10, GetBand4PriceOptions(), SeatsAvailable()[4])
        ticketSales = band1Sales + band2Sales + band3Sales + band4Sales  # Add sales from all bands
        return ticketSales  # Placeholder value for ticket sales

    def ProgrammeSales():
        """Calculate total programme sales."""
        return 0  # Placeholder value for programme sales

    def MerchandiseSales():
        """Calculate total merchandise sales."""
        return 0  # Placeholder value for merchandise sales

    def FoodAndDrinkSales():
        """Calculate total food and drink sales."""
        return 0  # Placeholder value for food and drink sales

    ticket_sales = TicketSales()
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
