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
        # Initialize session variables on first load
if "show_interest" not in st.session_state:
    st.session_state.show_interest = False
if start_test and name and phone and city:
    st.session_state.show_interest = True
    st.session_state.user_name = name

# === INTEREST SECTION ===
if st.session_state.show_interest:
    st.markdown("### Section 1: Your Interests")
    st.write("Select the option that best matches your preference.")

    bba_score = 0
    bcom_score = 0

    # Question 1
    q1 = st.radio("1. Which activity excites you more?",
        ["Managing events or campaigns", "Analyzing financial statements"])
    if q1 == "Managing events or campaigns":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 2
    q2 = st.radio("2. Which subject do you enjoy more?",
        ["Marketing and Business Studies", "Economics and Accountancy"])
    if q2 == "Marketing and Business Studies":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 3
    q3 = st.radio("3. What kind of problems do you prefer solving?",
        ["Team or people problems", "Number and calculation problems"])
    if q3 == "Team or people problems":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 4
    q4 = st.radio("4. Which club would you join in college?",
        ["Entrepreneurship club", "Finance club"])
    if q4 == "Entrepreneurship club":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 5
    q5 = st.radio("5. What excites you more in a newspaper?",
        ["Startups and business stories", "Budget, taxes, and economy updates"])
    if q5 == "Startups and business stories":
        bba_score += 1
    else:
        bcom_score += 1

    st.markdown("---")
    if st.button("👉 Next Section (Personality)"):
        st.session_state.bba_score = bba_score
        st.session_state.bcom_score = bcom_score
        st.success("Great! Moving to next section...")
        # Next section to be added on Day 4
