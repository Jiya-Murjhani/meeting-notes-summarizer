from groq import Groq
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key= st.secrets.get("GROQ_API_KEY" ,  os.getenv("GROQ_API_KEY"))
client = Groq(api_key=api_key)

if not api_key:
    raise ValueError("GROQ_API_KEY not found")

def summarize_notes(notes):
 prompt = f"""
You are an expert meeting notes analyst. Your job is to extract and structure 
information from raw meeting notes with complete accuracy.

STRICT RULES — follow these without exception:
1. Only extract information that is explicitly stated in the meeting notes.
   Do not infer, assume, or add anything not directly present in the text.
2. Only list open questions that were explicitly raised in the meeting.
   Do not convert problems, statements, or observations into questions.
3. If a task owner is not mentioned, write "Owner: Unknown"
4. If a deadline is not mentioned, write "Deadline: Not mentioned"
5. If a decision-maker is not mentioned, write "By: Unknown"
6. If any section has no relevant content, write "None identified."
7. Respond in clear, professional English regardless of the language
   or tone of the input notes.
8. Do not list decisions as action items. A decision is something that was agreed upon or finalized. An action item is a specific task assigned to someone to execute.
9.Do not convert open questions into action items.If something is 
   phrased as a question in the meeting notes, it belongs under 
   OPEN QUESTIONS, not ACTION ITEMS.
10.8. Each piece of information must appear under one section only. 
   Do not repeat the same point across multiple sections. 
   If something is a decision, it goes under DECISIONS MADE only. 
   If something is a question, it goes under OPEN QUESTIONS only. 
   If something is a task to be executed, it goes under ACTION ITEMS only.

FORMAT — follow this exactly, do not add or remove any headings:

[Write a 2-3 line summary here. Do not write the word SUMMARY before it.]

**ACTION ITEMS:**
- Task: [what needs to be done] | Owner: [name or Unknown] | Deadline: [date or Not mentioned]

**DECISIONS MADE:**
- [decision] — By: [name or Unknown]

**OPEN QUESTIONS:**
- [question explicitly raised in the meeting]

Meeting notes:
{notes}
"""
 
 response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
 )
 return response.choices[0].message.content