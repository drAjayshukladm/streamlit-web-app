import streamlit as st

st.title("DRI Calculator based on Weight, Gender, and Pregnancy for Adults")
st.subheader("Based on RDA for Indians 2020")

# User input for age, gender, weight, and height
age = st.number_input("Enter Age (years):", min_value=0, max_value=120, step=1)
gender = st.radio("Select Gender:", options=["Male", "Female"])
weight = st.number_input("Enter Weight (kg):", min_value=0.0, step=0.1)
height = st.number_input("Enter Height (cm):", min_value=0.0, step=0.1)

# Calculate BMI
bmi = (weight * 10000) / (height ** 2)
ht_inch = height / 2.54
feet = int(ht_inch // 12)
inch = ht_inch % 12

st.write(f"Weight (Kg): {weight}")
st.write(f"Height (cm): {height}")
st.write(f"BMI (kg/m²): {bmi:.2f}")
st.write(f"Height: {feet} feet and {int(inch)} inches")

# Resting Energy Expenditure and Ideal Body Weight
if gender == "Male":
    ree = 900 + 10 * weight
    ibw = 50 + 2.3 * (ht_inch - 60)
    lbw = (9270 * weight) / (6680 + 216 + bmi)
else:
    ree = 700 + 7 * weight
    ibw = 45.5 + 2.3 * (ht_inch - 60)
    lbw = (9270 * weight) / (8780 + 244 + bmi)

st.write(f"Resting Energy Expenditure (REE): {ree:.2f} kcal")
st.write(f"Ideal Body Weight (IBW): {ibw:.2f} kg")
st.write(f"Lean Body Weight (LBW): {lbw:.2f} kg")

# Activity Level
activity_level = st.selectbox("Select Activity Level:", options=[
    "Sedentary (Daily activities such as housework or gardening)",
    "Low Active (30 min of moderate activity, e.g., walking 4 mph)",
    "Active (60 min of moderate activity or 30 min vigorous)",
    "Very Active (45-60 min of vigorous activity)"
])
activity_multiplier = [1.2, 1.4, 1.6, 1.8][
    ["Sedentary", "Low Active", "Active", "Very Active"].index(activity_level.split()[0])]
eer = ree * activity_multiplier
fibre = (eer * 14) / 1000

st.write(f"Estimated Energy Requirement (EER): {eer:.2f} kcal")
st.write(f"Recommended Daily Fibre Intake: {fibre:.2f} grams")

# Pregnancy or Lactation Status (if female)
if gender == "Female":
    pregnancy_status = st.selectbox("Pregnancy/Lactation Status:", options=[
        "Non-pregnant", "First Trimester", "Second Trimester (12-20 weeks)", 
        "Second Trimester (20+ weeks)", "Third Trimester",
        "Lactating (0-6 months)", "Lactating (>6 months)"
    ])

    if pregnancy_status == "Non-pregnant":
        st.write("Non-pregnant")
        st.write("RDA Calcium: 1000 mg/day")
        st.write("RDA Iron: 40 mg/day")
        st.write("RDA Iodine: 150 mcg/day")
        st.write("RDA Folate: 220 mcg/day")
        st.write("RDA Vitamin B12: 2.5 mcg/day")
        st.write("RDA Vitamin A: 840 mcg/day")
        st.write("RDA Vitamin D: 600 IU/day")

    # Add more conditions for other pregnancy statuses similar to the non-pregnant block above
    # ...

# Protein Intake
st.write("### Protein Intake Calculation")
protein_per_kg = st.number_input("Enter Protein Requirement (g/kg):", min_value=0.0, step=0.1)
abw = ibw + 0.4 * (weight - ibw)
protein_ibw = protein_per_kg * ibw
protein_abw = protein_per_kg * abw
protein_current = protein_per_kg * weight

st.write(f"Adjusted Body Weight (ABW): {abw:.2f} kg")
st.write(f"Recommended Daily Protein (IBW): {protein_ibw:.2f} grams/day")
st.write(f"Recommended Daily Protein (ABW): {protein_abw:.2f} grams/day")
st.write(f"Recommended Daily Protein (Current Weight): {protein_current:.2f} grams/day")

# Additional information for male users
if gender == "Male":
    st.write("RDA Calcium: 600 mg/day")
    st.write("RDA Iron: 17 mg/day")
