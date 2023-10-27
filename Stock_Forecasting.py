import pandas as pd
import yfinance as yf
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Stock Price Forecasting",
    page_icon="🎯",
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

st.title("Stock Price Forecasting")
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

company_data = {
    'Ticker': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NFLX', 'IBM', 'NVDA', 'AMD'],
    'Company Name': ['Apple Inc.', 'Microsoft Corporation', 'Alphabet Inc.', 'Amazon.com Inc.', 
                      'Tesla, Inc.', 'Netflix, Inc.', 'International Business Machines Corporation', 
                      'NVIDIA Corporation', 'Advanced Micro Devices, Inc.']
}

company_df = pd.DataFrame(company_data)

selected_ticker = st.selectbox("Select a Stock Ticker:", company_df['Ticker'])

selected_company_name = company_df.loc[company_df['Ticker'] == selected_ticker, 'Company Name'].iloc[0]

ma_days = st.slider("Select Moving Average Day Count:", min_value=1, max_value=30, value=7)

def predict_stock_price(ticker, ma_days):
    data = yf.download(ticker, period="1y")
    
    ma_column = f'MA{ma_days}'
    data[ma_column] = data['Close'].rolling(window=ma_days).mean()
    
    fig = px.line(data, x=data.index, y=['Close', ma_column], labels={'value': 'Price', 'variable': 'Type'}, 
                  title=f'Stock Price and {ma_days}-day Moving Average for {selected_company_name}')
    
    # fig = px.line(data, x=data.index, y=['Close', ma_column], labels={'value': 'Price', 'variable': 'Type'}, 
    #           title=f'Stock Price and {ma_days}-day Moving Average for {selected_company_name}')
    
    ma_table = data[[ma_column]].tail(10)
    
    last_close_price = data['Close'].iloc[-1]
    predicted_close_price = data[ma_column].iloc[-1]
    predicted_next_day_close = (predicted_close_price - last_close_price) + data['Close'].iloc[-1]
    
    return fig, ma_table, predicted_next_day_close



if selected_ticker and ma_days:
    data = yf.download(selected_ticker, period="1y")
    st.write(f"Generating forecast for {selected_company_name} ({selected_ticker}) with {ma_days}-day Moving Average...")
    fig, ma_table, predicted_next_day_close = predict_stock_price(selected_ticker, ma_days)
    
    st.plotly_chart(fig, use_container_width=True)
    
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'])])

    # Update chart layout and appearance
    fig.update_layout(title=f"Candlestick Chart for {selected_ticker}",
                    xaxis_title='Date',
                    yaxis_title='Price',
                    xaxis_rangeslider_visible=False)

    # Display the candlestick chart
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("Moving Average Table (Last 10 Days):")
    st.table(ma_table)
    
    st.write("Predicted Next Day's Closing Price:")
    st.write(predicted_next_day_close)
