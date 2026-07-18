from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential 
import os
deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]


project_endpoint="https://ashishjha-resource-aifn-resource.services.ai.azure.com/api/projects/ashishjha-resource-aifndr-welcome"
#project_endpoint = "https://{resource-name}.services.ai.azure.com/api/projects/<project-name>"


project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)

openai_client = project_client.get_openai_client()

response = openai_client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(f"answer: {response.choices[0].message.content}")