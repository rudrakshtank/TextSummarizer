import streamlit as st
import whisper
import tempfile
import os
from dotenv import load_dotenv

# Load secret API key from .env
load_dotenv()

# Transcribe using Whisper
def transcribe_audio(audio_path, model_size='base'):
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    return result["text"]

# UI
st.title("🎧 Audio to Transcript")

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

        os.remove(audio_path)
