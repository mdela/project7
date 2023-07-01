import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Step 1: Load and prepare the data
data = pd.read_excel("mileage.xlsx")  # Replace "mileage.xlsx" with your actual file name

# Step 2: Create the feature matrix X and the target variable y
X = data[['mpg']]
y = data['miles']

# Step 3: Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Step 4: Predict the number of miles for a range of MPG values
min_mpg = 42  # Minimum MPG value to consider
max_mpg = 49  # Maximum MPG value to consider
num_mpg_values = (max_mpg - min_mpg) + 1  # Number of MPG values to predict

mpg_values = np.linspace(min_mpg, max_mpg, num_mpg_values).reshape(-1, 1)
predicted_miles = model.predict(mpg_values)

# Step 5: Print the predicted number of miles for each MPG value
for mpg, miles in zip(mpg_values, predicted_miles):
    print("MPG:", int(mpg[0]), "Predicted Miles:", round(miles))

# Additional steps and code can be added based on your requirements