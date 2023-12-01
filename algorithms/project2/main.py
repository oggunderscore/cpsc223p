"""
Function to return the total max stocks purchasable
params;
    n = Number of stocks available to trade
    stocks_and_values = Stocks array that contains the number of stocks to buy and total value of stocks
    amount = maximum amount to spend investing into stocks (cannot exceed)
"""


def stock_purchase_maximization(n, stocks_and_values, amount):
    # Initialize a memoization table with default values of -1
    memo = [[-1] * (amount + 1) for _ in range(n + 1)]

    # Helper function for recursive dynamic programming
    def max_stocks(index, remaining_amount):
        # Base case: If we have processed all stocks or remaining_amount is 0
        if index == 0 or remaining_amount == 0:
            return 0

        # Check if the result is already memoized
        if memo[index][remaining_amount] != -1:
            return memo[index][remaining_amount]

        # If the current stock cost is more than the remaining_amount, skip it
        if stocks_and_values[index - 1][1] > remaining_amount:
            result = max_stocks(index - 1, remaining_amount)
        else:
            # Compare options: include or exclude the current stock
            include_current = stocks_and_values[index - 1][0] + max_stocks(
                index - 1, remaining_amount - stocks_and_values[index - 1][1]
            )
            exclude_current = max_stocks(index - 1, remaining_amount)
            result = max(include_current, exclude_current)

        # Memoize the result and return
        memo[index][remaining_amount] = result
        return result

    # Call the helper function with the given parameters
    return max_stocks(n, amount)


# Sample input 1
N1 = 4
stocks_and_values1 = [[1, 2], [4, 3], [5, 6], [6, 7]]
amount1 = 12
output1 = stock_purchase_maximization(N1, stocks_and_values1, amount1)
print("Sample Output 1:", output1)

# Sample input 2
N2 = 4
stocks_and_values2 = [[3, 2], [4, 3], [5, 3], [6, 7]]
amount2 = 10
output2 = stock_purchase_maximization(N2, stocks_and_values2, amount2)
print("Sample Output 2:", output2)
