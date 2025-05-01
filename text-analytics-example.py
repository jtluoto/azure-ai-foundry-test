from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.projects.models import ConnectionType
import client_utils

try:
    # Get the project client using the utility module
    project_client = client_utils.get_project_client()

    # Get the properties of the default Azure AI Services connection with credentials
    connection = project_client.connections.get_default(
        connection_type=ConnectionType.AZURE_AI_SERVICES,
        include_credentials=True, 
    )
    
    # Create credential object. connection.key is the Azure AI Services API key
    ai_svc_credential = AzureKeyCredential(connection.key)
 
    # Use the connection information to create a text analytics client
    text_analytics_client = TextAnalyticsClient(endpoint=connection.endpoint_url, credential=ai_svc_credential)


    # Use the Language service to analyze some text (to infer sentiment) 
    text = "I hated the movie. It was so slow!"
    sentimentAnalysis = text_analytics_client.analyze_sentiment(documents=[text])[0]
    print("Text: {}\nSentiment: {}".format(text,sentimentAnalysis.sentiment))

except Exception as ex:
    print(ex)