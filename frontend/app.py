import streamlit as st
import requests

st.title("Financial Research Assistant")

ticker = st.text_input("Enter Ticker (AAPL, MSFT...)")

if st.button("Analyze"):
    try:
        res = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={"ticker": ticker}
        )

        print(res.text)  # helps debug

        if res.status_code != 200:
            st.error(f"Backend error: {res.text}")
        else:
            data = res.json()
            st.success("Analysis Complete!")
            st.write(data["summary"])

    except Exception as e:
        st.error(f"Error: {str(e)}")