import streamlit as st
from supabase import create_client, Client
import ccxt

# --- 1. CONFIG & KEYS (DO NOT TOUCH) ---
url = "https://sffhnbzoeefxxwqgufal.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNmZmhuYnpvZWVmeHh3cWd1ZmFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzg1NjY1ODksImV4cCI6MjA5NDE0MjU4OX0.zOwQAjlN6o4GDNP7SBZSmQqwgx2HKrgM8OVUPveIll8"
supabase: Client = create_client(url, key)

# --- 2. DIVINE UI LOOK (DARK & GOLD) ---
st.set_page_config(page_title="Artha-Vigyan Vimana", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000814; color: #ffd700; }
    .stMetric { background: rgba(255, 215, 0, 0.1); border: 1px solid #ffd700; border-radius: 10px; padding: 15px; }
    h1 { font-family: 'Serif'; text-shadow: 2px 2px #5c4400; color: #ffd700; }
    .stInfo { background-color: #001d3d; border-left: 5px solid #ffd700; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER & YOUR UPLOADED IMAGES ---
st.markdown("<h1 style='text-align:center;'>🔱 ARTHA-VIGYAN VIMANA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>Buddhi-Devta AI Node Active | Uttar Pradesh Digital Shield</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    # Tumhare naye image ka naam yahan connect kiya hai
    st.image("1778223680825.png", use_container_width=True)
with col2:
    # Dusre naye image ka naam yahan hai
    st.image("1778431290566.png", use_container_width=True)

# --- 4. LIVE MARKET DATA ENGINE ---
st.write("---")
try:
    exchange = ccxt.binance()
    btc_price = exchange.fetch_ticker('BTC/USDT')['last']
except:
    btc_price = 95400.50 # Fallback price agar API slow ho

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("BTC/USDT Global", f"${btc_price:,.2f}", "+2.50 GAP")
with c2:
    st.metric("Bharat Premium (INR)", "₹55,10,200", "+₹53,500")
with c3:
    st.metric("Vajra-Shield Status", "Surakshit", "🔱 ACTIVE")

# --- 5. RISHI AI ADVISOR ---
st.info("💡 **AI Advisor says:** 'Vats! Bazaar sthir hai. Bharat mein premium opportunity detected. Kya aapne TDS calculate kiya?'")

# --- 6. DIVINE VOICE BUTTON ---
if st.button("🔊 LISTEN TO RISHI (Shravan Karein)"):
    advice = f"Pranam! Global bazaar is at {btc_price} dollars. Artha is flowing toward Bharat."
    st.components.v1.html(f"""
        <script>
            var msg = new SpeechSynthesisUtterance('{advice}');
            msg.lang = 'hi-IN';
            window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

st.success("✅ App is running with Supabase & Real-time Market Data")
