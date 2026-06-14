def SeatsAvailable():
    return {1:20000,
            2:30000,
            3:10000,
            4:20000}  
    
def BandPriceOptions():
    return {
        1: {50: 100, 65:85, 90:60, 100:40, 110:20, 120:10},
        2: {40: 100, 50:85, 75:60, 80:40, 90:20, 100:10},
        3: {25: 100, 40:85, 60:60, 70:40, 85:20, 100:10},
        4: {10: 100, 15:85, 35:60, 45:40, 50:20, 60:10}
    }
        
def CalculateBandSales(price, band):
    capacityOptions = SeatsAvailable()  # Get the available seats for each band
    bandPriceOptions = BandPriceOptions()  # Get the price options for each band
    if band not in capacityOptions:
        raise KeyError(f"Unknown band: {band}")
    if band not in bandPriceOptions or price not in bandPriceOptions[band]:
        raise KeyError(f"Unknown price option for band {band}: {price}")
    availableSeats = capacityOptions[band]  # Get the available seats for the given band
    salesPercentage = bandPriceOptions[band][price]  # Get the percentage of tickets sold for the given price   
    return price * (salesPercentage / 100) * availableSeats  # Calculate sales based on available seats

def GetBandPrices(band):
    """Get the prices for a specific band."""
    bandPriceOptions = BandPriceOptions()
    if band not in bandPriceOptions:
        raise KeyError(f"Unknown band: {band}")
    return bandPriceOptions[band].keys()  # Return the available prices for the given band

# def CalculateTicketSales():
#     """Calculate total ticket sales."""
#     band1Sales = CalculateBandSales(50, 1)
#     band2Sales = CalculateBandSales(40, 2)
#     band3Sales = CalculateBandSales(25, 3)
#     band4Sales = CalculateBandSales(10, 4)
#     ticketSales = band1Sales + band2Sales + band3Sales + band4Sales  # Add sales from all bands
#     return ticketSales  # Placeholder value for ticket sales
