import pandas as pd
import numpy as np
from scipy import integrate, stats
import time

# # Define a simple function
# def integrand(x):
#     return x**2

# # Compute the integral of the function
# result, _ = integrate.quad(integrand, 0, 1)
# print("Integral of x^2 from 0 to 1:", result)


# # 50 days of steps, lowest day being 3000 steps, highest being 10000 steps
# daily_steps = np.random.randint(3000, 10000, size=50)

# mean_np = np.mean(daily_steps)
# median_np = np.median(daily_steps)
# variance_np = np.var(daily_steps)
# std_dev_np = np.std(daily_steps)

# mean_scipy = stats.tmean(daily_steps)
# median_scipy = np.median(daily_steps)  # SciPy does not have a separate median function
# variance_scipy = stats.tvar(daily_steps)
# std_dev_scipy = stats.tstd(daily_steps)



import pandas as pd
import numpy as np

# Simulating stock prices for a non-existent stock (DVLPRS)
np.random.seed(0)  # For reproducibility

# Generating 100 days of stock prices
dates = pd.date_range(start='2023-01-01', periods=100)
prices = np.random.normal(loc=100, scale=10, size=len(dates))  # Assume a mean price of 100 with a standard deviation of 10

# Creating a DataFrame
stock_data = pd.DataFrame({
    'Date': dates,
    'DVLPRS_Price': prices
})

# Displaying the first few rows of the simulated data
print(stock_data.head())

