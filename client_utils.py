from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ConnectionType
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

def load_environment():
    """Load environment variables from .env file"""
    load_dotenv()

def get_project_client():
    """
    Initialize and return an AIProjectClient using the connection string from environment variables.
    
    Returns:
        AIProjectClient: Initialized project client
        
    Raises:
        ValueError: If the AZURE_PROJECT_CONNECTION_STRING environment variable is not set
    """
    # Load environment variables if not already loaded
    load_environment()
    
    # Get project client
    project_connection_string = os.environ.get("AZURE_PROJECT_CONNECTION_STRING")
    if not project_connection_string:
        raise ValueError("Environment variable AZURE_PROJECT_CONNECTION_STRING is not set")    
    
    return AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(),
        conn_str=project_connection_string,
    )

def get_ai_services_connection(project_client=None):
    """
    Get the default Azure AI Services connection with credentials.
    
    Args:
        project_client (AIProjectClient, optional): An existing project client.
            If not provided, a new one will be created.
            
    Returns:
        tuple: (connection, AzureKeyCredential) - The connection object and a credential object
    """
    if project_client is None:
        project_client = get_project_client()
        
    # Get the properties of the default Azure AI Services connection with credentials
    connection = project_client.connections.get_default(
        connection_type=ConnectionType.AZURE_AI_SERVICES,
        include_credentials=True, 
    )
    
    # Create credential object 
    # connection.key is the Azure AI Services API key
    ai_svc_credential = AzureKeyCredential(connection.key)
    
    return connection, ai_svc_credential