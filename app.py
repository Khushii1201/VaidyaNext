import streamlit as st
from PyPDF2 import PdfReader
import re

# ------------ PDF TEXT EXTRACTION ------------
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# ------------ SIMPLE NLP EXTRACTION ------------
def extract_disease(text):
    keywords = ["cancer", "diabetes", "covid", "infection", "hypertension", "tumor"]
    for line in text.split("\n")[:50]:
        for word in keywords:
            if word in line.lower():
                return line.strip()
    return "Not Found"

def extract_sample_size(text):
    patterns = [r"n\s*=\s*(\d+)", r"(\d+)\s+patients", r"(\d+)\s+participants"]
    for p in patterns:
        x = re.search(p, text.lower())
        if x:
            return int(x.group(1))
    return None

def extract_outcome(text):
    if "significant" in text.lower() or "effective" in text.lower():
        return "Positive Outcome"
    elif "no effect" in text.lower() or "not effective" in text.lower():
        return "Negative Outcome"
    return "Unclear"

# ------------ SCORING SYSTEM ------------
def compute_scores(sample, outcome):
    score = 0
    if sample is None:
        score += 10
    elif sample > 200:
        score += 40
    elif sample > 100:
        score += 30
    elif sample > 50:
        score += 20
    else:
        score += 10

    if "positive" in outcome.lower():
        score += 40
    elif "unclear" in outcome.lower():
        score += 20
    else:
        score += 10

    return min(score, 100)

# ------------ STREAMLIT UI ------------
def main():
    st.title("🧠 VaidyaNext")
    st.write("AI Research Evaluation Tool")

    uploaded_file = st.file_uploader("Upload PDF research paper", type=["pdf"])
    text_input = st.text_area("Or paste research text here:")

    if st.button("Analyze"):
        if uploaded_file:
            text = extract_text_from_pdf(uploaded_file)
        elif text_input:
            text = text_input
        else:
            st.error("Upload a PDF or paste text.")
            return

        disease = extract_disease(text)
        sample = extract_sample_size(text)
        outcome = extract_outcome(text)
        score = compute_scores(sample, outcome)

        st.subheader("📌 Analysis Result")
        st.write(f"**Detected Disease:** {disease}")
        st.write(f"**Sample Size:** {sample if sample else 'Not found'}")
        st.write(f"**Outcome Interpretation:** {outcome}")
        st.metric("Final Confidence Score", f"{score}/100")

        if score > 75:
            st.success("High potential drug candidate.")
        elif score > 50:
            st.info("Moderate potential. Needs more validation.")
        else:
            st.warning("Low potential candidate.")

if __name__ == "__main__":
    main()
