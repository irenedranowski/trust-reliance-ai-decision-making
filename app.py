import streamlit as st
import random
import os
import pandas as pd
from conditions import CONDITIONS
from datetime import datetime
import gspread

SPREADSHEET_ID = "1WqVwLb451ADnHvn4nvKbCoF9JteGy_Z4vh0Pm6VDtkQ"
GOOGLE_CREDS_PATH = os.environ.get("GOOGLE_SHEETS_CREDENTIALS", "service_account.json")

GSHEET_HEADER = [
    "timestamp",
    "ai_use",
    "baseline_trust",
    "comfort",
    "selected_task",
    "decision_confidence",
    "ai_influence",
    "trust_1",
    "trust_2",
    "trust_3",
    "transparency_1",
    "transparency_2",
    "ux_1",
    "ux_2",
    "open_trust",
    "open_explanation",
    "open_improvement",
    "condition_key",
]

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "welcome"
    st.session_state.ai_use = 4
    st.session_state.baseline_trust = 4
    st.session_state.comfort = 4
    st.session_state.selected_task = None
    st.session_state.decision_confidence = 4
    st.session_state.ai_influence = 4
    st.session_state.trust_1 = 4
    st.session_state.trust_2 = 4
    st.session_state.trust_3 = 4
    st.session_state.transparency_1 = 4
    st.session_state.transparency_2 = 4
    st.session_state.ux_1 = 4
    st.session_state.ux_2 = 4
    st.session_state.open_trust = ""
    st.session_state.open_explanation = ""
    st.session_state.open_improvement = ""
    st.session_state.condition_key = random.choice(list(CONDITIONS.keys()))

tasks = pd.DataFrame({
    "Task": [
        "Draft Project Report",
        "Reply to Emails",
        "Review Course Module",
        "Organize Notes"
    ],
    "Deadline": ["Today", "Today", "Tomorrow", "Friday"],
    "Importance": ["High", "Medium", "High", "Low"]
})

condition = CONDITIONS[st.session_state.condition_key]

def get_google_sheet():
    if not os.path.exists(GOOGLE_CREDS_PATH):
        raise FileNotFoundError(
            f"Google credentials not found at {GOOGLE_CREDS_PATH}. "
            "Set GOOGLE_SHEETS_CREDENTIALS or place your service_account.json there."
        )
    client = gspread.service_account(filename=GOOGLE_CREDS_PATH)
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    return sheet


def append_response_to_sheet(record):
    sheet = get_google_sheet()
    row = [record[col] for col in GSHEET_HEADER]
    sheet.append_row(row, value_input_option="USER_ENTERED")

if st.session_state.page == "welcome":
    st.title("Trust & Reliance in AI Decision-Making")
    st.write("This prototype explores how AI communication style may influence trust and reliance in decision-making.")
    if st.button("Begin", key="begin_button"):
        st.session_state.page = "context"
        st.rerun()

elif st.session_state.page == "context":
    st.title("Context Questions")
    st.slider("I regularly use AI tools.", 1, 7, st.session_state.ai_use, key="ai_use")
    st.slider("I generally trust AI recommendations.", 1, 7, st.session_state.baseline_trust, key="baseline_trust")
    st.slider("I feel comfortable using AI to support decisions.", 1, 7, st.session_state.comfort, key="comfort")

    cols = st.columns([1, 8, 1])

    if cols[0].button("Back", key="back_to_welcome"):
        st.session_state.page = "welcome"
        st.rerun()
    if cols[2].button("Next", key="next_to_scenario"):
        st.session_state.page = "scenario"
        st.rerun()

elif st.session_state.page == "scenario":
    st.title("Scenario + AI Recommendation")
    st.table(tasks)
    st.subheader("AI Recommendation")
    st.info(condition["recommendation"])

    st.radio("Which task do you choose first?", tasks["Task"].tolist(), index = 0, key="selected_task")
    st.slider("How confident are you in your decision?", 1, 7, st.session_state.decision_confidence, key="decision_confidence")
    st.slider("How much did the AI influence your decision?", 1, 7, st.session_state.ai_influence, key="ai_influence")

    cols = st.columns([1, 8, 1])
    if cols[0].button("Back", key="back_to_context"):
        st.session_state.page = "context"
        st.rerun()
    if cols[2].button("Next", key="next_to_post_task"):
        st.session_state.page = "post_task"
        st.rerun()

elif st.session_state.page == "post_task":
    st.title("Post-Task Survey")
    st.slider("I trusted the AI recommendation.", 1, 7, st.session_state.trust_1, key="trust_1")
    st.slider("The AI seemed reliable.", 1, 7, st.session_state.trust_2, key="trust_2")
    st.slider("I would use this AI again.", 1, 7, st.session_state.trust_3, key="trust_3")
    st.slider("I understood why the AI made its recommendation.", 1, 7, st.session_state.transparency_1, key="transparency_1")
    st.slider("The explanation was helpful.", 1, 7, st.session_state.transparency_2, key="transparency_2")
    st.slider("The interface was easy to use.", 1, 7, st.session_state.ux_1, key="ux_1")
    st.slider("The AI helped me decide faster.", 1, 7, st.session_state.ux_2, key="ux_2")
    st.text_area("What made the AI feel trustworthy or untrustworthy?", st.session_state.open_trust, key="open_trust")
    st.text_area("Did the explanation feel helpful, excessive, or insufficient?", st.session_state.open_explanation, key="open_explanation")
    st.text_area("What would improve this experience?", st.session_state.open_improvement, key="open_improvement")

    cols = st.columns([1, 6, 1])
    if cols[0].button("Back", key="back_to_scenario"):
        st.session_state.page = "scenario"
        st.rerun()
    if cols[2].button("Submit", key="submit_responses"):
        record = {
            "timestamp": datetime.now().isoformat(),
            "ai_use": st.session_state.ai_use,
            "baseline_trust": st.session_state.baseline_trust,
            "comfort": st.session_state.comfort,
            "selected_task": st.session_state.selected_task,
            "decision_confidence": st.session_state.decision_confidence,
            "ai_influence": st.session_state.ai_influence,
            "trust_1": st.session_state.trust_1,
            "trust_2": st.session_state.trust_2,
            "trust_3": st.session_state.trust_3,
            "transparency_1": st.session_state.transparency_1,
            "transparency_2": st.session_state.transparency_2,
            "ux_1": st.session_state.ux_1,
            "ux_2": st.session_state.ux_2,
            "open_trust": st.session_state.open_trust,
            "open_explanation": st.session_state.open_explanation,
            "open_improvement": st.session_state.open_improvement,
            "condition_key": st.session_state.condition_key
        }
        append_response_to_sheet(record)
        st.session_state.page = "thank_you"

elif st.session_state.page == "thank_you":
    st.write("Thank you! Your responses have been recorded.")