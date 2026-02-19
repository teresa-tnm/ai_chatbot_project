import streamlit as st
from chatbot import get_ai_response

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("AI Chatbot")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm your AI assistant. How can I help you today?"
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    with st.chat_message("user"):
        st.write(user_input)
    
    with st.spinner("Thinking..."):
        api_messages = [
            {"role": "system", "content": "You are a helpful, friendly, and intelligent AI assistant."}
        ]
        
        for msg in st.session_state.messages:
            if msg["role"] in ["user", "assistant"]:
                api_messages.append(msg)
        
        response = get_ai_response(api_messages)
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
    
    with st.chat_message("assistant"):
        st.write(response)

st.sidebar.title("Settings")
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm your AI assistant. How can I help you today?"
        }
    ]
    st.rerun()
