import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib.ticker import ScalarFormatter


# Step 1: Read the Excel file
file_path = '3 charts.xlsx'
df = pd.read_excel(file_path, sheet_name='for Service Producing Industry', header=None)

# Step 2: Prepare the data
years = df.iloc[0, 1:].values
sectors = df.iloc[1:, 0].values
data = df.iloc[1:, 1:].values

# Step 3: Predict the next 5 years using Linear Regression
future_years = np.arange(2024, 2029)
all_years = np.append(years, future_years)

all_years = np.append(years, future_years)

predictions = []
for sector_data in data:
    X = np.array(years).reshape(-1, 1)
    y = np.array(sector_data)
    model = LinearRegression().fit(X, y)
    future_predictions = model.predict(future_years.reshape(-1, 1))
    predictions.append(np.append(sector_data, future_predictions))

# Step 4: Plot the data and predictions
plt.figure(figsize=(12, 6))  # Increase the figure size
for i, sector in enumerate(sectors):
    plt.plot(years, data[i], label=f'{sector} (Actual)', linestyle='-')
    plt.plot(all_years, predictions[i], label=f'{sector} (Predicted)', linestyle=':', color=plt.gca().lines[-1].get_color())

# Set x-axis scale with 2-year difference
plt.xticks(np.arange(min(all_years), max(all_years) + 1, 2))

plt.xlabel('Year')
plt.ylabel('Number of Employments')
plt.title('Employment Trends with Predictions for Next 5 Years for Service Producing Industry in Ontario')

# Position the legend in the upper right corner inside the plot area
# plt.legend(loc='upper right')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)  # Adjust legend location

# Set y-axis to display full digits
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().ticklabel_format(style='plain', axis='y')

plt.grid(True)
plt.tight_layout()  # Adjust the layout
plt.show()