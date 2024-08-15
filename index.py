import streamlit as st
import google.generativeai as genai

# Configure Google Generative AI
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Set up the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Set page configuration
st.set_page_config(page_title="Gemini Chatbot", page_icon=":robot_face:")

# Main title
st.title("Gemini Chatbot :robot_face:")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Generate response
    response = model.generate_content(user_input)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response.text)

# Sidebar with additional information
st.sidebar.title("About")
st.sidebar.info("This is a chatbot powered by Google's Gemini Pro model and built with Streamlit.")
st.sidebar.title("Instructions")
st.sidebar.write("1. Type your message in the input box at the bottom of the chat.")
st.sidebar.write("2. Press Enter or click the send button to submit your message.")
st.sidebar.write("3. The chatbot will generate a response based on your input.")
st.sidebar.write("4. Continue the conversation as long as you like!")