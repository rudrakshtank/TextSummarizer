import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Text Summarizer", layout="centered")
st.title("📝 AI Text Summarizer with OpenAI")

text = st.text_area("Paste your text here to summarize:", height=250)

if st.button("Summarize"):
    if not openai.api_key:
        st.error("API key not found. Please set your OpenAI key in a .env file.")
    elif not text.strip():
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": f"Summarize this:\n{text}"}
                    ]
                )
                summary = response["choices"][0]["message"]["content"]
                st.success("✅ Summary generated:")
                st.text_area("Summary", summary, height=200)
            except Exception as e:
                st.error(f"❌ Error: {e}")
