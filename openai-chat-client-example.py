from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
import client_utils
import openai
import os

try:
    client_utils.load_environment()

    api_version = os.environ.get("OPEN_AI_CLIENT_API_VERSION")
    model_name = os.environ.get("OPEN_AI_MODEL_NAME")

    # Get the project client using the utility module
    project_client = client_utils.get_project_client()

    ## Get an Azure OpenAI chat client
    openai_client = project_client.inference.get_azure_openai_client(api_version=api_version)

    # Get a chat completion based on a user-provided prompt
    user_prompt = input("Enter a question:")
    response = openai_client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant that answers questions."},
            {"role": "user", "content": user_prompt},
        ]
    )
    print(response.choices[0].message.content)

except Exception as ex:
    print(ex)