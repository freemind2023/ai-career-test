import streamlit as st

# Set title & favicon on browser tab
st.set_page_config(
    page_title="BBA vs BCom Career Test",
    page_icon="🎓",  # This is the small icon on browser tab
    layout="centered"
)

# Show your logo (we'll replace this link with your real logo later)
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/FreeMind_logo.svg/2560px-FreeMind_logo.svg.png", width=150)

# Main title
st.title("BBA vs BCom Career Test")

# Subheading
st.markdown("Welcome to **Free Mind Career Guidance Platform** 👋")
st.write("Let's begin by knowing who you are.")

# Separator
st.markdown("---")

# Form for student details
with st.form(key='student_info'):
    name = st.text_input("Full Name")
    phone = st.text_input("Mobile Number")
    city = st.text_input("Your City or Location")
    
    # Submit button
    start_button = st.form_submit_button(label="🚀 Start Test")

# When button is clicked
if start_button:
    if name and phone and city:
        st.success(f"Hi {name}, you’re ready to begin your test!")
        # This is where we will show the test in Day 3
    else:
        st.warning("Please fill in all fields before continuing.")
