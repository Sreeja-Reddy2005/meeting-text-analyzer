import streamlit as st
import ollama

def analyze_text(text):

    prompt = f"""
You are an AI assistant.

Read the notes and extract the information.

Return output exactly in this format:

Summary:
Write a detailed summary of the meeting in 4–5 sentences explaining what was discussed.


Action Items:
- item1
- item2

Key Decisions:
- decision1
- decision2

Meeting Notes:
{text}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


st.title("AI  Analyzer")

text = st.text_area("Paste Text")

if st.button("Analyze"):
    if text:
        with st.spinner("Analyzing  ..."):
            result = analyze_text(text)
        st.write(result)
    else:
        st.warning("Please enter text")


