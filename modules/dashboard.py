import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import get_scores


def run():
    st.title("📊 Dashboard")

    data = get_scores()

    if data:
        # matches: id, rounds, score, date
        df = pd.DataFrame(
            data,
            columns=["id", "rounds", "score", "date"]
        )

        df["date"] = pd.to_datetime(df["date"])

        # line chart
        fig = plt.figure()
        plt.plot(
            df["date"],
            df["score"],
            marker="o"
        )

        plt.xlabel("Date")
        plt.ylabel("Score")
        plt.title("Performance Trend")

        st.pyplot(fig)

        # rounds chart
        st.subheader("Rounds Played")
        st.bar_chart(df["rounds"])

        # table
        st.subheader("History")
        st.dataframe(df)

    else:
        st.info("No data yet")