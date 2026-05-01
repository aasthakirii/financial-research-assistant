import streamlit as st
import requests

BACKEND_URL = "https://financial-research-assistant-e9u7.onrender.com/analyze"

st.set_page_config(
    page_title="FinSight AI",
    page_icon="💸",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

/* Full page background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffd6e8, #ffeaf4);
}

/* Remove dark header */
[data-testid="stHeader"] {
    background: transparent;
}

/* Input box styling */
.stTextInput input {
    background-color: white !important;
    color: black !important;
    border-radius: 12px !important;
    border: 2px solid #ff9fcf !important;
    padding: 10px;
}

/* Button styling */
.stButton button {
    background-color: black !important;
    color: white !important;
    border-radius: 12px !important;
    width: 100%;
    height: 55px;
    font-size: 18px;
    font-weight: bold;
    border: none !important;
}

/* Button hover */
.stButton button:hover {
    background-color: #333 !important;
}

/* Result card */
.result-card {
    background-color: white;
    color: black;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
    margin-top: 20px;
}

/* Hide footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    """
    <h1 style='text-align:center; color:black; font-size:55px;'>
    💸 FinSight AI
    </h1>
    """,
    unsafe_allow_html=True
)

# Subtitle
st.markdown(
    """
    <p style='text-align:center; color:black; font-size:20px;'>
    Cute but powerful stock analysis ✨📈
    </p>
    """,
    unsafe_allow_html=True
)

# Input
ticker = st.text_input(
    "Enter Stock Ticker",
    placeholder="AAPL, TSLA, MSFT"
)

# Analyze Button
if st.button("Analyze 🚀"):
    if ticker:
        try:
            with st.spinner("Analyzing company data... 📊"):
                response = requests.post(
                    BACKEND_URL,
                    json={"ticker": ticker.upper()},
                    timeout=60
                )

            if response.status_code == 200:
                data = response.json()

                if "analysis" in data:
                    st.markdown(
                        f"""
                        <div class="result-card">
                            <h2>📊 Analysis Report</h2>
                            <p>{data['analysis']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                elif "error" in data:
                    st.error(data["error"])

                else:
                    st.error("Unexpected backend response.")

            else:
                st.error("Backend error occurred.")

        except requests.exceptions.Timeout:
            st.warning(
                "Backend is waking up (Render free tier). Try again in 30 seconds."
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")

    else:
        st.warning("Please enter a stock ticker.")