import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch

def bmi_chart():
    st.write("## BMI Chart Based on Weight and Height")

    # Define weight (in kg) and height (in cm) ranges
    weights_kg = np.arange(40, 115, 5)  # 40 to 110 kg in steps of 5
    heights_cm = np.arange(140, 190, 5)  # 140 to 185 cm in steps of 5
    heights_m = heights_cm / 100  # Convert height to meters

    # Create a BMI grid
    bmi_grid = np.zeros((len(heights_cm), len(weights_kg)))
    for i, height in enumerate(heights_m):
        bmi_grid[i, :] = weights_kg / (height ** 2)

    # Define BMI categories and colors
    categories = ['Underweight', 'Normal range', 'Overweight', 'Obese', 'Morbidly Obese']
    colors = ['#ffffcc', '#ccebc5', '#ffedb3', '#fbb4ae', '#b3cde3']
    cmap = ListedColormap(colors)
    bounds = [0, 18.5, 23, 25, 30, 100]
    norm = BoundaryNorm(bounds, cmap.N)

    # User input for weight and height
    user_weight = st.number_input("Enter your weight (kg):", min_value=30.0, max_value=150.0, step=0.1)
    user_height_cm = st.number_input("Enter your height (cm):", min_value=120.0, max_value=220.0, step=0.1)
    user_height_m = user_height_cm / 100
    user_bmi = user_weight / (user_height_m ** 2)

    # Create plot
    fig, ax = plt.subplots(figsize=(12, 6))
    c = ax.pcolormesh(weights_kg, heights_cm, bmi_grid, cmap=cmap, norm=norm, edgecolors='w', linewidth=1)

    # Add text to each cell for better visibility
    for i in range(len(heights_cm)):
        for j in range(len(weights_kg)):
            ax.text(weights_kg[j], heights_cm[i], f"{bmi_grid[i, j]:.1f}", va='center', ha='center', fontsize=8, color='black')

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
    legend_elements = [Patch(facecolor=color, edgecolor='w', label=category) for category, color in zip(categories, colors)]
    ax.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    # Display plot in Streamlit
    st.pyplot(fig)

# Add to main app function


def main():
    st.title("DRI Calculator for Adults")

    st.write("### Age and Gender")
    age = st.number_input("Age (years):", min_value=0, max_value=120, step=1)
    gender = st.radio("Gender", ["Male", "Female"])

    st.write("### Weight and Height")
    weight = st.number_input("Weight (kg):", min_value=0.0, step=0.1)
    height = st.number_input("Height (cm):", min_value=0.0, step=0.1)

    bmi = (weight * 10000) / (height * height)
    ht_inch = height / 2.54
    feet = int(ht_inch / 12)
    inch = ht_inch % 12

    st.write(f"**BMI**: {bmi:.2f} kg/m²")
    st.write(f"**Height**: {feet} feet and {inch:.1f} inches")

    ree = 900 + 10 * weight if gender == "Male" else 700 + 7 * weight
    ibw = 50 + 2.3 * (ht_inch - 60) if gender == "Male" else 45.5 + 2.3 * (ht_inch - 60)

    st.write("### Physical Activity Level")
    activity_level = st.selectbox("Choose activity level:", 
                                  ["Sedentary", "Low Active", "Active", "Very Active"])
    activity_multiplier = {"Sedentary": 1.2, "Low Active": 1.4, "Active": 1.6, "Very Active": 1.8}[activity_level]
    eer = activity_multiplier * ree
    st.write(f"**Estimated Energy Requirement (EER)**: {eer:.2f} kcal")

    st.write("### Protein Intake")
    protein_per_kg = st.number_input("Protein requirement (grams/kg):", min_value=0.0, step=0.1)
    protein_ibw = protein_per_kg * ibw
    protein_abw = protein_per_kg * (ibw + 0.4 * (weight - ibw))
    protein_current = protein_per_kg * weight
    st.write(f"Recommended protein (ideal body weight): {protein_ibw:.2f} grams/day")
    st.write(f"Recommended protein (adjusted body weight): {protein_abw:.2f} grams/day")
    st.write(f"Recommended protein (current body weight): {protein_current:.2f} grams/day")

    if gender == "Female":
        st.write("### Pregnancy/Lactation Status")
        pregnancy_status = st.selectbox("Select status:",
                                        ["Non-pregnant", "First Trimester", "Second Trimester (12-20 weeks)",
                                         "Second Trimester (≥20 weeks)", "Third Trimester", 
                                         "Lactating (0-6 months)", "Lactating (>6 months)"])
        if pregnancy_status == "Non-pregnant":
            st.write("RDA for Calcium: 1000 mg/day")
            st.write("RDA for Iron: 40 mg/day")
            # Add other nutrient requirements based on pregnancy_status

    st.write("### Nutritional Recommendations for General Reference")
    # Here include other general RDAs, protein recommendations, etc., as per ICMR-NIN 2020 standards

if __name__ == "__main__":
    main()

  
