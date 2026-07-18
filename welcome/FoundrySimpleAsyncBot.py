from azure.ai.projects.aio import AIProjectClient
from azure.identity.aio import DefaultAzureCredential
import os
import asyncio


model_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]

project_endpoint = "https://ashishjha-resource-aifn-resource.services.ai.azure.com/api/projects/ashishjha-resource-aifndr-welcome"
#project_endpoint = "https://{resource-name}.services.ai.azure.com/api/projects/<project-name>"


async def main():
    async with (
        DefaultAzureCredential() as credential,
        AIProjectClient(
            endpoint=project_endpoint,
            credential=credential
        ) as project_client,
    ):
        # This returns an AsyncOpenAI client, already authenticated
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
            response1 = await openai_client.responses.create(
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
            response2 = await openai_client.responses.create(
                model=model_name,
                input=conversation_history,
                stream=True
            )

            async for event in response2:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="", flush=True)
                elif event.type == "response.completed":
                    response_id = event.response.id

        except Exception as ex:
            print(f"Error: {ex}")


asyncio.run(main())
