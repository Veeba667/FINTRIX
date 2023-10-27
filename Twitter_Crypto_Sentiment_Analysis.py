import streamlit as st
from textblob import TextBlob
import plotly.express as px


def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive", analysis.sentiment.polarity
    elif analysis.sentiment.polarity < 0:
        return "Negative", analysis.sentiment.polarity
    else:
        return "Neutral", analysis.sentiment.polarity

def main():
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.set_page_config(
    page_title="Twitter Crypto Sentiment Analysis",
    page_icon="💲",
    layout="wide",
    initial_sidebar_state="expanded"
    )
            
    st.title("Crypto Sentiment Analysis")
    st.markdown(
        """
        <style>
            body {
                background-color: #f7f7f7;
            }
            .text-input {
                color: #000000;
            }
            .st-bw {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                color: #000000;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.write("Enter your crypto-related text below to analyze its sentiment:")

    crypto_text = st.text_area("Enter text here:", height=150, max_chars=500, key='text-input')

    st.markdown(
        """
        <style>
            div[class^="st-"] div div div textarea {
                color: black;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Analyze"):
        if crypto_text:
            sentiment_label, sentiment_intensity = analyze_sentiment(crypto_text)
            st.markdown(f"<div class='st-bw'>Sentiment: <b>{sentiment_label}</b></div>", unsafe_allow_html=True)

            chart_data = {
                "Sentiment": ["Positive", "Negative", "Neutral"],
                "Intensity": [0, 0, 0]
            }
            if sentiment_intensity > 0:
                chart_data["Intensity"][0] = sentiment_intensity
            elif sentiment_intensity < 0:
                chart_data["Intensity"][1] = abs(sentiment_intensity)
            else:
                chart_data["Intensity"][2] = 1

            bar_fig = px.bar(chart_data, x="Sentiment", y="Intensity", color="Sentiment")
            bar_fig.update_traces(marker=dict(line=dict(color='rgb(255,255,255)', width=2)))

            st.plotly_chart(bar_fig)

            pie_fig = px.pie(names=chart_data["Sentiment"], values=chart_data["Intensity"], title="Sentiment Intensity Distribution")
            st.plotly_chart(pie_fig)

        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main()
