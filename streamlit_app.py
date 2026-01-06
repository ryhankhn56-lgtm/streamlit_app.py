import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    page="about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True
)
project_1_page = st.Page(
    page="sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:"
)
project_2_page = st.Page(
    page="chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:"
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page]
    }
)

# --- SHARED ON ALL PAGES ---
st.sidebar.image("logo2.png", width=85)
st.sidebar.text("Made by Rehan 😍")



# --- RUN NAVIGATION ---
pg.run()