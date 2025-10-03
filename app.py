import streamlit as st

# -------------------------------
# Dream Devotional Gamification
# Apostle Emeka Onyekwere Ministries
# -------------------------------

st.set_page_config(page_title="Dream Devotional Gamification", page_icon="🌟", layout="centered")

# POINTS RULES
POINTS_RULES = {
    "Share Devotional": 10,
    "Facebook Follow": 20,
    "YouTube Subscribe": 30,
    "Partnership Seed": 0  # handled separately
}

# SESSION STATE TO HOLD SCORES + SEEDS
if "scores" not in st.session_state:
    st.session_state["scores"] = {}
if "seeds" not in st.session_state:
    st.session_state["seeds"] = []  # list of dicts: {name, amount, points}

# FUNCTION TO ADD POINTS
def add_points(user, action, amount=0):
    if action == "Partnership Seed":
        points = amount // 100   # 1 point per ₦100
        st.session_state["seeds"].append({"name": user, "amount": amount, "points": points})
    else:
        points = POINTS_RULES.get(action, 0)

    st.session_state["scores"][user] = st.session_state["scores"].get(user, 0) + points
    return points

# APP HEADER
st.title("🌟 Dream Devotional Gamification")
st.write("**Eternal Value for Your Voice** — Apostle Emeka Onyekwere Ministries")

# SEED ACCOUNT DETAILS (your real account)
st.info("💳 Partnership Seed Account:\n\n"
        "Bank: Access Bank\n"
        "Account Name: Emeka Augustine Onyekwere\n"
        "Account Number: 1668708536")

# USER INPUT FORM
st.subheader("🎯 Submit Your Action")
with st.form("points_form"):
    user = st.text_input("Enter Your Name / Phone Number")
    action = st.selectbox("Select Action", list(POINTS_RULES.keys()))
    amount = st.number_input("Amount (₦) (only if Partnership Seed)", min_value=0, step=100)
    
    submitted = st.form_submit_button("✅ Submit Action")
    if submitted and user:
        pts = add_points(user, action, amount)
        st.success(f"✅ {user} earned {pts} points for **{action}**!")

# LEADERBOARD
st.subheader("🏆 Leaderboard")
sorted_scores = sorted(st.session_state["scores"].items(), key=lambda x: x[1], reverse=True)
if sorted_scores:
    for i, (name, score) in enumerate(sorted_scores, start=1):
        st.write(f"**{i}. {name}** — {score} points")
else:
    st.info("No entries yet. Be the first to log your action!")

# SEED TRANSACTIONS LOG
st.subheader("🌱 Partnership Seed Log")
if st.session_state["seeds"]:
    for seed in st.session_state["seeds"]:
        st.write(f"- {seed['name']} gave ₦{seed['amount']} → earned {seed['points']} points")
else:
    st.info("No partnership seeds recorded yet.")

# FOOTER
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Powered by Apostle Emeka Onyekwere Ministries</p>",
    unsafe_allow_html=True
)
