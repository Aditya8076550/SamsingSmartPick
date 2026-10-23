import os
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Samsung SmartPick", page_icon="📱", layout="wide")

# Demo data for an educational prototype; specifications/prices are illustrative, not live offers.
PRODUCTS = [
    {"name":"Galaxy A16 5G","price":17999,"camera":65,"battery":82,"performance":58,"display":70,"storage":128,"use":"Everyday","ecosystem":"Starter","description":"Budget-friendly everyday phone for calls, study, browsing and social apps."},
    {"name":"Galaxy A26 5G","price":24999,"camera":73,"battery":80,"performance":68,"display":78,"storage":128,"use":"Everyday","ecosystem":"Starter","description":"Balanced phone for daily use, photos, streaming and multitasking."},
    {"name":"Galaxy A36 5G","price":32999,"camera":78,"battery":78,"performance":76,"display":84,"storage":256,"use":"Content","ecosystem":"Starter","description":"A balanced option for creators who shoot photos and watch lots of video."},
    {"name":"Galaxy A56 5G","price":41999,"camera":82,"battery":78,"performance":82,"display":86,"storage":256,"use":"Content","ecosystem":"Connected","description":"Higher mid-range performance for content, gaming and multitasking."},
    {"name":"Galaxy S24 FE","price":54999,"camera":88,"battery":75,"performance":88,"display":88,"storage":256,"use":"Gaming","ecosystem":"Connected","description":"Performance-focused option for demanding apps, games and photography."},
    {"name":"Galaxy S24","price":69999,"camera":91,"battery":74,"performance":93,"display":92,"storage":256,"use":"Gaming","ecosystem":"Connected","description":"Compact flagship-style experience with strong performance and display."},
    {"name":"Galaxy S24 Ultra","price":109999,"camera":98,"battery":82,"performance":98,"display":99,"storage":512,"use":"Creator","ecosystem":"Advanced","description":"Premium choice for advanced photography, productivity and demanding workloads."},
    {"name":"Galaxy Z Flip6","price":89999,"camera":87,"battery":69,"performance":91,"display":91,"storage":256,"use":"Creator","ecosystem":"Advanced","description":"Foldable design for users who value portability and flexible camera angles."},
]

st.markdown("""
<style>
.stApp {background: linear-gradient(180deg, #f7f8fc 0%, #ffffff 45%);}
.hero {padding: 1.5rem 1.7rem; border-radius: 20px; background: #101828; color: white; margin-bottom: 1rem;}
.hero h1 {margin:0; font-size:2.2rem;}
.hero p {color:#d0d5dd; margin:.4rem 0 0 0;}
.small-note {color:#667085; font-size:.85rem;}
.product {border:1px solid #e4e7ec; border-radius:16px; padding:1rem; background:white; min-height:220px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>📱 Samsung SmartPick</h1><p>A simple AI-inspired mobile recommendation system — choose what matters to you and discover a phone that fits.</p></div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("Your preferences")
    budget = st.slider("Maximum budget (₹)", 15000, 120000, 55000, step=1000)
    purpose = st.selectbox("Main use", ["Everyday", "Photography & content", "Gaming & performance", "Study & multitasking", "Premium / productivity"])
    camera = st.slider("Camera importance", 1, 5, 3)
    battery = st.slider("Battery importance", 1, 5, 4)
    performance = st.slider("Performance importance", 1, 5, 3)
    display = st.slider("Display importance", 1, 5, 3)
    storage_min = st.selectbox("Minimum storage", [128, 256, 512], index=0)
    ecosystem = st.selectbox("Samsung ecosystem interest", ["Any", "Starter", "Connected", "Advanced"])
    recommend = st.button("✨ Find my best matches", type="primary", use_container_width=True)

purpose_map = {
    "Everyday": {"camera":0.15,"battery":0.30,"performance":0.20,"display":0.20,"storage":0.15},
    "Photography & content": {"camera":0.35,"battery":0.15,"performance":0.15,"display":0.20,"storage":0.15},
    "Gaming & performance": {"camera":0.10,"battery":0.20,"performance":0.40,"display":0.20,"storage":0.10},
    "Study & multitasking": {"camera":0.10,"battery":0.25,"performance":0.25,"display":0.20,"storage":0.20},
    "Premium / productivity": {"camera":0.25,"battery":0.15,"performance":0.25,"display":0.20,"storage":0.15},
}

def score_product(p):
    weights = purpose_map[purpose].copy()
    # User sliders personalize the feature weights. This is a transparent weighted-score model.
    slider_weights = {"camera": camera, "battery": battery, "performance": performance, "display": display}
    for key in slider_weights:
        weights[key] = weights[key] * slider_weights[key]
    total = sum(weights.values())
    weights = {k: v/total for k,v in weights.items()}
    raw = (p["camera"]*weights["camera"] + p["battery"]*weights["battery"] +
           p["performance"]*weights["performance"] + p["display"]*weights["display"] +
           min(p["storage"]/512*100, 100)*weights["storage"])
    # A soft affordability adjustment ranks within-budget products first; out-of-budget devices are excluded below.
    return round(raw, 1)

df = pd.DataFrame(PRODUCTS)
df["score"] = df.apply(score_product, axis=1)
filtered = df[(df["price"] <= budget) & (df["storage"] >= storage_min)]
if ecosystem != "Any":
    filtered = filtered[filtered["ecosystem"] == ecosystem]
if purpose == "Photography & content":
    filtered = filtered[filtered["use"].isin(["Content","Creator","Everyday"])]
elif purpose == "Gaming & performance":
    filtered = filtered[filtered["use"].isin(["Gaming","Creator"])]
elif purpose == "Premium / productivity":
    filtered = filtered[filtered["ecosystem"].isin(["Connected","Advanced"])]

filtered = filtered.sort_values(["score","price"], ascending=[False, True])

if recommend or True:
    st.subheader("Your recommendations")
    st.caption("Recommendations are based on your selected budget, use case, storage and feature priorities.")
    if filtered.empty:
        st.warning("No demo phones match every filter. Try increasing your budget, lowering storage, or selecting Ecosystem: Any.")
    else:
        top = filtered.head(3)
        cols = st.columns(len(top))
        for col, (_, p) in zip(cols, top.iterrows()):
            with col:
                st.markdown(f'<div class="product"><h3>{p["name"]}</h3><h2>₹{int(p["price"]):,}</h2><p>{p["description"]}</p></div>', unsafe_allow_html=True)
                st.progress(min(float(p["score"])/100, 1.0), text=f"Preference match score: {p['score']}/100")
                st.write(f"**Camera:** {p['camera']}/100")
                st.write(f"**Battery:** {p['battery']}/100")
                st.write(f"**Performance:** {p['performance']}/100")
                st.write(f"**Display:** {p['display']}/100")
                st.write(f"**Storage:** {int(p['storage'])} GB")
                st.write(f"**Ecosystem fit:** {p['ecosystem']}")
    st.divider()
    st.subheader("Why this recommendation?")
    if not filtered.empty:
        best = filtered.iloc[0]
        reasons = []
        if best["price"] <= budget:
            reasons.append(f"fits your budget of ₹{budget:,}")
        if best["storage"] >= storage_min:
            reasons.append(f"meets your {storage_min} GB storage preference")
        high_features = sorted([("camera",camera,best["camera"]),("battery",battery,best["battery"]),("performance",performance,best["performance"]),("display",display,best["display"])], key=lambda x:x[1], reverse=True)
        for name, importance, value in high_features[:2]:
            reasons.append(f"matches your priority for {name} (score {value}/100)")
        explanation = f"{best['name']} is the top match because it " + ", ".join(reasons) + "."
        st.info(explanation)
        st.markdown("**GenAI explanation (optional):** If you add a Gemini API key, the app can rewrite this result in natural language. Without a key, the transparent explanation above still works.")
        api_key = os.getenv("GEMINI_API_KEY", "")
        if api_key and st.button("Generate GenAI explanation"):
            try:
                from google import genai
                client = genai.Client(api_key=api_key)
                prompt = (
                    "You are a concise Samsung phone shopping assistant. Use only these supplied demo facts; "
                    "do not invent specs or claim live prices. Explain in 3 short bullets why this phone matches the user's preferences. "
                    f"User purpose: {purpose}. Budget: INR {budget}. Product: {best['name']}, price INR {int(best['price'])}, "
                    f"camera score {best['camera']}, battery score {best['battery']}, performance score {best['performance']}, "
                    f"display score {best['display']}, storage {int(best['storage'])} GB. "
                    f"Match score {best['score']}/100. Mention scores are demo scores."
                )
                response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                st.success(response.text)
            except Exception as e:
                st.error("GenAI request failed. Check your API key and internet connection. The regular recommendation still works.")
    st.divider()
    st.subheader("Compare matching phones")
    if not filtered.empty:
        view = filtered[["name","price","score","camera","battery","performance","display","storage","ecosystem"]].copy()
        view = view.rename(columns={"name":"Phone","price":"Price (₹)","score":"Match score","camera":"Camera","battery":"Battery","performance":"Performance","display":"Display","storage":"Storage (GB)","ecosystem":"Ecosystem"})
        st.dataframe(view, use_container_width=True, hide_index=True)
        st.download_button("Download comparison as CSV", view.to_csv(index=False).encode("utf-8"), "smartpick_comparison.csv", "text/csv")

with st.expander("How this mini-project works"):
    st.markdown("""
    1. **Input:** You select budget, use case, storage and feature priorities.
    2. **Data:** The app uses a small structured table of illustrative phone features.
    3. **Feature engineering:** Camera, battery, performance, display and storage are numeric features.
    4. **Scoring:** A weighted score ranks phones. Higher slider values give a feature more influence.
    5. **Filtering:** Phones outside the budget or selected constraints are removed.
    6. **Explanation:** The app states why the top match fits. Optional Gemini integration generates a natural-language explanation.

    This is a content-based, rule/score-driven recommendation prototype, not a trained machine-learning model. Product data and scores are demo values and should be replaced with verified current specifications before real use.
    """)

st.markdown('<p class="small-note">Educational mini-project inspired by the Samsung Mobile recommendation-system topic. This is an independent student prototype, not an official Samsung product or price listing.</p>', unsafe_allow_html=True)
