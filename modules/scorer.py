import streamlit as st
import pandas as pd
from database import add_score, get_scores


def run():
    st.title("🏹 Scorer")

    rounds = st.number_input(
        "Rounds Played",
        min_value=1,
        max_value=20,
        value=1
    )

    score = st.number_input(
        "Score",
        min_value=0,
        max_value=1000,
        value=0
    )

    if st.button("Save Score"):
        add_score(rounds, score)   # <-- fixed here
        st.success("Saved!")

    st.subheader("History")

    data = get_scores()

    if data:
        df = pd.DataFrame(
            data,
            columns=["ID", "Rounds", "Score", "Date"]
        )
        st.dataframe(df)
    else:
        st.info("No scores yet")