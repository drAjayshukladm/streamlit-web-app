import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

# Define weight (in kg) and height (in cm) ranges
weights_kg = np.arange(40, 115, 5)  # 40 to 110 kg in steps of 5
heights_cm = np.arange(140, 190, 5)  # 140 to 185 cm in steps of 5

# Convert height to meters
heights_m = heights_cm / 100

# Create a BMI grid
bmi_grid = np.zeros((len(heights_cm), len(weights_kg)))

for i, height in enumerate(heights_m):
    bmi_grid[i, :] = weights_kg / (height ** 2)

# Define BMI categories and lighter colors for better readability
categories = ['Underweight', 'Normal range', 'Overweight', 'Obese', 'Morbidly Obese']
colors = ['#ffffcc', '#ccebc5', '#ffedb3', '#fbb4ae', '#b3cde3']  # Lighter colors
cmap = ListedColormap(colors)
bounds = [0, 18.5, 23, 25, 30, 100]
norm = BoundaryNorm(bounds, cmap.N)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the BMI grid as a table
c = ax.pcolormesh(weights_kg, heights_cm, bmi_grid, cmap=cmap, norm=norm, edgecolors='w', linewidth=1)

# Add text to each cell with improved visibility
for i in range(len(heights_cm)):
    for j in range(len(weights_kg)):
        ax.text(weights_kg[j], heights_cm[i], f"{bmi_grid[i, j]:.1f}", va='center', ha='center', fontsize=8, color='black')

# Ask user for their weight and height
user_weight = float(input("Enter your weight in kg: "))
user_height_cm = float(input("Enter your height in cm: "))
user_height_m = user_height_cm / 100

# Calculate user's BMI
user_bmi = user_weight / (user_height_m ** 2)

# Plot user's BMI on the chart
ax.plot(user_weight, user_height_cm, 'ro', markersize=10, label=f'Your BMI: {user_bmi:.1f}')
ax.legend(loc='upper right')

# Set axis labels and title
ax.set_xlabel('Weight (kg)')
ax.set_ylabel('Height (cm)')
ax.set_title('Body Mass Index (BMI) Chart')

# Customize ticks
ax.set_xticks(weights_kg)
ax.set_yticks(heights_cm)

# Create a custom legend with lighter colors
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, edgecolor='w', label=category) for category, color in zip(categories, colors)]
plt.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.show()
