from typing import Any
from openai import AsyncOpenAI


class RequestAPI:
    def __init__(self, client: AsyncOpenAI, model: str = "gpt-4o-mini"):
        self.client = client
        self.model = model

    async def get_request(self, request: Any, data: str = ""):
        system_msg = await request.comb(context=data)
        response = await self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[system_msg, {"role": "user", "content": data}],
            response_format=request.structure,
        )
        return response.choices[0].message.parsed
