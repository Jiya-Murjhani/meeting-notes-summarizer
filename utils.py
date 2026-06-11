from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("GROQ_API_KEY")
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