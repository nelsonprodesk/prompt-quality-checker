import streamlit as st
import pandas as pd

st.set_page_config(page_title="Prompt Quality Checker", page_icon="📝")
st.title("Prompt Quality Checker 📝")
st.write("Type a prompt or upload a text file with multiple prompts to evaluate their quality.")

# --- Function to evaluate prompts ---
def evaluate_prompt(prompt):
    score = 0
    feedback = []

    # Length check
    if len(prompt) >= 20:
        score += 1
    else:
        feedback.append("Prompt is too short; try to give more context.")

    # Question check
    if "?" in prompt:
        score += 1
    else:
        feedback.append("Try phrasing it as a clear question.")

    # Action word check
    if any(word in prompt.lower() for word in ["explain", "describe", "summarize"]):
        score += 1
    else:
        feedback.append("Add an action word like 'explain', 'describe', or 'summarize'.")

    return score, feedback

# --- Text entry prompt ---
text_prompt = st.text_area("Type a single prompt here:", height=100)
if st.button("Evaluate Text Prompt"):
    if text_prompt.strip() == "":
        st.warning("Please type a prompt to evaluate.")
    else:
        score, feedback = evaluate_prompt(text_prompt)
        st.subheader("Evaluation Results")
        st.write(f"Prompt: {text_prompt}")
        st.write(f"Score: **{score}/3**")
        if feedback:
            st.write("Suggestions:")
            for f in feedback:
                st.write("- " + f)
        else:
            st.success("Your prompt looks good!")

# --- File upload for multiple prompts ---
st.markdown("---")
uploaded_file = st.file_uploader("Or upload a .txt file (one prompt per line):", type="txt")

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
    st.subheader("Evaluation Results (File Upload)")
    st.dataframe(df)

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Results as CSV", csv, "prompt_evaluation.csv", "text/csv")
