import os

from groq import Groq
from openai import OpenAI

from .models import LLM, SystemPrompt, UserPrompt


def get_response(
    llm: LLM, system_prompt: SystemPrompt, user_prompt: UserPrompt, random_seed: int
) -> str:
    model = llm.model_name_version
    if llm.provider_name == "OpenAI":
        client = OpenAI()
    elif llm.provider_name == "Nvidia":
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.environ["NVIDIA_API_KEY"],
        )
    elif llm.provider_name == "Groq":
        client = Groq()
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt.prompt},
            {"role": "user", "content": user_prompt.prompt},
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
        seed=random_seed,
    )

    return completion.choices[0].message.content
