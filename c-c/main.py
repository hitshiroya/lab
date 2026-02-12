from client.llm_client import LLMClient
import asyncio

async def main():
    client = LLMClient()
    messages = [
        {
            "role" : "user",
            "content" : "what is namespace in openshift?"
        }
    ]
    async for event in client.chat_completion(messages,True):
        print(event)



asyncio.run(main())


