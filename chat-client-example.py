from azure.ai.inference.models import SystemMessage, UserMessage
import client_utils

try:
    # Get the project client using the utility module
    project_client = client_utils.get_project_client()

    # Get a chat client
    chat = project_client.inference.get_chat_completions_client()

    # Get a chat completion based on a user-provided prompt
    user_prompt = input("Enter a question:")

    response = chat.complete(
        model="phi-4-mini-reasoning",
        messages=[
                   SystemMessage("You are a helpful AI assistant that answers questions."),
                   UserMessage(user_prompt)
        ],
    )
    print(response.choices[0].message.content)

except Exception as ex:
    print(ex)