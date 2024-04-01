import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Define responses for the chatbot
patterns = [
    r"hi",
    r"how are you",
    r"bye",
    r"Tell me a joke",
    r"what is streamlit", # make sure you put the comma
    r"About Your Buisness"  # Assuming this is a pattern for asking about the business
]

responses = [
    ["Hello!"],
    ["I'm good, thank you."],
    ["Goodbye!"],
    ["Why don't skeletons fight each other? They don't have the guts!"],
    ["Streamlit is a Python library that allows you to quickly create web applications using simple Python scripts. It's designed to make the process of building interactive web apps as easy as writing Python code. With Streamlit, you can create data-driven apps, visualizations, dashboards, and more, all with minimal effort and without needing to know web development languages like HTML, CSS, or JavaScript."],
    ["We help in Analytic problem"]  # Adjusted response
    
]

# Combine patterns and responses using zip
pairs = list(zip(patterns, responses))

# Create a chatbot using NLTK
chatbot = Chat(pairs, reflections)
chat_history = []

# Streamlit UI
st.image("https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.nigeriajob.com%2Fsites%2Fnigeriajob.com%2Ffiles%2Fstyles%2Fmedium%2Fpublic%2Flogo%2Fearly_code.png%3Fitok%3DEidefLyy&tbnid=bppcsTeywKXEPM&vet=12ahUKEwj-_birkaGFAxXIybsIHZL5DpkQMygBegQIARBQ..i&imgrefurl=https%3A%2F%2Fwww.nigeriajob.com%2Frecruiter%2F88818&docid=YsZ4_Ddj5fHJqM&w=220&h=220&q=download%20earlycode%20image&ved=2ahUKEwj-_birkaGFAxXIybsIHZL5DpkQMygBegQIARBQ", width=100) 
st.title("EARLYCODE CHAT-BOT")

# Allow users to set up profiles
user_name = st.text_input("Enter your name:")
avatar = st.file_uploader("Upload your avatar:")

user_input = st.text_input("You:")
if st.button("Send"):
    response = chatbot.respond(user_input)
    chat_history.append({"user": user_name, "message": user_input})
    chat_history.append({"user": "ChatBot", "message": response})

# Display chat messages with custom styling
for chat in chat_history:
    if chat["user"] == user_name:
        st.markdown(f"**{chat['user']}**: {chat['message']}", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='color: white'><b>{chat['user']}</b>: {chat['message']}</div>", unsafe_allow_html=True)
