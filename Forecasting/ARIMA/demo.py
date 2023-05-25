# import itertools
# from statsmodels.tsa.arima.model import ARIMA

# data = [759.0, 773.3125, 593.75, 523.375, 763.125, 768.8125, 743.75, 750.0625, 751.625, 593.9375,
#         500.5, 747.0, 738.8125, 782.4375, 785.0625, 777.25, 596.375, 487.0625, 719.4375, 767.75,
#         765.25, 755.3125, 777.9375, 605.1875, 510.375, 732.0625, 747.5, 749.625, 758.1875, 742.3125]
#   # Your dataset of 30 values

# # Define the range of p, d, and q values
# p_values = range(0, 6)  # Change the range as needed
# d_values = range(0, 3)  # Change the range as needed
# q_values = range(0, 6)  # Change the range as needed

# # Generate all possible combinations of p, d, and q
# order_combinations = list(itertools.product(p_values, d_values, q_values))

# # Iterate over each order combination and fit the ARIMA model
# for order in order_combinations:
#     try:
#         model = ARIMA(data, order=order).fit()
#         print(f"Order {order}: AIC = {model.aic}, BIC = {model.bic}")
#     except:
#         continue
