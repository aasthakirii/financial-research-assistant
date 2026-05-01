import streamlit as st
import requests

BACKEND_URL = "https://financial-research-assistant-e9u7.onrender.com/analyze"

st.set_page_config(
    page_title="FinSight AI",
    page_icon="💖",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom right, #ffd6e8, #ffe6f2);
}

h1 {
    color: black;
    text-align: center;
    font-size: 55px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: black;
    font-size: 20px;
    margin-bottom: 30px;
}

.stButton button {
    background-color: black;
    color: white;
    border-radius: 12px;
    width: 100%;
    height: 50px;
    font-size: 18px;
}

.result-card {
    background-color: white;
    color: black;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>💸 FinSight AI</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>Cute but powerful stock analysis ✨📈</p>",
    unsafe_allow_html=True
)

ticker = st.text_input("Enter Stock Ticker", placeholder="AAPL, TSLA, MSFT")

if st.button("Analyze 🚀"):
    if ticker:
        try:
            with st.spinner("Analyzing..."):
                response = requests.post(
                    BACKEND_URL,
                    json={"ticker": ticker},
                    timeout=60
                )

            if response.status_code == 200:
                data = response.json()

                if "analysis" in data:
                    st.markdown(
                        f"""
                        <div class="result-card">
                            <h3>📊 Analysis Report</h3>
                            <p>{data['analysis']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.error("No analysis returned.")

            else:
                st.error("Backend error")

        except Exception as e:
            st.error(str(e))