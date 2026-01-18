import streamlit as st
import pandas as pd

st.set_page_config(page_title="Grade Calculator", layout="centered")

st.title("Grade Calculator")
st.write("Enter your grades and their weight to calculate your final grade.")

# Default categories
default_categories = ["Homework", "Projects", "Midterm", "Final"]
default_grades = [80, 80, 80, 80]      # float values for grades
default_weights = [25, 25, 25, 25]     # int values for weights

# Number of grade categories
num_categories = st.number_input(
    "How many grading categories?",
    min_value=1,
    max_value=10,
    value=len(default_categories),
    step=1
)

st.divider()

category_names = []
grades = []
weights = []

for i in range(num_categories):
    st.subheader(f"Category {i + 1}")

    col1, col2, col3 = st.columns(3)

    # Set default values if within the default list
    default_name = default_categories[i] if i < len(default_categories) else f"Category {i + 1}"
    default_grade = float(default_grades[i]) if i < len(default_grades) else 80.0
    default_weight = int(default_weights[i]) if i < len(default_weights) else 0

    with col1:
        category_name = st.text_input(
            "Category name",
            value=default_name,
            key=f"name_{i}"
        )

    with col2:
        grade = st.number_input(
            "Grade (%)",
            min_value=0.0,
            max_value=100.0,
            value=default_grade,
            step=0.1,
            key=f"grade_{i}"
        )

    with col3:
        weight = st.number_input(
            "Weight (%)",
            min_value=0,
            max_value=100,
            value=default_weight,
            step=1,
            key=f"weight_{i}"
        )

    category_names.append(category_name)
    grades.append(grade)
    weights.append(weight)

st.divider()

total_weight = sum(weights)
st.write(f"**Total Weight:** {total_weight:.1f}%")

def letter_grade(score):
    if score >= 97:
        return "A+", "🤩🔥"
    elif score >= 93:
        return "A", "😄🎉"
    elif score >= 90:
        return "A-", "😊✨"
    elif score >= 87:
        return "B+", "😎👍"
    elif score >= 83:
        return "B", "🙂📘"
    elif score >= 80:
        return "B-", "😌📗"
    elif score >= 77:
        return "C+", "😐📙"
    elif score >= 73:
        return "C", "😬📒"
    elif score >= 70:
        return "C-", "😕📕"
    elif score >= 67:
        return "D+", "😟⚠️"
    elif score >= 63:
        return "D", "😣🚨"
    elif score >= 60:
        return "D-", "😖❗"
    else:
        return "F", "💀📉"

if total_weight != 100:
    st.warning("⚠️ Total weight must equal 100% to calculate final grade.")
else:
    final_grade = sum(
        grade * (weight / 100)
        for grade, weight in zip(grades, weights)
    )

    letter, emoji = letter_grade(final_grade)

    st.success(f"🎓 **Final Grade: {final_grade:.2f}%**")
    st.markdown(f"## {letter} {emoji}")

    # ------------------------------
    # Create a DataFrame for chart
    # ------------------------------
    df = pd.DataFrame({
        "Category": category_names,
        "Grade": grades
    })

    st.subheader("📊 Grades by Category")
    st.bar_chart(df.set_index("Category"))

# ------------------------------
# Fun Apple Game
# ------------------------------
st.divider()
st.subheader("🍎 Give an Apple to the Teacher!")

if st.button("Give an Apple!"):
    st.balloons()
    st.success("You gave the teacher an apple! 🍎 They are so happy! 😄")
