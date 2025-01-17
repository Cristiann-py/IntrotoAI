# pip install openai
from openai import OpenAI

client = OpenAI(api_key="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")

# Set your OpenAI API key
  # Replace with your key or set it in the environment

def chatbot():
    conversation = []  # To store the chat history

    print("Welcome to the argumentative chatbot!")
    print("Type 'exit' to quit the chat.")

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() == 'exit':
            print("Goodbye!")
            break

        # Add user's message to the conversation
        conversation.append({"role": "user", "content": user_message})

        # Prepare the system prompt and the full conversation
        system_data = [
            {
                "role": "system",
                "content": (
                    "You are an argumentative chatbot who is very sassy and talks back to the user on whatever "
                    f"their opinion is. Clown on the user's choice and be mean. Argue and never back down. "
                )
            }
        ] + conversation

        try:
            # Get a response from OpenAI
            response = client.chat.completions.create(model="gpt-4o-mini",
                                                          messages=system_data)

            chatbot_reply = response.choices[0].message.content

            # Add chatbot's reply to the conversation
            conversation.append({"role": "assistant", "content": chatbot_reply})

            # Print the chatbot's reply
            print(f"Chatbot: {chatbot_reply}")

        except Exception as e:
            print(f"Error: {str(e)}")
            break

if __name__ == "__main__":
    chatbot()