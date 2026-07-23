import streamlit as st
from utils.pdf_reader import extract_text
from utils.summarizer import summarize_text

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("⚙️ Menu")
    st.write("Welcome!")
    st.divider()

    st.button("📝 Summarize Notes")
    st.button("❓ Ask Questions")
    st.button("🧠 Flashcards")
    st.button("📚 Generate Quiz")

# Main Page
st.title("📚 AI Study Assistant")

st.write(
    "Upload your study notes and let AI help you understand them."
)

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)
if uploaded_file is not None:

    with st.spinner("Reading your PDF..."):
        text = extract_text(uploaded_file)

    with st.spinner("Gemini is preparing your summary..."):
        summary = summarize_text(text)

    st.subheader("📄 AI Summary")

    st.write(summary)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

st.divider()

st.subheader("AI Response")

st.info("Your summaries, flashcards and answers will appear here.")