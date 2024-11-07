import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch

# Function to display the BMI Chart
def bmi_chart():
    st.write("## BMI Chart Based on Weight and Height")

    weights_kg = np.arange(40, 115, 5)
    heights_cm = np.arange(140, 190, 5)
    heights_m = heights_cm / 100

    bmi_grid = np.zeros((len(heights_cm), len(weights_kg)))
    for i, height in enumerate(heights_m):
        bmi_grid[i, :] = weights_kg / (height ** 2)

    categories = ['Underweight', 'Normal range', 'Overweight', 'Obese', 'Morbidly Obese']
    colors = ['#ffffcc', '#ccebc5', '#ffedb3', '#fbb4ae', '#b3cde3']
    cmap = ListedColormap(colors)
    bounds = [0, 18.5, 23, 25, 30, 100]
    norm = BoundaryNorm(bounds, cmap.N)

    user_weight = weight
    #st.number_input("Enter your weight (kg):", min_value=30.0, max_value=150.0, step=0.1)
    user_height_cm =height
    #st.number_input("Enter your height (cm):", min_value=120.0, max_value=220.0, step=0.1)
    user_height_m = user_height_cm / 100
    user_bmi = user_weight / (user_height_m ** 2)

    fig, ax = plt.subplots(figsize=(12, 6))
    c = ax.pcolormesh(weights_kg, heights_cm, bmi_grid, cmap=cmap, norm=norm, edgecolors='w', linewidth=1)

    for i in range(len(heights_cm)):
        for j in range(len(weights_kg)):
            ax.text(weights_kg[j], heights_cm[i], f"{bmi_grid[i, j]:.1f}", va='center', ha='center', fontsize=8, color='black')

    ax.plot(user_weight, user_height_cm, 'ro', markersize=10, label=f'Your BMI: {user_bmi:.1f}')
    ax.legend(loc='upper right')

    ax.set_xlabel('Weight (kg)')
    ax.set_ylabel('Height (cm)')
    ax.set_title('Body Mass Index (BMI) Chart')

    ax.set_xticks(weights_kg)
    ax.set_yticks(heights_cm)

    legend_elements = [Patch(facecolor=color, edgecolor='w', label=category) for category, color in zip(categories, colors)]
    ax.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    st.pyplot(fig)

# Main function for the app
def main():
    st.title("DRI and RDA Calculator for Adults")

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
    lbw = (9270 * weight) / (6680 + 216 + bmi) if gender == "Male" else (9270 * weight) / (8780 + 244 + bmi)

    st.write(f"**Resting Energy Expenditure (REE)**: {ree:.2f} kcal")
    st.write(f"**Lean Body Weight (LBW)**: {lbw:.2f} kg")
    st.write(f"**Ideal Body Weight (IBW)**: {ibw:.2f} kg")

    st.write("### Physical Activity Level")
    activity_level = st.selectbox("Choose activity level:", 
                                  ["Daily activities only", "30 minutes moderate activity", "60 minutes moderate/30 vigorous", "45-60 minutes vigorous"])
    activity_multiplier = {"Daily activities only": 1.2, "30 minutes moderate activity": 1.4, "60 minutes moderate/30 vigorous": 1.6, "45-60 minutes vigorous": 1.8}[activity_level]
    eer = activity_multiplier * ree
    fibre = (eer * 14) / 1000
    st.write(f"**Estimated Energy Requirement (EER)**: {eer:.2f} kcal")
    st.write(f"**Recommended Daily Fibre Intake**: {fibre:.2f} grams")

    st.write("### Protein Intake")
    protein_per_kg = st.number_input("Protein requirement (grams/kg):", min_value=0.0, step=0.1)
    protein_ibw = protein_per_kg * ibw
    abw = ibw + 0.4 * (weight - ibw)
    protein_abw = protein_per_kg * abw
    protein_current = protein_per_kg * weight
    st.write(f"Protein (IBW): {protein_ibw:.2f} g/day")
    st.write(f"Protein (ABW): {protein_abw:.2f} g/day")
    st.write(f"Protein (Current Weight): {protein_current:.2f} g/day")

    if gender == "Female":
        st.write("### Pregnancy/Lactation Status")
        preg_status = st.selectbox("Select status:", 
                                   ["Non-pregnant", "First Trimester", "Second Trimester (12-20 weeks)", 
                                    "Second Trimester (≥20 weeks)", "Third Trimester", "Lactating (0-6 months)", 
                                    "Lactating (>6 months)"])
        if preg_status == "Non-pregnant":
            st.write("**RDA for Non-pregnant**")
            st.write("Calcium: 1000 mg/d")
            st.write("Iron: 40 mg/d")
            st.write("Iodine: 150 mcg/d")
            st.write("Folate: 220 mcg/d")
            st.write("Vitamin B12: 2.5 mcg/d")
            st.write("Vitamin A: 840 mcg/d")
            st.write("Vitamin D: 600 IU/d")
        elif preg_status == "First Trimester":
            st.write("Additional energy: 350 kcal")
            st.write("Protein increase: 23 g/day")
        elif preg_status == "Second Trimester (12-20 weeks)":
            st.write("Calcium: 1200 mg/d, Iron: 35 mg/d")
            st.write("Additional energy: 350 kcal")
            st.write("Protein increase: 23 g/day")
        elif preg_status == "Lactating (0-6 months)":
            st.write("Additional energy: 600 kcal")
            st.write("Protein increase: 19 g/day")
        elif preg_status == "Lactating (>6 months)":
            st.write("Additional energy: 520 kcal")
            st.write("Protein increase: 13 g/day")

    else:
        st.write("**RDA for Males**")
        st.write("Calcium: 600 mg/d")
        st.write("Iron: 17 mg/d")

    bmi_chart()

if __name__ == "__main__":
    main()
