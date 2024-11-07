import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# Simple hard-coded credentials
users = {
    "8462866656": "max",
    "8400275050": "max2",
    # Add more users as needed
}

# Login
st.title("Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username in users and users[username] == password:
        st.success("Login successful!")
        # Display app content
        st.write("Welcome to the app!")
    else:
        st.error("Invalid username or password")

# Define the diabetes distress categories
categories = [
    'Feeling that I am not as skilled at managing diabetes as I should be.',
    'Feeling that I don’t eat as carefully as I probably should.',
    'Feeling that I don’t notice the warning signs of hypoglycemia as well as I used to.',
    'Feeling that people treat me differently when they find out I have diabetes.',
    'Feeling discouraged when I see high blood glucose numbers that I can’t explain.',
    'Feeling that my family and friends make a bigger deal out of diabetes than they should.',
    'Feeling that I can’t tell my diabetes doctor what is really on my mind.',
    'Feeling that I am not taking as much insulin as I should.',
    'Feeling that there is too much diabetes equipment and stuff I must always have with me.',
    'Feeling like I have to hide my diabetes from other people.',
    'Feeling that my friends and family worry more about hypoglycemia than I want them to.',
    'Feeling that I don’t check my blood glucose level as often as I probably should.',
    'Feeling worried that I will develop serious long-term complications, no matter how hard I try.',
    'Feeling that I don’t get help I really need from my diabetes doctor about managing diabetes.',
    'Feeling frightened that I could have a serious hypoglycemic event when I’m asleep.',
    'Feeling that thoughts about food and eating control my life.',
    'Feeling that my friends or family treat me as if I were more fragile or sicker than I really am.',
    'Feeling that my diabetes doctor doesn\'t really understand what it\'s like to have diabetes.',
    'Feeling concerned that diabetes may make me less attractive to employers.',
    'Feeling that my friends or family act like “diabetes police” (bother me too much).',
    'Feeling that I’ve got to be perfect with my diabetes management.',
    'Feeling frightened that I could have a serious hypoglycemic event while driving.',
    'Feeling that my eating is out of control.',
    'Feeling that people will think less of me if they knew I had diabetes.',
    'Feeling that no matter how hard I try with my diabetes, it will never be good enough.',
    'Feeling that my diabetes doctor doesn\'t know enough about diabetes and diabetes care.',
    'Feeling that I can’t ever be safe from the possibility of a serious hypoglycemic event.',
    'Feeling that I don’t give my diabetes as much attention as I probably should.'
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
