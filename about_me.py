import streamlit as st
from contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HEADER SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("nmh.png", width=230)

with col2:
    st.title("Rehan Khan", anchor=False)
    st.write(
        "Junior Web Developer, assisting in building responsive and user-friendly websites."
    )

    if st.button("💌 Contact Me"):
        show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.subheader("Experience & Qualifications", anchor=False)
st.write("""
- 7 Years experience extracting actionable insights from data
- Strong hands-on experience and knowledge in Python and Excel
- Good understanding of statistical principles and their respective applications
- Excellent team-player and displaying a strong sense of initiative on tasks
""")

# --- SKILLS ---
st.subheader("Hard Skills", anchor=False)
st.write("""
- Programming: Python (Scikit-learn, Pandas), SQL, VBA
- Data Visualization: PowerBI, MS Excel, Plotly
- Modeling: Logistic regression, linear regression, decision trees
- Databases: Postgres, MongoDB, MySQL
""")

