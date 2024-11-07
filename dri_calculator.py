import streamlit as st

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

