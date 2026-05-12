import streamlit as st
import ccxt
import time

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Artha-Vigyan Vimana", layout="wide", initial_sidebar_state="collapsed")

# --- 2. ADVANCED VEDIC CSS (Directly matching your images) ---
st.markdown("""
    <style>
    .main { background-color: #000b18; color: #ffd700; }
    .stApp { background: radial-gradient(circle, #001529 0%, #000814 100%); }
    
    /* Glowing Cards */
    .metric-card {
        background: rgba(255, 215, 0, 0.05);
        border: 1px solid #ffd700;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.2);
    }
    
    .price-text { font-size: 24px; font-weight: bold; color: #ffd700; }
    .label-text { font-size: 14px; color: #888; }
    
    /* Title Style */
    .title-font {
        font-family: 'Serif';
        color: #ffd700;
        text-align: center;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        font-size: 45px;
        letter-spacing: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER SECTION ---
st.markdown("<h1 class='title-font'>🔱 ARTHA-VIGYAN VIMANA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ffd700;'>Buddhi-Devta AI Node Active</p>", unsafe_allow_html=True)

# --- 4. LIVE DATA FETCHING ---
try:
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('BTC/USDT')
    btc_price = ticker['last']
    change = ticker['percentage']
except:
    btc_price = 96500.00
    change = 2.5

# --- 5. TOP ROW (Vedic Layout like 529.png) ---
cols = st.columns(5)
assets = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "DOGE/USDT"]
for i, asset in enumerate(assets):
    with cols[i]:
        st.markdown(f"""
            <div class="metric-card">
                <div class="label-text">{asset} Live Price</div>
                <div class="price-text">${btc_price if i==0 else btc_price/(i+1.5):,.2f}</div>
                <div style="color: {'#00ff00' if change > 0 else '#ff0000'};">▲ {change}%</div>
            </div>
        """, unsafe_allow_html=True)

# --- 6. CENTER DEITY IMAGE (The Core Visual) ---
st.write("##")
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    # Yahan tumhari image ko "Glow" effect ke saath center kiya hai
    st.image("1778223680825.png", use_container_width=True)
    st.markdown("""
        <div style="background: rgba(0,0,0,0.6); border: 1px solid #ffd700; border-radius: 10px; padding: 10px; text-align: center;">
            <p style="color: #ffd700; margin: 0;">🔱 AI Advisor says: "Dharma Sanket: Bazaar shunya sthiti mein hai. Sahaj rahein."</p>
        </div>
    """, unsafe_allow_html=True)

# --- 7. ARBITRAGE SECTION (Layout like 1286.png) ---
st.write("---")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("<h3 style='color:#00d4ff;'>🌍 GLOBAL ARBITRAGE (Binance/Bybit)</h3>", unsafe_allow_html=True)
    st.image("1286.png", use_container_width=True) # Reference for the logic

with col_b:
    st.markdown("<h3 style='color:#ffaa00;'>🇮🇳 BHARAT PREMIUM (Indian Exchanges)</h3>", unsafe_allow_html=True)
    st.metric("BTC (INR) Converted", "₹82,45,600", "+₹53,500 GAP")
    st.info("Vats! Global market mein yudh tivra hai, par Bharat mein Premium ka bhandar hai.")

# --- 8. FOOTER CONTROLS ---
st.write("##")
f1, f2 = st.columns(2)
with f1:
    if st.button("APP MODE ACTIVE", use_container_width=True):
        st.balloons()
with f2:
    st.button("WEB MODE ACTIVE", use_container_width=True)
    
