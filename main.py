import streamlit as st
from ocr.extract import extract_text
from analysis.spell_check import analyze_spelling

st.title("🧠 InkSight: Dyslexia Detector")

uploaded = st.file_uploader("Upload a handwriting photo", type=["png", "jpg", "jpeg"])
if uploaded:
    st.image(uploaded, caption="Handwritten Text", use_column_width=True)
    text = extract_text(uploaded)
    st.subheader("Extracted Text")
    st.text(text)

    st.subheader("Error Analysis")
    errors = analyze_spelling(text)
    for err in errors:
        st.write(f"🔍 {err['message']} (Suggestions: {err['replacements']})")
