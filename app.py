import streamlit as st
from config import APP_NAME
from database import init_db

from modules import (
    posture_detection,
    scorer,
    diet_planner,
    daily_records,
    exercise_suggestor,
    dashboard
)

init_db()

st.set_page_config(page_title=APP_NAME, layout="wide")

st.sidebar.title(APP_NAME)

menu = st.sidebar.radio("Menu", [
    "Live Detection",
    "Scorer",
    "Diet Planner",
    "Daily Records",
    "Exercises",
    "Dashboard"
])

if menu == "Live Detection":
    posture_detection.run()

elif menu == "Scorer":
    scorer.run()

elif menu == "Diet Planner":
    diet_planner.run()

elif menu == "Daily Records":
    daily_records.run()

elif menu == "Exercises":
    exercise_suggestor.run()

elif menu == "Dashboard":
    dashboard.run()