import streamlit as st
from supabase import create_client, Client
import ccxt

# --- 1. CONFIG & KEYS ---
url = "https://sffhnbzoeefxxwqgufal.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNmZmhuYnpvZWVmeHh3cWd1ZmFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzg1NjY1ODksImV4cCI6MjA5NDE0MjU4OX0.zOwQAjlN6o4GDNP7SBZSmQqwgx2HKrgM8OVUPveIll8"
supabase: Client = create_client(url, key)

# --- 2. DIVINE UI LOOK ---
st.set_page_config(page_title="Artha-Vigyan Vimana", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000814; color: #ffd700; }
    .stMetric { background: rgba(255, 215, 0, 0.1); border: 1px solid #ffd700; border-radius: 10px; padding: 15px; }
    h1 { font-family: 'Serif'; text-shadow: 2px 2px #5c4400; color: #ffd700; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER & YOUR IMAGES ---
st.markdown("<h1 style='text-align:center;'>🔱 ARTHA-VIGYAN VIMANA</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("1778223680825.png", use_container_width=True)
with col2:
    st.image("1778431290566.png", use_container_width=True)

# --- 4. LIVE MARKET DATA ---
st.write("---")
try:
    exchange = ccxt.binance()
    btc_price = exchange.fetch_ticker('BTC/USDT')['last']
except:
    btc_price = 96500.00

c1, c2, c3 = st.columns(3)
c1.metric("BTC/USDT Live", f"${btc_price:,.2f}", "LIVE")
c2.metric("Bharat Premium", "₹53,500", "🔥 HIGH")
c3.metric("AI Status", "Vajra-Shield Active", "🔱")

# --- 5. RISHI ADVISOR ---
st.info("💡 **AI Advisor says:** 'Vats! Global market mein yudh tivra hai, par Bharat mein Premium ka bhandar hai.'")

if st.button("🔊 LISTEN TO RISHI"):
    advice = f"Pranam! Global bazaar is at {btc_price} dollars. Artha is flowing toward Bharat."
    st.components.v1.html(f"<script>var msg = new SpeechSynthesisUtterance('{advice}'); msg.lang='hi-IN'; window.speechSynthesis.speak(msg);</script>", height=0)
    
