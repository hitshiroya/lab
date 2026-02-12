from groq import AsyncGroq
from typing import Any , AsyncGenerator
from dotenv import load_dotenv
import os 

load_dotenv()


from client.response import StreamEvent
from client.response import TextDelta
from client.response import TokenUsage
from client.response import EventType


api_key = os.getenv("LLM_API_KEY")
model_name = os.getenv("MODEL_NAME")

class LLMClient:
    def __init__(self) -> None:
       self._client : AsyncGroq | None = None

    

    def get_client(self) -> AsyncGroq:
        if self._client is None:
            self._client = AsyncGroq(
                api_key=api_key,
            )
        return self._client
    
    

    async def close(self) -> None:
        if self._client:
            await self._client.close()
            self._client = None 
    
    async def chat_completion(self,messages: list[dict[str,Any]],stream:bool = True) -> AsyncGenerator[StreamEvent,None]:
        client = self.get_client()

        kwargs = {
             "model": model_name,
             "messages" : messages,
             "stream" : stream
        }

        if stream:
            async for event in self._stream_response(client,kwargs):
                yield event

        else:
            event = await self._non_stream_response(client,kwargs)
            yield event

    
    async def _stream_response(self, client : AsyncGroq , kwargs : dict[str,Any]) -> AsyncGenerator[StreamEvent, None]:
        response = await client.chat.completions.create(**kwargs)

        finish_reason : str | None = None
        usage : TokenUsage | None = None
        
        async for chunk in response:
            if hasattr(chunk,"usage") and chunk.usage:
                usage = TokenUsage(
                    prompt_tokens = chunk.usage.prompt_tokens,
                    completion_tokens = chunk.usage.completion_tokens,
                    total_tokens = chunk.usage.total_tokens,
                )
            
            if not chunk.choices:
                continue

            choice = chunk.choices[0]
            delta = choice.delta

            if choice.finish_reason:
                finish_reason = choice.finish_reason
            
            if delta.content:
                yield StreamEvent (
                    type = EventType.TEXT_DELTA,
                    text_delta = TextDelta(delta.content)
                )

        yield StreamEvent(
            type = EventType.MESSAGE_COMPLETE,
            finish_reason = finish_reason,
            usage = usage

        )






        
    async def _non_stream_response(self, client : AsyncGroq , kwargs : dict[str,Any]) -> StreamEvent:
        response = await client.chat.completions.create(**kwargs)
        choice = response.choices[0]
        message = choice.message
        
        text_delta = None
        if message.content:
            text_delta = TextDelta(content = message.content)

        usage = None
        if response.usage:
            usage = TokenUsage(
                prompt_tokens = response.usage.prompt_tokens,
                completion_tokens = response.usage.completion_tokens,
                total_tokens = response.usage.total_tokens,
            )
        
        return StreamEvent(
            type = EventType.MESSAGE_COMPLETE,
            text_delta  = text_delta,
            finish_reason = choice.finish_reason,
            usage = usage
        )
