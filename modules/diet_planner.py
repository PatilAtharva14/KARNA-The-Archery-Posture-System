import streamlit as st
import pandas as pd


def calculate_bmr(weight, height, age, gender):
    # Mifflin-St Jeor
    if gender == "Male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161


def activity_multiplier(level):
    mapping = {
        "Light": 1.375,
        "Moderate": 1.55,
        "Heavy": 1.725
    }
    return mapping[level]


def get_macros(calories, goal, weight):
    if goal == "Muscle Gain":
        protein = weight * 2.0
        fat = weight * 1.0
    elif goal == "Fat Loss":
        protein = weight * 2.2
        fat = weight * 0.8
    else:
        protein = weight * 1.8
        fat = weight * 0.9

    protein_cal = protein * 4
    fat_cal = fat * 9

    carbs = (calories - protein_cal - fat_cal) / 4

    return round(protein), round(carbs), round(fat)


def meal_plan(goal):
    if goal == "Muscle Gain":
        return {
            "Breakfast": "Oats + Eggs + Banana + Milk",
            "Lunch": "Rice + Chicken + Vegetables",
            "Snack": "Peanut butter sandwich + Fruit",
            "Dinner": "Chapati + Paneer/Chicken + Salad",
            "Post Workout": "Protein shake + Dates"
        }

    elif goal == "Fat Loss":
        return {
            "Breakfast": "Oats + Boiled Eggs",
            "Lunch": "Brown rice + Grilled chicken + Salad",
            "Snack": "Greek yogurt + Nuts",
            "Dinner": "Soup + Paneer/Tofu",
            "Post Workout": "Whey + Apple"
        }

    return {
        "Breakfast": "Oats + Fruit + Milk",
        "Lunch": "Rice + Dal + Vegetables",
        "Snack": "Nuts + Banana",
        "Dinner": "Chapati + Curry + Salad",
        "Post Workout": "Protein shake"
    }


def run():
    st.title("🏹 KARNA Diet Planner")

    st.subheader("Athlete Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 10, 80, 20)
        weight = st.number_input("Weight (kg)", 20, 200, 70)
        gender = st.selectbox("Gender", ["Male", "Female"])

    with col2:
        height = st.number_input("Height (cm)", 100, 250, 170)
        activity = st.selectbox(
            "Training Intensity",
            ["Light", "Moderate", "Heavy"]
        )
        goal = st.selectbox(
            "Goal",
            ["Muscle Gain", "Fat Loss", "Maintenance"]
        )

    if st.button("Generate Diet Plan"):

        # ---------------- CALCULATIONS ----------------
        bmr = calculate_bmr(weight, height, age, gender)
        calories = bmr * activity_multiplier(activity)

        if goal == "Muscle Gain":
            calories += 300
        elif goal == "Fat Loss":
            calories -= 400

        protein, carbs, fats = get_macros(calories, goal, weight)

        water = round(weight * 0.04, 1)

        # ---------------- OUTPUT ----------------
        st.success("Diet Plan Generated")

        st.subheader("Daily Targets")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Calories", f"{int(calories)} kcal")
        c2.metric("Protein", f"{protein} g")
        c3.metric("Carbs", f"{carbs} g")
        c4.metric("Fat", f"{fats} g")

        st.info(f"💧 Water Target: {water} L/day")

        # ---------------- MEAL TIMING ----------------
        st.subheader("Workout Nutrition")

        st.write("**Pre-workout (60 min before):** Banana + Peanut Butter")
        st.write("**Post-workout (within 30 min):** Protein shake + Dates")

        # ---------------- DAILY PLAN ----------------
        st.subheader("Suggested Meal Plan")

        meals = meal_plan(goal)

        df = pd.DataFrame(
            meals.items(),
            columns=["Meal", "Recommendation"]
        )

        st.table(df)

        # ---------------- EXPORT ----------------
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download Diet Plan",
            csv,
            "karna_diet_plan.csv",
            "text/csv"
        )