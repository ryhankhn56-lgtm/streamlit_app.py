import streamlit as st
import random

st.set_page_config(page_title="Python Jokes Bot", page_icon="🐍")

st.title("🐍 Python Jokes Chatbot")
st.caption("Ask me for Python jokes 😄")

# Python jokes database
python_jokes = [
    "Why do Python programmers wear glasses? Because they can’t C 👓",
    "Why was the Python developer unhappy? Because he didn’t get arrays 😆",
    "Why did the Python programmer quit his job? Because he didn’t get tuples 😄",
    "I told my Python code a joke… but it didn’t laugh, it just returned None 🤣",
    "Why is Python so friendly? Because it has a lot of 'import' friends 🐍",
    "Why do Python programmers prefer dark mode? Because light attracts bugs 🐛",
    "Python developers don’t argue — they just raise exceptions 😜"
]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Say something like: tell me a python joke")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot logic
    if "joke" in user_input.lower():
        bot_reply = random.choice(python_jokes)
    else:
        bot_reply = "😄 Ask me for a *Python joke* by typing **tell me a python joke**"

    # Display bot message
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # Save bot message
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
