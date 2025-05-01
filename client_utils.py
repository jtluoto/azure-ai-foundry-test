from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
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
