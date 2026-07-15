import streamlit as st
import pandas as pd
from database import add_record, get_records


def run():
    st.title("📘 Daily Records")

    st.subheader("Add Today's Record")

    date = st.date_input("Date")
    arrows = st.number_input("Total Arrows Shot", 0)
    practice_time = st.number_input(
        "Practice Time (hours)",
        min_value=0.0,
        step=0.5
    )

    mistakes = st.text_area(
        "Mistakes Made",
        placeholder="e.g. elbow dropping, shoulder tilt"
    )

    learnings = st.text_area(
        "New Learnings",
        placeholder="e.g. improved anchor point"
    )

    if st.button("Save Record"):
        add_record(
            str(date),
            arrows,
            practice_time,
            mistakes,
            learnings
        )
        st.success("Record saved successfully!")

    st.divider()

    st.subheader("History")

    data = get_records()

    if data:
        df = pd.DataFrame(
            data,
            columns=[
                "ID",
                "Date",
                "Arrows",
                "Practice Time",
                "Mistakes",
                "Learnings"
            ]
        )

        st.dataframe(df)

    else:
        st.info("No records found")