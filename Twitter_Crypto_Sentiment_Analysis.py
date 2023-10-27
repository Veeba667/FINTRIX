import streamlit as st
from textblob import TextBlob


def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    # port = 5000
    # st.set_option('server.port', port)
    
    st.set_page_config(
        page_title="Crypto Sentiment Analysis",
        page_icon="🔗",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    hide_streamlit_style = """
        <style>
            #MainMenu {visibility: hidden;}
            .stButton>button {display: none;}
            footer {visibility: hidden;}
        </style>
    """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.title("Crypto Sentiment Analysis")
    st.write("Enter your crypto-related text below to analyze its sentiment:")

    crypto_text = st.text_area("Enter text here:")
    
    if st.button("Analyze"):
        if crypto_text:
            sentiment = analyze_sentiment(crypto_text)
            st.write("Sentiment:", sentiment)
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main()
