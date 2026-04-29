import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(page_title="RCB Reality Check", layout="wide")

st.markdown("""
<style>

/* Full app background */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #000000 !important;
}

/* Remove default padding color */
[data-testid="stHeader"] {
    background: #000000 !important;
}

/* Main container */
.main {
    background-color: #000000 !important;
    color: #ffffff;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #000000 !important;
}

/* Text colors */
h1, h2, h3, h4, h5, h6 {
    color: #ff1a1a;
    text-shadow: 0 0 10px rgba(255,0,0,0.4);
}
p, div, span {
    color: #ffffff;
}

/* Cards */
.card {
    background: #0f0f0f;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #ff1a1a;
    box-shadow: 0 0 15px rgba(255,0,0,0.25);
    transition: 0.3s;
    text-align: center;
    font-weight: 500;
}
.card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(255,0,0,0.6);
}

/* Footer */
.footer-box {
    background: #000000;
    border-top: 2px solid #ff1a1a;
    padding: 30px;
    text-align: center;
    margin-top: 50px;
}

/* Buttons */
.stButton>button {
    background-color: #ff1a1a;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #cc0000;
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

st.title("🔴 RCB Reality Check")
st.subheader("Chaos • Collapses • Records")

st.metric("🔥 Lowest Total Ever", "49 ALL OUT", "vs RR (2009)")
st.divider()

records = [
    "49 all out vs RR (2009)",
    "70 all out vs KKR (2008)",
    "3 wickets for 0 (2022 collapse)",
    "Biggest loss by 146 runs vs CSK",
    "Conceded 263 runs in an innings",
    "6 consecutive losses (2019)",
    "Lost 3 IPL finals (0 trophies)",
    "Multiple 200+ runs conceded matches",
    "Kohli low score in finals (8 runs)",
    "Frequent powerplay collapses",
]


st.header("💀 Worst Records")

cols = st.columns(3)
for i, rec in enumerate(records):
    with cols[i % 3]:
        st.markdown(f"<div class='card'>{rec}</div>", unsafe_allow_html=True)

st.divider()

st.header("📊 Collapse Frequency")

chart_df = pd.DataFrame({
    "Category": ["Batting Collapse", "Big Loss", "Bowling Failure", "Final Loss"],
    "Count": [8, 5, 6, 3]
})

fig = px.bar(chart_df, x="Category", y="Count")

# Make chart dark theme
fig.update_layout(
    plot_bgcolor="#000000",
    paper_bgcolor="#000000",
    font=dict(color="white")
)

st.plotly_chart(fig, use_container_width=True)

st.divider()


st.header("😂 Meme Zone")

memes = [
    "49 ALL OUT 💀",
    "Top order vanished",
    "Hope → Hype → Collapse",
    "'Ee Sala Cup Namde' again",
    "Bowling leaking runs",
]

cols = st.columns(3)
for i, meme in enumerate(memes):
    with cols[i % 3]:
        st.markdown(f"<div class='card'>{meme}</div>", unsafe_allow_html=True)

st.divider()


st.markdown("<div class='footer-box'>", unsafe_allow_html=True)

st.subheader("🎲 Reality Generator")

if "last_record" not in st.session_state:
    st.session_state.last_record = "Click below to reveal the next disaster 👇"

st.write(f"### {st.session_state.last_record}")

if st.button("Show Worst Record"):
    st.session_state.last_record = random.choice(records)

st.markdown("</div>", unsafe_allow_html=True)
