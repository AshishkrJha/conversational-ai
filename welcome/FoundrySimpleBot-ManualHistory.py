from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential 
import os
model_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]

project_endpoint="https://ashishjha-resource-aifn-resource.services.ai.azure.com/api/projects/ashishjha-resource-aifndr-welcome"
#project_endpoint = "https://{resource-name}.services.ai.azure.com/api/projects/<project-name>"


project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)

openai_client = project_client.get_openai_client()

try:
    # Start with initial message
    conversation_history = [
        {
            "type": "message",
            "role": "user",
            "content": "What is machine learning?"
        }
    ]

    # First response
    response1 = openai_client.responses.create(
        model=model_name,
        input=conversation_history
    )

    print("Assistant:", response1.output_text)

    # Add assistant response to history
    conversation_history += response1.output

    # Add new user message
    conversation_history.append({
        "type": "message",
        "role": "user", 
        "content": "Can you give me an example?"
    })

    # Second response with full history
    response2 = openai_client.responses.create(
        model=model_name,
        input=conversation_history
    )

    print("Assistant:", response2.output_text)

except Exception as ex:
    print(f"Error: {ex}")