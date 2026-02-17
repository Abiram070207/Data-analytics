import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp
from scipy.optimize import minimize
import statsmodels.api as sm

print("NumPy Examples:")

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean of array:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

matrix = np.random.rand(3, 3)
print("\nMatrix:")
print(matrix)

print("Matrix Transpose:")
print(matrix.T)

print("Dot Product:")
print(np.dot(matrix, matrix.T))


print("\nSciPy Examples:")

t_stat, p_value = ttest_1samp(arr, 3)
print("T-statistic:", t_stat)
print("P-value:", p_value)

result = minimize(lambda x: x**2 + 5, 0)
print("\nOptimization Result:", result)


print("\nPandas Examples:")

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())


print("\nReading from Text File:")

with open('sample.txt', 'w') as f:
    f.write(
        "Name,Age,Salary\n"
        "Alice,25,50000\n"
        "Bob,30,60000\n"
        "Charlie,35,70000"
    )

df_text = pd.read_csv('Sample.txt')
print(df_text)


print("\nReading from Excel File:")

df.to_excel('sample.xlsx', index=False)

df_excel = pd.read_excel('sample.xlsx')
print(df_excel)


print("\nReading from Web:")

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"

df_web = pd.read_csv(url)
print(df_web.head())


print("\nStatsmodels Example:")

X = sm.add_constant([4, 5, 6])
Y = [1, 2, 3]

model = sm.OLS(Y, X).fit()
print(model.summary())
