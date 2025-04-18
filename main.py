import streamlit as st

# Page title and layout
st.set_page_config(
    page_title="Career Test – Practical EduSkills",
    page_icon="🎓",
    layout="centered"
)

# === THEME COLOR STYLE ===
st.markdown("""
    <style>
    body {
        background-color: #1B1B2F;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #2A2A40;
        color: white;
    }
    .stTextInput label, .stTextArea label {
        color: white;
        font-weight: bold;
    }
    .stButton button {
        background-color: #F2B233;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stSuccess {
        color: #ABEBC6 !important;
    }
    .stWarning {
        color: #F5B041 !important;
    }
    </style>
""", unsafe_allow_html=True)

# === MAIN INTERFACE ===
st.title("BBA vs BCom Career Test")
st.markdown("Welcome to **Practical EduSkills Career Guidance Platform** 👋")
st.write("Let’s begin by knowing who you are.")

st.markdown("---")

# === Student Info Form ===
with st.form(key='student_form'):
    name = st.text_input("👤 Full Name")
    phone = st.text_input("📞 Mobile Number")
    city = st.text_input("🏙️ City / Location")
    start_test = st.form_submit_button("🚀 Start Test")

# === On Submission ===
if start_test:
    if name and phone and city:
        st.success(f"Hi {name}! You’re ready to begin the test.")
    else:
        st.warning("Please fill in all fields to continue.")
