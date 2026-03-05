import ollama

def analyze_text(text):

    prompt = f"""
Read the following meeting text and extract:

1. Summary
2. Action Items (as bullet points)
3. Key Decisions (as bullet points)

Text:
{text}

Return output exactly in this format:

Summary:
...

Action Items:
- item1
- item2

Key Decisions:
- decision1
- decision2
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


text = """
In today's meeting the team discussed launching the new mobile application by July.
The marketing team will prepare the promotional campaign.
John will coordinate with developers for final testing.
It was decided that the beta version will be released next month.
Budget approval was confirmed for marketing activities.
"""

print(analyze_text(text))