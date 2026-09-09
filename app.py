import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="🤖"
)

st.title("🐽 Sentiment Analysis")
st.write("Analyze the sentiment of a sentence using a Hugging Face model.")

@st.cache_resource
def load_model():
    model = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )
    return model

sentiment_model = load_model()


text = st.text_area(
    "Enter your sentence:",
    placeholder="Example: I really enjoyed this movie!"
)


if st.button("Analyze Sentiment"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:
        result = sentiment_model(text)[0]

        label = result["label"]
        score = result["score"]

        st.subheader("Result")

        if label == "POSITIVE":
            st.success("😊 Positive Sentiment")
        else:
            st.error("😞 Negative Sentiment")

        st.write("**Sentiment:**", label)
        st.write("**Confidence:**", f"{score:.2%}")
