import streamlit as st
import re
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjcwNTZkMDYzZTA0MzU1MjZiNTUzMzUxMzIi_pc"

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None


def contact_form():
    # Session state to control form visibility
    if "show_form" not in st.session_state:
        st.session_state.show_form = False

    st.title("📩 Contact Us")

    if st.button("Open Contact Form"):
        st.session_state.show_form = True

    if st.session_state.show_form:
        with st.form("contact_form"):
            name = st.text_input("First Name")
            email = st.text_input("Email Address")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Submit")

        if submitted:
            if not name:
                st.error("Please provide your name.")
            elif not email:
                st.error("Please provide your email address.")
            elif not is_valid_email(email):
                st.error("Please provide a valid email address.")
            elif not message:
                st.error("Please provide a message.")
            else:
                payload = {
                    "name": name,
                    "email": email,
                    "message": message
                }

                try:
                    response = requests.post(WEBHOOK_URL, data=payload, timeout=10)

                    if response.status_code == 200:
                        st.success("Message sent successfully! 🎉")
                        st.session_state.show_form = False
                    else:
                        st.error("Webhook failed")

                except requests.exceptions.RequestException as e:
                    st.error(e)



