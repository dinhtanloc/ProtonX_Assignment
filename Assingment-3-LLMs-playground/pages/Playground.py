import streamlit as st
import requests
import uuid
import json

st.set_page_config(layout="wide")

# Set up the Streamlit interface
st.title("Assignment 3 - Build LLMs Playground")
st.markdown("""
    Assignment 3 - ProtonX AI for devs
""")

st.session_state.flask_api_url = "https://1111-34-125-0-7.ngrok-free.app/chat"  # Set your Flask API URL here

# Generate a random session ID
session_id = str(uuid.uuid4())

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display the chat history using chat UI
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input(key="chat", placeholder="What is up?"):
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the payload for the request
    payload = {
        "message": {"content": prompt},
        "context": st.session_state.chat_history,
        "sessionId": session_id,
        "model": st.session_state.selected_model,
        "temperature": st.session_state.temperature,
        "top_p": st.session_state.top_p,
        "stream": True 
    }

    # Stream the response from the Flask API
    with st.chat_message("assistant"):
        streamed_content = ""  # Initialize an empty string to concatenate chunks
        response = requests.post(st.session_state.flask_api_url, json=payload, stream=True)

        # Create a placeholder to update the markdown
        response_placeholder = st.empty()

        if response.status_code == 200:
            # TODO 4
            # Loop through each chunk and add the content to the variable streamed_content
            # Don't forget to use markdown to print the result
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    chunk_data = chunk.decode("utf-8")
                    try:
                        streamed_json = json.loads(chunk_data)
                        chunk_content = streamed_json.get('content', '')
                    except json.JSONDecodeError:
                        chunk_content = chunk_data  

                    streamed_content += chunk_content
                    response_placeholder.markdown(streamed_content)  
            # Once complete, add the full response to the chat history
            st.session_state.chat_history.append({"role": "assistant", "content": streamed_content})
        else:
            st.error(f"Error: {response.status_code}")

# Sidebar settings for model, temperature, and top_p
with st.sidebar:
    # TODO 1: Create a selectbox with options "gpt-4o" and "gpt-4"
    st.session_state.selected_model = st.selectbox(
        "Select Model:",
        options=["gpt-4o", "gpt-4"],
        index=0  
    )
    st.write("You selected:", st.session_state.selected_model)

    # TODO 2: Create a slider ranging from 0.0 to 1.0 with a step of 0.1
    st.session_state.temperature = st.slider(
        "Temperature:",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.temperature,
        step=0.1
    )
    st.write("Current Temperature:", st.session_state.temperature)

    # TODO 3: Create a slider ranging from 0.0 to 1.0 with a step of 0.1
    st.session_state.top_p = st.slider(
        "Top P:",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.top_p,
        step=0.1
    )
    st.write("Current Top P:", st.session_state.top_p)

    st.image("https://storage.googleapis.com/mle-courses-prod/users/61b6fa1ba83a7e37c8309756/private-files/678dadd0-603b-11ef-b0a7-998b84b38d43-ProtonX_logo_horizontally__1_.png", width=100)
