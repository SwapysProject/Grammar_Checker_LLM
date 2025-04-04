import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load model and tokenizer
@st.cache_resource
def load_model():
    model_name = "prithivida/grammar_error_correcter_v1"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model()

def correct_grammar(text):
    inputs = tokenizer.encode("gec: " + text, return_tensors="pt", max_length=128, truncation=True)
    outputs = model.generate(inputs, max_length=128, num_beams=5, early_stopping=True)
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_text

# Streamlit UI
st.title("📝 Automatic Grammar Checker")
st.write("Enter a sentence, and I'll fix any grammar mistakes!")

user_input = st.text_area("Enter text here:", "")

if st.button("Correct Grammar"):
    if user_input.strip():
        corrected_text = correct_grammar(user_input)
        st.subheader("Corrected Text:")
        st.write(corrected_text)
    else:
        st.warning("Please enter some text!")
