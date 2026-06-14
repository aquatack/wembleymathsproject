def calculateIncome():
	"""Calculate total income."""
	return 100000  # Placeholder value for income


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
