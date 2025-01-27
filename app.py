import streamlit as st
import ollama

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant. Always explain your reasoning step-by-step before providing the final answer."}
    ]

# Streamlit app title
st.title("Local ChatGPT")

# Display chat history
for message in st.session_state.messages:
    if message["role"] != "system":  # Don't display system messages
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()  # Placeholder for the response
        full_response = ""

        # Stream the response token-by-token
        for chunk in ollama.generate(model="llama2", prompt=prompt, stream=True):
            token = chunk['response']
            full_response += token
            response_placeholder.markdown(full_response + "▌")  # Add a cursor effect

        # Finalize the response
        response_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})