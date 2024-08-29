import streamlit as st
import google.generativeai as genai

# Configure the Google AI SDK
api_key = "AIzaSyAiisRzHkz3rAiyn0A_L5_2Ehwav7TNeX8"  # Replace with your actual API key
genai.configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Streamlit app layout
st.title("Poem Generator using LLM Model")

# Only the topic is required now
topic = st.text_input("Enter a topic for your poem:")

if st.button("Generate Poem"):
    if topic:
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        f"Write a poem about {topic}.",
                    ],
                },
            ]
        )
        response = chat_session.send_message("Generate the poem")

        st.subheader("Generated Poem:")
        st.write(response.text)
    else:
        st.error("Please enter a topic to generate a poem.")
