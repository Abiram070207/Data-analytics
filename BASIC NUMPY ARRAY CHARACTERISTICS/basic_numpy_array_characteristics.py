import statsmodels.api as sm
import numpy as np
X = np.array([1, 2, 3, 4, 5]) # Independent variable (X)
y = np.array([1.2, 1.9, 3.2, 3.8, 5.1]) #Dependent variable (y)
X = sm.add_constant(X) # Adding constant
model = sm.OLS(y, X) # Ordinary Least Squares (OLS) regression
results = model.fit()
print(results.summary()) # Summary of the regression results
predicted = results.predict(X) # Predicted values
print("\nPredicted values:", predicted)