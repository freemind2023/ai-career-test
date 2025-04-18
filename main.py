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
        st.session_state.show_interest = False
        st.session_state.show_personality = True

# === SECTION 2: PERSONALITY TRAITS ===
if st.session_state.get("show_personality", False):
    st.markdown("### Section 2: Your Personality")
    st.write("Let’s understand your natural working style.")

    # Load previous scores
    bba_score = st.session_state.bba_score
    bcom_score = st.session_state.bcom_score

    # Question 6
    q6 = st.radio("6. You’re more comfortable...",
        ["Taking charge in a group", "Working alone with accuracy"])
    if q6 == "Taking charge in a group":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 7
    q7 = st.radio("7. How do you usually make decisions?",
        ["Quickly and confidently", "Carefully after research"])
    if q7 == "Quickly and confidently":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 8
    q8 = st.radio("8. Which describes you more?",
        ["Talkative and energetic", "Quiet and detail-focused"])
    if q8 == "Talkative and energetic":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 9
    q9 = st.radio("9. You prefer to work in...",
        ["Dynamic teams", "Structured environments"])
    if q9 == "Dynamic teams":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 10
    q10 = st.radio("10. How do you handle tasks?",
        ["Multi-task fast", "Focus on one task perfectly"])
    if q10 == "Multi-task fast":
        bba_score += 1
    else:
        bcom_score += 1

    st.markdown("---")
    if st.button("👉 Next Section (Skills)"):
        st.session_state.bba_score = bba_score
        st.session_state.bcom_score = bcom_score
        st.session_state.show_personality = False
        st.session_state.show_skills = True
        # === SECTION 3: SKILLS ASSESSMENT ===
if st.session_state.get("show_skills", False):
    st.markdown("### Section 3: Your Skills")
    st.write("Which of these skills best describe you?")

    # Load scores from previous sections
    bba_score = st.session_state.bba_score
    bcom_score = st.session_state.bcom_score

    # Question 11
    q11 = st.radio("11. Which is your strong point?",
        ["Convincing others", "Working with numbers"])
    if q11 == "Convincing others":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 12
    q12 = st.radio("12. You are better at...",
        ["Team leadership", "Detailed analysis"])
    if q12 == "Team leadership":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 13
    q13 = st.radio("13. Which task do you enjoy more?",
        ["Creating presentations", "Creating spreadsheets"])
    if q13 == "Creating presentations":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 14
    q14 = st.radio("14. Your communication skills are...",
        ["Very strong", "Average"])
    if q14 == "Very strong":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 15
    q15 = st.radio("15. When facing a challenge, you...",
        ["Motivate people and act", "Make a step-by-step plan"])
    if q15 == "Motivate people and act":
        bba_score += 1
    else:
        bcom_score += 1

    st.markdown("---")
    if st.button("👉 Final Section (Career Goals)"):
        st.session_state.bba_score = bba_score
        st.session_state.bcom_score = bcom_score
        st.session_state.show_skills = False
        st.session_state.show_goals = True
        # === SECTION 4: CAREER GOALS ===
if st.session_state.get("show_goals", False):
    st.markdown("### Final Section: Your Career Goals")
    st.write("Let’s understand your long-term preferences and aspirations.")

    # Load previous scores
    bba_score = st.session_state.bba_score
    bcom_score = st.session_state.bcom_score

    # Question 16
    q16 = st.radio("16. Which career path appeals to you more?",
        ["Management, startups or marketing", "Finance, banking or auditing"])
    if q16 == "Management, startups or marketing":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 17
    q17 = st.radio("17. What do you value most in a career?",
        ["Leadership opportunities", "Stability and structure"])
    if q17 == "Leadership opportunities":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 18
    q18 = st.radio("18. Where do you see yourself thriving?",
        ["In a business team or startup", "In a corporate office or government job"])
    if q18 == "In a business team or startup":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 19
    q19 = st.radio("19. What would you prefer to pursue after graduation?",
        ["MBA or entrepreneurship", "CA, CS or government exams"])
    if q19 == "MBA or entrepreneurship":
        bba_score += 1
    else:
        bcom_score += 1

    # Question 20
    q20 = st.radio("20. What kind of job would make you happy?",
        ["Creative and people-driven", "Structured and number-focused"])
    if q20 == "Creative and people-driven":
        bba_score += 1
    else:
        bcom_score += 1

    st.markdown("---")
    if st.button("🎯 See My Result"):
        st.session_state.bba_score = bba_score
        st.session_state.bcom_score = bcom_score
        st.session_state.show_goals = False
        st.session_state.show_result = True
        # === FINAL RESULT SECTION ===
if st.session_state.get("show_result", False):
    st.markdown("## 🎓 Your Career Test Result")
    st.write(f"Hello **{st.session_state.user_name}**, based on your answers, here’s what we suggest:")

    # Get final scores
    bba_score = st.session_state.bba_score
    bcom_score = st.session_state.bcom_score

    # Calculate percentages
    total = bba_score + bcom_score
    bba_percent = round((bba_score / total) * 100, 1)
    bcom_percent = round((bcom_score / total) * 100, 1)

    # Show score bars
    st.markdown(f"**BBA Suitability:** {bba_percent}%")
    st.progress(bba_percent / 100)

    st.markdown(f"**B.Com Suitability:** {bcom_percent}%")
    st.progress(bcom_percent / 100)

    st.markdown("---")

    # Suggestion logic
    if bba_percent > bcom_percent:
        st.success("✅ You are better aligned with **BBA** – your personality and interests suggest you're a natural manager, communicator, or entrepreneur.")
    elif bcom_percent > bba_percent:
        st.success("✅ You are better aligned with **B.Com** – your strengths show a deep interest in finance, accuracy, and structured systems.")
    else:
        st.info("🤝 You seem balanced between **BBA and B.Com**. You can explore both fields based on future goals or higher studies preference.")

    st.markdown("**Thanks for taking the test!** You’ll get more clarity as you grow — but you’ve already taken the right first step 🎯")
    # Save final recommendation for report download
if bba_percent > bcom_percent:
    final_recommendation = "You are better aligned with BBA – great for careers in business, communication, and leadership."
elif bcom_percent > bba_percent:
    final_recommendation = "You are better aligned with B.Com – great for finance, accounting, and structured career paths."
else:
    final_recommendation = "You’re balanced between BBA and B.Com – either can work based on future goals."

# Save in session for PDF/download
st.session_state.final_report = final_recommendation

# Call to Action (CTA)
st.markdown("### 💬 Want Personalised Guidance?")
if st.button("📞 Book a Free Career Call with Practical EduSkills"):
    st.success("✅ Our counselor will contact you soon. You can also WhatsApp us at +91-XXXXXXXXXX.")

st.markdown("---")
st.caption("🔒 Your data is private and only used to guide your career.")





























