import streamlit as st
import pandas as pd

st.set_page_config(page_title="Prompt Quality Checker", page_icon="📝")
st.title("Prompt Quality Checker 📝")
st.write("Upload a text file of prompts to evaluate their quality automatically.")

# Upload file
uploaded_file = st.file_uploader("Upload a .txt file with one prompt per line", type="txt")

def evaluate_prompt(prompt):
    score = 0
    feedback = []

    if len(prompt) >= 20:
        score += 1
    else:
        feedback.append("Prompt is too short; try to give more context.")

    if "?" in prompt:
        score += 1
    else:
        feedback.append("Try phrasing it as a clear question.")

    if any(word in prompt.lower() for word in ["explain", "describe", "summarize"]):
        score += 1
    else:
        feedback.append("Add an action word like 'explain', 'describe', or 'summarize'.")

    return score, feedback

# Process file
if uploaded_file is not None:
    prompts = uploaded_file.read().decode("utf-8").splitlines()
    results = []

    for prompt in prompts:
        score, feedback = evaluate_prompt(prompt)
        results.append({
            "Prompt": prompt,
            "Score": f"{score}/3",
            "Suggestions": "; ".join(feedback) if feedback else "Good!"
        })

    # Display results as table
    df = pd.DataFrame(results)
    st.subheader("Evaluation Results")
    st.dataframe(df)

    # Allow download as CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Results as CSV", csv, "prompt_evaluation.csv", "text/csv")
