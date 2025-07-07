import streamlit as st
import whisper
import tempfile
import openai
import os
from dotenv import load_dotenv

# Load secret API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Transcribe using Whisper
def transcribe_audio(audio_path, model_size='base'):
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    return result["text"]

# Summarize using GPT
def summarize_text(transcript):
    prompt = f"""
    Summarize the following educational lecture transcript clearly and concisely.

    Transcript:
    {transcript[:3500]}

    Summary:
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error during summarization: {e}"

# UI
st.title("🎧 Audio to Transcript + AI Summary")

uploaded_file = st.file_uploader("Upload an audio file (e.g., .mp3, .wav, .m4a)", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    with st.spinner("Processing..."):

        with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name[-4:]) as temp_audio:
            temp_audio.write(uploaded_file.read())
            audio_path = temp_audio.name

        st.info("🎙️ Transcribing with Whisper...")
        transcript = transcribe_audio(audio_path)

        st.success("✅ Transcription complete!")
        st.subheader("Transcript")
        st.text_area("Transcript", transcript, height=300)

        st.info("📚 Generating Summary with GPT...")
        summary = summarize_text(transcript)

        st.success("✅ Summary Ready!")
        st.subheader("Summary")
        st.write(summary)

        os.remove(audio_path)import streamlit as st
import whisper
import tempfile
import openai
import os
from dotenv import load_dotenv

# Load secret API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Transcribe using Whisper
def transcribe_audio(audio_path, model_size='base'):
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    return result["text"]

# Summarize using GPT
def summarize_text(transcript):
    prompt = f"""
    Summarize the following educational lecture transcript clearly and concisely.

    Transcript:
    {transcript[:3500]}

    Summary:
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error during summarization: {e}"

# UI
st.title("🎧 Audio to Transcript + AI Summary")

uploaded_file = st.file_uploader("Upload an audio file (e.g., .mp3, .wav, .m4a)", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    with st.spinner("Processing..."):

        with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name[-4:]) as temp_audio:
            temp_audio.write(uploaded_file.read())
            audio_path = temp_audio.name

        st.info("🎙️ Transcribing with Whisper...")
        transcript = transcribe_audio(audio_path)

        st.success("✅ Transcription complete!")
        st.subheader("Transcript")
        st.text_area("Transcript", transcript, height=300)

        st.info("📚 Generating Summary with GPT...")
        summary = summarize_text(transcript)

        st.success("✅ Summary Ready!")
        st.subheader("Summary")
        st.write(summary)

        os.remove(audio_path)
