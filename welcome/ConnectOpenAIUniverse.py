from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import os
deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]

endpoint = "https://ashishjha-resource-aifn-resource.services.ai.azure.com/openai/v1"

token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

response = client.responses.create(
    model=deployment_name,
    input="What is the capital of France?",
)

print(f"answer: {response.output_text}")
