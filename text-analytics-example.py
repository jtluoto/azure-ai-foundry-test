from azure.ai.textanalytics import TextAnalyticsClient
import client_utils

try:
    # Get the AI services connection using the utility module
    connection, ai_svc_credential = client_utils.get_ai_services_connection()

    # Use the connection information to create a text analytics client
    text_analytics_client = TextAnalyticsClient(endpoint=connection.endpoint_url, credential=ai_svc_credential)

    # Use the Language service to analyze some text (to infer sentiment) 
    text = "I hated the movie. It was so slow!"
    sentimentAnalysis = text_analytics_client.analyze_sentiment(documents=[text])[0]
    print("Text: {}\nSentiment: {}".format(text,sentimentAnalysis.sentiment))

except Exception as ex:
    print(ex)