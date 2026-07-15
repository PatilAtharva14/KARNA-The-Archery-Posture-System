import streamlit as st
import pandas as pd


def get_exercises(body_part, goal, level):

    database = {
        "Shoulders": {
            "Strength": [
                ("Overhead Press", "4 x 8", "90 sec",
                 "https://www.youtube.com/results?search_query=overhead+press"),
                ("Lateral Raises", "3 x 12", "60 sec",
                 "https://www.youtube.com/results?search_query=lateral+raises")
            ],
            "Mobility": [
                ("Band Shoulder Mobility", "3 x 15", "30 sec",
                 "https://www.youtube.com/results?search_query=shoulder+mobility"),
                ("Wall Slides", "3 x 12", "30 sec",
                 "https://www.youtube.com/results?search_query=wall+slides")
            ]
        },

        "Back": {
            "Strength": [
                ("Deadlift", "4 x 6", "120 sec",
                 "https://www.youtube.com/results?search_query=deadlift"),
                ("Lat Pulldown", "3 x 10", "60 sec",
                 "https://www.youtube.com/results?search_query=lat+pulldown")
            ],
            "Mobility": [
                ("Cat-Cow Stretch", "3 x 15", "30 sec",
                 "https://www.youtube.com/results?search_query=cat+cow+stretch"),
                ("Thoracic Rotation", "3 x 12", "30 sec",
                 "https://www.youtube.com/results?search_query=thoracic+rotation")
            ]
        },

        "Core": {
            "Strength": [
                ("Plank", "3 x 60 sec", "45 sec",
                 "https://www.youtube.com/results?search_query=plank"),
                ("Russian Twists", "3 x 20", "45 sec",
                 "https://www.youtube.com/results?search_query=russian+twist")
            ],
            "Endurance": [
                ("Mountain Climbers", "3 x 40 sec", "30 sec",
                 "https://www.youtube.com/results?search_query=mountain+climbers"),
                ("Bicycle Crunch", "3 x 20", "30 sec",
                 "https://www.youtube.com/results?search_query=bicycle+crunch")
            ]
        },

        "Legs": {
            "Strength": [
                ("Squats", "4 x 10", "90 sec",
                 "https://www.youtube.com/results?search_query=squats"),
                ("Lunges", "3 x 12", "60 sec",
                 "https://www.youtube.com/results?search_query=lunges")
            ],
            "Endurance": [
                ("Wall Sit", "3 x 60 sec", "45 sec",
                 "https://www.youtube.com/results?search_query=wall+sit"),
                ("Jump Squats", "3 x 15", "45 sec",
                 "https://www.youtube.com/results?search_query=jump+squats")
            ]
        }
    }

    exercises = database.get(body_part, {}).get(goal, [])

    # scale for level
    if level == "Advanced":
        scaled = []
        for ex in exercises:
            scaled.append((ex[0], "5 sets", ex[2], ex[3]))
        return scaled

    return exercises


def weekly_plan(days):
    plan = []
    body_cycle = ["Shoulders", "Back", "Core", "Legs"]

    for i in range(days):
        plan.append({
            "Day": f"Day {i+1}",
            "Focus": body_cycle[i % len(body_cycle)]
        })

    return pd.DataFrame(plan)


def run():
    st.title("🏹 KARNA Exercise Suggestor")

    st.subheader("Customize Your Training")

    col1, col2 = st.columns(2)

    with col1:
        body_part = st.selectbox(
            "Target Body Part",
            ["Shoulders", "Back", "Core", "Legs"]
        )

        goal = st.selectbox(
            "Goal",
            ["Strength", "Mobility", "Endurance"]
        )

    with col2:
        level = st.selectbox(
            "Difficulty",
            ["Beginner", "Intermediate", "Advanced"]
        )

        days = st.slider(
            "Training Days / Week",
            1, 7, 4
        )

    if st.button("Generate Exercise Plan"):

        exercises = get_exercises(body_part, goal, level)

        st.success("Workout Plan Generated")

        # ---------------- DAILY WORKOUT ----------------
        st.subheader("Today's Workout")

        if exercises:
            df = pd.DataFrame(
                exercises,
                columns=[
                    "Exercise",
                    "Sets/Reps",
                    "Rest",
                    "Video Link"
                ]
            )

            st.dataframe(df)

        else:
            st.warning("No exercises found.")

        # ---------------- WEEKLY PLAN ----------------
        st.subheader("Weekly Training Plan")

        week_df = weekly_plan(days)
        st.table(week_df)

        # ---------------- TIPS ----------------
        st.subheader("Coach Tips")

        st.info(
            "Warm up for 10 minutes before training and stretch after every session."
        )

        st.info(
            "Focus on form over weight. Archery requires stability and endurance."
        )

        # ---------------- DOWNLOAD ----------------
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download Workout Plan",
            csv,
            "karna_workout_plan.csv",
            "text/csv"
        )
