import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define the diabetes distress categories
categories = [
    'Feeling that I am not as skilled at managing diabetes as I should be.',
    'Feeling that I don’t eat as carefully as I probably should.',
    'Feeling that I don’t notice the warning signs of hypoglycemia as well as I used to.',
    # Add all other questions here...
]

# Streamlit interface title and description
st.title("Diabetes Distress Assessment")
st.write("Please rate each statement on a scale from 1 to 6:")
st.write("1=Not a Problem, 2=A Slight Problem, 3=A Moderate Problem, 4=Somewhat Serious Problem, 5=A Serious Problem, 6=A Very Serious Problem")

# Collect responses for each question
responses = []
for i, question in enumerate(categories, start=1):
    rating = st.slider(f"{i}. {question}", 1, 6)
    responses.append(rating)

# Calculate the average score and display it
if st.button("Calculate Distress Scores"):
    score28 = sum(responses) / len(responses)
    st.write(f"Average T1-DDS score of 28 questions is {score28:.2f}")

    # Determine distress level
    if score28 < 2:
        st.write("Indicates little or no distress, as this score is less than 2.")
    elif 2 <= score28 < 3:
        st.write("Indicates moderate distress, as the average score is between 2.0 and 2.9.")
    else:
        st.write("Indicates high distress, as the average score is greater than 3.0.")

    # Subscale calculations
    subscales = {
        "Powerlessness": [responses[4], responses[8], responses[12], responses[20], responses[24]],
        "Management Distress": [responses[0], responses[7], responses[11], responses[27]],
        "Hypoglycemia Distress": [responses[2], responses[14], responses[21], responses[26]],
        "Negative Social Perceptions": [responses[3], responses[9], responses[18], responses[23]],
        "Eating Distress": [responses[1], responses[15], responses[22]],
        "Physician Distress": [responses[6], responses[13], responses[17], responses[25]],
        "Friend/Family Distress": [responses[5], responses[10], responses[16], responses[19]]
    }

    # Display subscale scores and determine if they are clinically significant
    scores = []
    for subscale_name, items in subscales.items():
        score = sum(items) / len(items)
        scores.append(score)
        st.write(f"{subscale_name} score: {score:.2f} out of max score 6")
        if score > 2:
            st.write(f"{subscale_name} score > 2.0 is considered clinically significant.")

    # Radar chart for subscale scores
    N = len(subscales)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    scores += scores[:1]  # Closing the loop

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.plot(angles, scores, 'o-', linewidth=2)
    ax.fill(angles, scores, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles[:-1]), list(subscales.keys()))
    ax.set_ylim(0, 6)
    st.pyplot(fig)

    # Bar chart for subscale scores
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(subscales.keys(), scores[:-1])  # Exclude the duplicated last score for bar chart
    ax.set_ylabel("Score (out of 6)")
    ax.set_title("Type 1 Diabetes Distress Subscale Scores")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)

    # Pie charts for each subscale
    fig, axes = plt.subplots(2, 4, figsize=(15, 8))
    axes = axes.flatten()
    for i, (subscale, score) in enumerate(subscales.items()):
        axes[i].pie([sum(score) / len(score), 6 - (sum(score) / len(score))],
                    labels=[f"{sum(score) / len(score):.2f}", f"{6 - (sum(score) / len(score)):.2f}"],
                    autopct='%1.1f%%', startangle=140, colors=["#66c2a5", "#f2f2f2"])
        axes[i].set_title(subscale)
    axes[-1].axis("off")
    plt.suptitle("Pie Charts Showing Proportion of Distress Level in Each Subscale", size=16)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    st.pyplot(fig)
