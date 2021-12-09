from bs4 import BeautifulSoup
import requests
import time
import streamlit as st

st.title('Bitcoin Exchange Rate')

coin = st.text_input("Enter Text")

def get_price(coin):
  url = "https://www.google.com/search?q="+coin+"+price"
  res = requests.get(url)
  soup = BeautifulSoup(res.text, "html.parser")
  #current price
  text = soup.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
  return text


if st.button("Show Price"):
    price = get_price(coin)
    st.write(price)
