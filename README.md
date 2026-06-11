# Meeting Notes Summarizer

An AI-powered web app that converts messy, unstructured meeting notes 
into clean, structured summaries in seconds.

## Live Demo
[Click here to try the app](<https://meeting-notes-summarizer-pmbi6z3tumpb7a5t88q32c.streamlit.app/>)

---

## What it does

Paste your raw meeting notes and the app instantly extracts:

- **Summary** — 2-3 line overview of the meeting
- **Action Items** — each task with owner name and deadline
- **Decisions Made** — what was finalized and by whom
- **Open Questions** — things raised but not resolved

## Example

**Input:**
Weekly standup with the dev team. Ankit said the login feature is
almost done, needs one more day. Database migration is pending,
nobody has picked it up yet. Sara will write the API documentation.
We decided to move the staging environment to AWS.
Anyone know if the old server needs to be shut down after migration?

**Output:**

**SUMMARY:**
The dev team held a weekly standup to discuss ongoing tasks and 
infrastructure changes.

**ACTION ITEMS:**
- Task: Complete login feature | Owner: Ankit | Deadline: Not mentioned
- Task: Write API documentation | Owner: Sara | Deadline: Not mentioned
- Task: Pick up database migration | Owner: Unknown | Deadline: Not mentioned

**DECISIONS MADE:**
- Move staging environment to AWS — By: Unknown

**OPEN QUESTIONS:**
- Anyone know if the old server needs to be shut down after migration?

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend / UI | Streamlit |
| Backend | Python |
| LLM API | Groq (LLaMA 3) |
| Environment Management | python-dotenv |

---

## Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Jiya-Murjhani/meeting-notes-summarizer.git
cd meeting-notes-summarizer
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up your API key**

Create a `.env` file in the root folder and add:
GROQ_API_KEY=your_actual_key_here
Get your free API key from [console.groq.com](https://console.groq.com)

**4. Run the app**

streamlit run app.py

The app will open automatically in your browser at `http://localhost:8501`

---

## Project Structure
meeting-notes-summarizer/
│
├── app.py              # Streamlit UI
├── utils.py            # Prompt engineering + API call
├── requirements.txt    # Project dependencies
├── .env                # API key (not pushed to GitHub)
├── .gitignore          # Files excluded from GitHub
└── README.md           # Project documentation

---

## Key Engineering Decisions

- **Prompt engineered to prevent hallucination** — strict rules ensure 
  the LLM only extracts what is explicitly stated in the notes, never 
  infers or generates content
- **Edge case handling** — unknown owners, missing deadlines, and empty 
  sections are all handled gracefully
- **Clean separation of concerns** — UI logic in app.py, 
  AI logic in utils.py

---

## Author

**Jiya Murjhani**  
[LinkedIn](<https://www.linkedin.com/in/jiya-murjhani/>) • [GitHub](<https://github.com/Jiya-Murjhani>)
