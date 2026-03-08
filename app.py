import streamlit as st

st.set_page_config(page_title="Prompt Quality Checker", page_icon="📝")

st.title("Prompt Quality Checker 📝")
st.write(
    "Evaluate the quality of AI prompts and get suggestions for improvement."
)

# User input
prompt = st.text_area("Enter your prompt here:", height=150)

# Button to evaluate
if st.button("Evaluate Prompt"):
    score = 0
    feedback = []

    # Check length
    if len(prompt) >= 20:
        score += 1
    else:
        feedback.append("Prompt is too short; try to give more context.")

    # Check for question
    if "?" in prompt:
        score += 1
    else:
        feedback.append("Try phrasing it as a clear question.")

    # Check for clarity (example: use "explain")
    if any(word in prompt.lower() for word in ["explain", "describe", "summarize"]):
        score += 1
    else:
        feedback.append("Add an action word like 'explain', 'describe', or 'summarize'.")

    # Display results
    st.subheader("Evaluation Results")
    st.write(f"Prompt Score: **{score}/3**")
    if feedback:
        st.write("Suggestions to improve your prompt:")
        for f in feedback:
            st.write("- " + f)
    else:
        st.success("Your prompt looks good!")
