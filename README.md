# Trust and Reliance in AI-Assisted Decision-Making

## Understanding When People Trust AI—and When They Actually Rely on It

As AI becomes increasingly integrated into everyday decision-making, trust alone isn't enough. The critical question is whether people simply *trust* AI recommendations or whether those recommendations actually influence their decisions.

This mixed-methods research project investigates how different AI communication styles shape user trust, perceived transparency, decision confidence, and self-reported reliance during an AI-assisted task prioritization exercise.

Participants completed a realistic decision-making scenario in which they reviewed a list of tasks and received an AI recommendation about which task to complete first. Although the recommendation itself remained constant, the AI's communication style varied across four experimental conditions, allowing the study to isolate the effects of explanation style and confidence language.

The project combines behavioral research, statistical analysis, qualitative coding, and responsible AI design principles to better understand how AI can support—not replace—human decision-making.

---

## Research Questions

This study explored the following questions:

* How do AI explanation style and confidence language influence trust and reliance in AI-assisted decision-making?
* Do different communication styles change perceived transparency, trust, AI influence, decision confidence, or overall user experience?
* Is perceived transparency associated with trust?
* Is trust associated with self-reported AI influence?
* Can participants' written feedback explain the quantitative findings?

---

## Study Conditions

The experiment evaluated four distinct AI communication styles.

| Condition                 | Description                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| `high_confidence`         | Uses assertive confidence language (e.g., "highly confident," "clearly").                        |
| `uncertainty_calibrated`  | Expresses calibrated confidence while acknowledging uncertainty and providing a brief rationale. |
| `transparent_explanation` | Provides explicit reasoning behind the recommendation.                                           |
| `minimal_explanation`     | Presents only the recommendation with minimal supporting information.                            |

---

## Repository Overview

| File                     | Purpose                                                                                       |
| ------------------------ | --------------------------------------------------------------------------------------------- |
| `app.py`                 | Streamlit application used to run the study and collect participant responses.                |
| `conditions.py`          | Defines the four experimental AI communication conditions.                                    |
| `analysis.ipynb`         | Complete data cleaning, visualization, statistical analysis, and qualitative coding workflow. |
| `final_report.md`        | Final mixed-methods research report with findings and design recommendations.                 |
| `open_response_notes.md` | Thematic analysis of participant comments.                                                    |
| `assets/`                | Figures and visualizations used throughout the report.                                        |
| `data/`                  | Local participant datasets (excluded from Git).                                               |
| `requirements.txt`       | Python dependencies.                                                                          |

---

## Analysis Workflow

The analysis pipeline includes:

* Data cleaning and preprocessing
* Composite score creation
* Descriptive statistics
* Condition-level visualizations
* Kruskal-Wallis tests
* Brown-Forsythe (Levene) variance tests
* Pearson correlation analysis
* Exploratory OLS regression
* Qualitative thematic coding
* Mixed-methods synthesis

---

## Key Findings

Although the sample size was exploratory, several meaningful patterns emerged.

* Trust remained relatively stable across communication styles.
* Decision confidence showed the greatest variability between conditions.
* Perceived transparency demonstrated a strong positive association with trust.
* Trust was **not** significantly associated with self-reported AI influence, suggesting that trusting an AI recommendation does not necessarily mean users rely on it when making decisions.
* Participant comments revealed that explanations mattered more than confidence alone. Recommendations felt most trustworthy when supported by clear reasoning, while unsupported certainty was often perceived as overconfident.

Together, these findings highlight an important distinction between **building trust** and **changing user behavior**.

---

## Responsible AI Design Implications

The findings suggest several practical guidelines for designing human-centered AI systems:

* Support recommendations with clear evidence rather than confidence alone.
* Calibrate uncertainty instead of projecting unwarranted certainty.
* Pair expressions of uncertainty with concise explanations.
* Match explanation depth to task complexity.
* Preserve user agency by positioning AI as decision support rather than decision replacement.
* Measure behavioral influence directly instead of assuming trust leads to reliance.

---

## Tools & Technologies

* Python
* Streamlit
* Pandas
* SciPy
* Statsmodels
* Matplotlib
* Google Sheets API
* Mixed-methods UX Research

---

## Conclusion

This project bridges behavioral science, UX research, and responsible AI design to explore how communication—not just recommendation quality—influences human-AI collaboration. It demonstrates a complete end-to-end research workflow, from experimental design and participant data collection to statistical analysis, qualitative synthesis, and actionable product recommendations.

**Try the live interactive study:**

👉 https://trust-reliance-ai-decision-making-z9nhkauxjftupkpf2jcapq.streamlit.app/
