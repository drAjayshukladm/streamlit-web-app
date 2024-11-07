import matplotlib.pyplot as plt
import numpy as np

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
    'Feeling that I don’t get help I really need from my diabetes doctor about managing diabetes',
    'Feeling frightened that I could have a serious hypoglycemic event when I’m asleep.',
    'Feeling that thoughts about food and eating control my life.',
    'Feeling that my friends or family treat me as if I were more fragile or sicker than I really am',
    'Feeling that my diabetes doctor doesn\'t really understand what it\'s like to have diabetes',
    'Feeling concerned that diabetes may make me less attractive to employers.',
    'Feeling that my friends or family act like “diabetes police” (bother me too much).',
    'Feeling that I’ve got to be perfect with my diabetes management',
    'Feeling frightened that I could have a serious hypoglycemic event while driving',
    'Feeling that my eating is out of control',
    'Feeling that people will think less of me if they knew I had diabetes',
    'Feeling that no matter how hard I try with my diabetes, it will never be good enough.',
    'Feeling that my diabetes doctor doesn\'t know enough about diabetes and diabetes care.',
    'Feeling that I can’t ever be safe from the possibility of a serious hypoglycemic event',
    'Feeling that I don’t give my diabetes as much attention as I probably should'
]

# Prompt ratings
print('Please rate each statement on a scale from 1 to 6:')
print('1=Not a Problem, 2=A Slight Problem, 3=A Moderate Problem, 4=Somewhat Serious Problem, 5=A Serious Problem, 6=A Very Serious Problem\n')

# Collect responses in a loop
responses = []
for i, question in enumerate(categories, start=1):
    while True:
        try:
            rating = int(input(f"{i}. {question} (1-6): "))
            if 1 <= rating <= 6:
                responses.append(rating)
                break
            else:
                print("Please enter a valid rating between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

# Calculate the average score
score28 = sum(responses) / len(responses)
print(f"\nAverage T1-DDS score of 28 questions is {score28:.2f}")

# Determine distress level
if score28 < 2:
    print("Indicates little or no distress, as this score is less than 2.")
elif 2 <= score28 < 3:
    print("Indicates moderate distress, as the average score is between 2.0 and 2.9.")
else:
    print("Indicates high distress, as the average score is greater than 3.0.")

# Calculate subscale scores
subscales = {
    "Powerlessness": [responses[4], responses[8], responses[12], responses[20], responses[24]],
    "Management Distress": [responses[0], responses[7], responses[11], responses[27]],
    "Hypoglycemia Distress": [responses[2], responses[14], responses[21], responses[26]],
    "Negative Social Perceptions": [responses[3], responses[9], responses[18], responses[23]],
    "Eating Distress": [responses[1], responses[15], responses[22]],
    "Physician Distress": [responses[6], responses[13], responses[17], responses[25]],
    "Friend/Family Distress": [responses[5], responses[10], responses[16], responses[19]]
}

for subscale_name, items in subscales.items():
    score = sum(items) / len(items)
    print(f"{subscale_name} score: {score:.2f} out of max score 6")
    if score > 2:
        print(f"{subscale_name} score > 2.0 is considered clinically significant.\n")

# Radar chart for subscale scores
N = len(subscales)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

# Subscale scores
scores = [sum(items) / len(items) for items in subscales.values()]
scores += scores[:1]

# Create polar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.plot(angles, scores, 'o-', linewidth=2)
ax.fill(angles, scores, alpha=0.25)

# Label each axis
ax.set_thetagrids(np.degrees(angles[:-1]), list(subscales.keys()))
ax.set_ylim(0, 6)

# Title and display
plt.title('Type 1 Diabetes Distress Subscale Scores', size=20)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Sample data based on the categories and calculated subscale scores
categories = [
    "Powerlessness", "Management Distress", "Hypoglycemia Distress",
    "Negative Social Perceptions", "Eating Distress",
    "Physician Distress", "Friend/Family Distress"
]
# Sample scores for demonstration purposes
scores = [3.2, 2.8, 3.5, 2.1, 3.0, 2.4, 2.7]

# Create an axis graph (bar chart) for the scores
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(categories, scores)

# Add labels and title
ax.set_ylabel("Score (out of 6)")
ax.set_title("Type 1 Diabetes Distress Subscale Scores")
ax.set_ylim(0, 6)  # Setting max score to 6 for better visualization

# Display the plot
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
# Create a pie chart for each subscale based on the sample scores

fig, axes = plt.subplots(2, 4, figsize=(15, 8))
axes = axes.flatten()  # Flatten the 2x4 grid to easily index

# Define the subscale labels and sample scores
subscales = {
    "Powerlessness": 3.2,
    "Management Distress": 2.8,
    "Hypoglycemia Distress": 3.5,
    "Negative Social Perceptions": 2.1,
    "Eating Distress": 3.0,
    "Physician Distress": 2.4,
    "Friend/Family Distress": 2.7
}

# Pie chart segments to show the scored part vs. the maximum score
for i, (subscale, score) in enumerate(subscales.items()):
    axes[i].pie([score, 6 - score], labels=[f"{score}", f"{6 - score}"],
                autopct='%1.1f%%', startangle=140, colors=["#66c2a5", "#f2f2f2"])
    axes[i].set_title(subscale)

# Hide the last subplot as it's unused
axes[-1].axis("off")

# Adjust layout and display
plt.suptitle("Pie Charts Showing Proportion of Distress Level in Each Subscale", size=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
