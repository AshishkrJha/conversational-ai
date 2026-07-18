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

# Track responses
last_response_id = None

# Loop until the user wants to quit
print("Assistant: Enter a prompt (or type 'quit' to exit)")
while True:
    input_text = input('\nYou: ')
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    # Get a response
    extra_args = {}
    if last_response_id is not None:
        extra_args["previous_response_id"] = last_response_id

    response = openai_client.responses.create(
                model=model_name,
                instructions="You are a helpful AI assistant that explains technology concepts clearly.",
                input=input_text,
                **extra_args
    )
    assistant_text = response.output_text
    print("\nAssistant:", assistant_text)
    last_response_id = response.id

    