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

# Initial messages
conversation_messages=[
    {
        "role": "system",
        "content": "You are a helpful AI assistant that answers questions and provides information."
    }]

# Loop until the user wants to quit
print("Assistant: Enter a prompt (or type 'quit' to exit)")
while True:
    input_text = input('\nYou: ')
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    
    conversation_messages.append({"role": "user",
        "content": input_text})

    response = openai_client.chat.completions.create(
                model=model_name,
                messages=conversation_messages
    )

    assistant_text = response.choices[0].message.content
    conversation_messages.append({"role": "Assistant",
        "content": assistant_text})
    print("\nAssistant:", assistant_text)
    

    