def calculate_percentage_difference(paid, current):
    try:
        # Ensure both inputs are numbers
        paid = float(paid)
        current = float(current)

        # Calculate percentage difference
        percentage_difference = ((current - paid) / abs(paid)) * 100

        return percentage_difference
    except ValueError:
        print("Error: Please provide valid numeric inputs.")
