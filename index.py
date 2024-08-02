# import streamlit as st
# from dotenv import load_dotenv
# import os
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Gemini API
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Initialize Gemini model
# model = genai.GenerativeModel("gemini-1.0-pro")
# chat = model.start_chat(history=[])

# def get_gemini_response(question):
#     response = chat.send_message(question, stream=True)
#     return response

# # Streamlit app
# st.set_page_config(page_title="Gemini Chatbot", layout="wide")
# st.header("Gemini Chatbot")

# # Initialize session state for chat history
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# # Chat input
# input = st.text_input("You:", key="input")
# if st.button("Send"):
#     if input:
#         # Get response from Gemini
#         response = get_gemini_response(input)
        
#         # Add user input to chat history
#         st.session_state['chat_history'].append({"role": "user", "content": input})
        
#         # Add Gemini response to chat history
#         full_response = ""
#         for chunk in response:
#             full_response += chunk.text
#         st.session_state['chat_history'].append({"role": "assistant", "content": full_response})

# # Display chat history
# for message in st.session_state['chat_history']:
#     if message["role"] == "user":
#         st.text_area("You:", value=message["content"], height=50, max_chars=None, key=f"user_{len(st.session_state['chat_history'])}")
#     else:
#         st.text_area("Gemini:", value=message["content"], height=100, max_chars=None, key=f"assistant_{len(st.session_state['chat_history'])}")

# # Clear chat history button
# if st.button("Clear Chat"):
#     st.session_state['chat_history'] = []
#     st.experimental_rerun()
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model
# model = genai.GenerativeModel('gemini-1.0-pro')
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
