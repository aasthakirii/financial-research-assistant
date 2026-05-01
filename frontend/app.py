import streamlit as st
import requests

# Render backend URL
BACKEND_URL = "https://financial-research-assistant-e9u7.onrender.com/analyze"

st.set_page_config(
    page_title="Financial Research Assistant",
    page_icon="📈",
    layout="centered"
)

st.title("Financial Research Assistant")

ticker = st.text_input(
    "Enter Ticker (AAPL, MSFT...)"
)

if st.button("Analyze"):
    if ticker:
        try:
            with st.spinner("Analyzing company..."):
                response = requests.post(
                    BACKEND_URL,
                    json={"ticker": ticker},
                    timeout=60
                )

            if response.status_code == 200:
                data = response.json()

                if "analysis" in data:
                    st.success("Analysis Complete!")

                    st.write(data["analysis"])

                elif "error" in data:
                    st.error(data["error"])

                else:
                    st.error("Unexpected response from backend")

            else:
                st.error(f"Backend Error: {response.status_code}")

        except requests.exceptions.Timeout:
            st.error(
                "Request timed out. Render free tier may be waking up. Try again in 30 seconds."
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")

    else:
        st.warning("Please enter a stock ticker.")