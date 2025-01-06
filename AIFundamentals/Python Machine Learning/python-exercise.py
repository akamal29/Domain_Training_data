# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Create a synthetic dataset
np.random.seed(42)  # For reproducibility

# Generating synthetic data
data_size = 500
car_sales_data = {
    'Make': np.random.choice(['Ford', 'Chevrolet', 'Honda', 'Toyota', 'BMW'], size=data_size),
    'Model': np.random.choice(['Model A', 'Model B', 'Model C', 'Model D'], size=data_size),
    'Year': np.random.randint(2000, 2023, size=data_size),
    'Mileage': np.random.randint(5000, 200000, size=data_size),
    'Price': np.random.randint(5000, 30000, size=data_size)
}

car_sales_df = pd.DataFrame(car_sales_data)

# Display the first few rows of the DataFrame
print("First 5 rows of the synthetic Car Sales dataset:")
print(car_sales_df.head())

# Step 2: Data Preprocessing
# Checking for missing values
print("\nMissing values in each column:")
print(car_sales_df.isnull().sum())

# Basic data cleaning: Dropping unnecessary columns (if any)
# Here, there are no unnecessary columns since it's a synthetic dataset.

# Encoding categorical variables
car_sales_df = pd.get_dummies(car_sales_df, drop_first=True)

# Visualizing the distribution of the target variable (Price)
plt.figure(figsize=(10, 6))
sns.histplot(car_sales_df['Price'], bins=30, kde=True)
plt.title('Distribution of Car Prices')
plt.xlabel('Car Price')
plt.ylabel('Frequency')
plt.show()

# Data Visualization: Correlation Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(car_sales_df.corr(), annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Heatmap')
plt.show()

# Preparing the data for machine learning
# Selecting features and target variable
X = car_sales_df.drop(['Price'], axis=1)  # Features
y = car_sales_df['Price']                   # Target variable

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Building and training the Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nMean Squared Error:", mse)
print("R-squared Score:", r2)

# Feature Importance
feature_importances = model.feature_importances_
sorted_indices = np.argsort(feature_importances)[::-1]
plt.figure(figsize=(10, 6))
plt.barh(range(len(sorted_indices)), feature_importances[sorted_indices], align='center')
plt.yticks(range(len(sorted_indices)), X.columns[sorted_indices])
plt.title('Feature Importance in Car Price Prediction')
plt.xlabel('Importance Score')
plt.show()