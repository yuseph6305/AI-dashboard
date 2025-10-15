# importing streamlit UI as st
import streamlit as st
# imports downloaded yfinace as yf
import yfinance as yf


# title of streamlit dashboard
st.title("Yuseph's AI-Powered Market Insight Dashboard")


# prompt to get ticker info deafulted to apple
ticker = st.text_input("Enter a stock ticker (e.g. AAPL, TSLA, MSFT):", "AAPL")

#variable to store user stock
stock = yf.Ticker(ticker)

#creates a Ticker object for the given symbol
info = stock.info


st.subheader(info['longName'])
st.write(f"**Sector:** {info.get('sector')}")
st.write(f"**P/E Ratio:** {info.get('trailingPE')}")
st.write(f"**Market Cap:** {info.get('marketCap'):,}")
st.write(f"**1-Year Change:** {info.get('52WeekChange'):.2%}")
try:
    analysis = stock.get_analysis()
    st.subheader("Analyst Price Targets / Forecasts")
    st.dataframe(analysis)
except Exception as e:
    st.write("Price target data unavailable.")

period = st.selectbox("Select time period:", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"])
data = stock.history(period=period)
st.line_chart(data["Close"])