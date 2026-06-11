import streamlit as st
from utils import summarize_notes


st.markdown("""
<h1 style="
    text-align: left;
    font-size: 3rem;
    font-weight: bold;
    background: linear-gradient(90deg, #00F5A0, #00D9F5, #A200FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 20px;
">
     Meeting Notes Summarizer
</h1>
""", unsafe_allow_html=True)
st.write("Upload your meeting notes, and I'll summarize them for you!")

EXAMPLE_NOTES = """Weekly standup with the dev team.
Ankit said the login feature is almost done, needs one more day.
Database migration is pending, nobody has picked it up yet.
Sara will write the API documentation.
We decided to move the staging environment to AWS.
Team agreed to switch from Slack to Teams for communication.
Anyone know if the old server needs to be shut down after migration?"""

if "notes" not in st.session_state:
    st.session_state.notes = ""
if st.button("Load example notes"):
    st.session_state.notes=EXAMPLE_NOTES

notes = st.text_area("Enter your meeting notes here:", height=250 , placeholder="Paste your meeting notes here..." , value=st.session_state.notes)
st.caption(f"Character count: {len(notes)}")
generate =st.button("generate summary")
if generate:
    if notes.strip() == "":
        st.warning("please enter some meeting notes to summarize.")
    else:
        summary = summarize_notes(notes)
        with st.spinner("Analyzing meeting notes..."):
            try:
                st.markdown("### Summary:")
                st.markdown(summary)
            except Exception as e:
                st.error(f"An error occurred while generating the summary: {e}\n Please try again later!")

    st.download_button(
    label="download summary as .txt",
    data=summary,
    file_name="meeting_summary.txt",
    mime="text/plain"
    )
