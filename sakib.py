import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Excel data
file_path = "3 charts.xlsx"  # Update this with your actual file path
df = pd.read_excel(file_path, sheet_name='Stack Chart for Ontario', header=None)

# Extract categories (years) from the first row
years = df.iloc[0, 1:].values  # Skip the first column (column A) as it's the name of data

# Extract data from all rows starting from the second row and use the first column as labels
labels = df.iloc[1:, 0].values  # Labels are in the first column (column A)
data = df.iloc[1:, 1:].values   # Data starts from row 2 and column B onward

# Calculate percentages for each category within each year
data_percentage = data / data.sum(axis=0) * 100  # Normalize each column to 100%

# Create the stacked horizontal bar chart
bar_height = 0.6
ind = np.arange(len(years))  # the y locations for the groups

# Define a color palette excluding pink
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', 
    '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', 
    '#dbdb8d', '#9edae5'
]

# Plot each data row as a separate stack in the horizontal bar chart
bottom = np.zeros(len(years))

for i, (label, color) in enumerate(zip(labels, colors)):
    plt.barh(ind, data_percentage[i], label=label, color=color, left=bottom, height=bar_height)
    bottom += data_percentage[i]  # Update bottom to stack the next bar segment

# Customize the chart
plt.xlabel("Percentage (%)")
plt.ylabel("Years")
plt.title("Four Major Industries Stack Chart for Ontario")
plt.yticks(ind, years)
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.05), ncol=2)  # Adjust legend location

# Show plot
plt.tight_layout()
plt.show()