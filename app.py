import streamlit as st

st.title("Trust & Reliance in AI Decision-Making")

st.write(
    "This prototype explores how AI communication style may influence trust and reliance in decision-making."
)

if st.button("Begin"):
    st.session_state["page"] = "context"
