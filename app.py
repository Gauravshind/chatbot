import streamlit as st

# Define a basic chatbot response function
def chatbot_response(user_input):
    # For demonstration, a simple keyword-based response
    responses = {
        "hello": "Hi gaurav how are you!",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!",
    }
    return responses.get(user_input.lower(), "Sorry, I didn't understand that.")

# Streamlit app
def main():
    st.title("Simple Chatbot")
    st.write("Talk to our chatbot!")

    # Create a text input box for user to type their message
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if user_input:
            response = chatbot_response(user_input)
            st.write(f"**Bot:** {response}")
        else:
            st.write("Please type a message!")

if __name__ == "__main__":
    main()
