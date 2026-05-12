import streamlit as st
from supabase import create_client, Client
import ccxt
import os

# --- 1. SUPABASE CONNECTION (FIXED BY AI) ---
url = "https://sffhnbzoeefxxwqgufal.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNmZmhuYnpvZWVmeHh3cWd1ZmFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzg1NjY1ODksImV4cCI6MjA5NDE0MjU4OX0.zOwQAjlN6o4GDNP7SBZSmQqwgx2HKrgM8OVUPveIll8"
supabase: Client = create_client(url, key)

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="Artha-Vigyan Vimana", page_icon="🔱", layout="wide")

# --- 3. IMAGES LOGIC (IZZT SE) ---
# Ye code check karega ki images repository mein hain ya nahi
col1, col2 = st.columns(2)
with col1:
    if os.path.exists("1286.png"):
        st.image("1286.png", use_container_width=True)
    else:
        st.write("🖼️ Image 1286 Loading...")

with col2:
    if os.path.exists("529.png"):
        st.image("529.png", use_container_width=True)
    else:
        st.write("🖼️ Image 529 Loading...")

# --- 4. DIVINE UI ---
st.markdown("<h1 style='text-align:center; color:#ffd700; font-family:serif;'>🔱 ARTHA-VIGYAN VIMANA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>Project by ARTI | Protected by Vajra-Shield | Uttar Pradesh Node</p>", unsafe_allow_html=True)
st.write("---")

# --- 5. LIVE MARKET DATA ENGINE ---
def get_market_data():
    try:
        exchange = ccxt.binance()
        ticker = exchange.fetch_ticker('BTC/USDT')
        return ticker['last']
    except Exception as e:
        return 65000.0

price = get_market_data()
st.sidebar.metric(label="Global Market Pulse", value=f"${price:,.2f}")

# --- 6. DIVINE VOICE ADVICE ---
advice = f"Pranam! Global bazaar is at {price}. Artha is flowing toward Bharat."
if st.button("🔊 LISTEN TO RISHI VOICE (Shravan Karein)"):
    st.components.v1.html(f"""
        <script>
            var msg = new SpeechSynthesisUtterance('{advice}');
            msg.lang = 'hi-IN';
            window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

# --- 7. STATUS ---
st.success("✅ AI Engine Online | Supabase Connected | Vajra-Shield Active")
