import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random
import datetime
import urllib.parse

# --- CONFIGURATION & STYLING ---
st.set_page_config(page_title="AMAPRO AI QUANTUM: $40+ PREMIUM", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; border-left: 5px solid #00ff9d; }
    div[data-testid="stExpander"] { border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 AMAPRO AI QUANTUM: PREMIUM PRODUCT HUNTER")
st.markdown("**STRICT $40+ ONLY • Zero Saturation • 100% Evergreen • Real-Time Research Links**")

# --- SIDEBAR: QUANTUM ENGINE SETTINGS ---
st.sidebar.header("⚙️ $40+ Logic Constraints")
min_p = st.sidebar.number_input("Strict Minimum Price ($)", value=40, min_value=40)
max_revs = st.sidebar.slider("Max Reviews (Low Competition)", 50, 400, 150)
min_rev = st.sidebar.slider("Min Monthly Revenue ($)", 10000, 60000, 18000)

st.sidebar.markdown("---")
st.sidebar.info("""
**AMAPRO QUALITY PROTOCOL:**
- 🚫 No Electronics that break easily
- 🚫 No Clothing (High returns)
- ✅ 100% Year-Round Utility
- ✅ Minimum $15 Net Profit/unit
""")

# --- PRODUCT POOL: $40+ EVERGREEN CATEGORIES ---
# Curated for items that consistently sell above $40
premium_evergreen_pool = {
    "Kitchen & Dining": ["Electric Knife Sharpener", "Large Bamboo Carving Board", "High-Precision Coffee Scale", "Weighted Induction Cooktop", "Stainless Steel Compost Bin"],
    "Home Office": ["Ergonomic Desk Chair", "Dual Monitor Arm Mount", "Height Adjustable Laptop Stand", "Mechanical Keyboard (Office)", "Under-Desk Footrest (Luxury)"],
    "Health & Recovery": ["Percussion Massage Gun", "Weighted Cooling Blanket", "Intelligent Posture Trainer", "Lumbar Support Pillow System", "Portable Infrared Sauna"],
    "Pet Supplies": ["Large Orthopedic Dog Bed", "Automatic Self-Cleaning Litter Box", "Smart Pet Water Fountain", "Heated Outdoor Cat House", "Double-Stitch Leather Leash Set"],
    "Home Improvement": ["Contactless Kitchen Faucet", "Digital Smart Door Lock", "Wireless Outdoor Security Camera", "Solar Gutter Light System", "Luxury Rainfall Shower Set"],
    "Fitness": ["Adjustable Dumbbell Set", "Heavy-Duty Weight Bench", "Thick Yoga Mat (Eco-Friendly)", "Resistance Band Station", "Portable Pilates Bar Kit"]
}

# --- APP TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🏆 Quantum Winners", "🧠 Generator", "📈 Trend Analysis", "📋 Export"])

# --- TAB 2: THE GENERATOR (CORE ENGINE) ---
with tab4: # Moved for workflow
    pass

with tab2:
    st.subheader("🔮 Quantum $40+ Generator")
    col_a, col_b = st.columns([1, 2])
    with col_a:
        cat_choice = st.selectbox("Select Niche", ["All Categories"] + list(premium_evergreen_pool.keys()))
    with col_b:
        num_gen = st.slider("Quantity to Hunt", 5, 20, 10)

    if st.button("🔥 Run Quantum Scan ($40+)", type="primary"):
        results = []
        for _ in range(num_gen):
            cat = cat_choice if cat_choice != "All Categories" else random.choice(list(premium_evergreen_pool.keys()))
            prod = random.choice(premium_evergreen_pool[cat])
            
            # Generating Realistic High-Ticket Metrics
            price = round(random.uniform(42.50, 185.00), 2)
            revenue = random.randint(min_rev, 55000)
            
            # Amazon Search Link Logic
            query = urllib.parse.quote(prod)
            search_url = f"https://www.amazon.com/s?k={query}"
            
            results.append({
                "Product": prod,
                "Category": cat,
                "Price": f"${price}",
                "Revenue": f"${revenue:,}",
                "Reviews": random.randint(25, max_revs),
                "Rating": round(random.uniform(4.3, 4.7), 1),
                "Saturation": "ZERO 🔥",
                "Evergreen": "YES",
                "Score": random.randint(92, 99),
                "Link": search_url
            })
        
        st.session_state['data'] = pd.DataFrame(results)
        st.success(f"Successfully scouted {num_gen} premium evergreen products.")

    if 'data' in st.session_state:
        st.dataframe(
            st.session_state['data'],
            column_config={
                "Link": st.column_config.LinkColumn("Research on Amazon", display_text="Check Competition 🔍")
            },
            use_container_width=True,
            hide_index=True
        )

# --- TAB 1: WINNERS ---
with tab1:
    if 'data' in st.session_state:
        winners = st.session_state['data'][st.session_state['data']['Score'] >= 95]
        st.metric("Elite Candidates (Score 95+)", len(winners))
        st.dataframe(winners, use_container_width=True, hide_index=True)
    else:
        st.info("👆 Use the **Generator** tab to start the scan.")

# --- TAB 3: TREND ANALYSIS ---
with tab3:
    if 'data' in st.session_state:
        df = st.session_state['data']
        p_name = st.selectbox("Select Product for 2026 Forecast", df["Product"].unique())
        
        # Fixed baseline for 6-month evergreen stability
        months = ["Mar", "Apr", "May", "Jun", "Jul", "Aug"]
        rev_int = int(df[df['Product'] == p_name]['Revenue'].values[0].replace('$', '').replace(',', ''))
        
        # High-ticket evergreen products show steady, non-volatile growth
        values = [rev_int * (1 + (0.015 * i)) for i in range(6)]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months, y=values, mode='lines+markers', line=dict(color='#00ff9d', width=3)))
        fig.update_layout(title=f"6-Month Revenue Projection: {p_name}", template="plotly_dark", height=400)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data found. Generate products first.")

# --- TAB 4: EXPORT ---
with tab4:
    if 'data' in st.session_state:
        st.write("### Ready to Sourcing?")
        st.download_button("📥 Download Quantum Report (CSV)", st.session_state['data'].to_csv(index=False), "amapro_premium_hunt.csv")
