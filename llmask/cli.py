import os
import argparse
from functools import partial

from groq import Groq
from openai import OpenAI


# MAX_TOKENS = 1024
# TEMPERATURE = 1
# TOP_P = 1


class NvidiaLLM:
    @staticmethod
    def get_response(
        model_name: str,
        system_prompt: str,
        user_prompt: str,
        random_seed: int,
        max_tokens,
        temperature,
        top_p,
    ):
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.environ["NVIDIA_API_KEY"],
        )
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            seed=random_seed,
        )

        return completion.choices[0].message.content


class GroqLLM:
    @staticmethod
    def get_response(
        model_name: str,
        system_prompt: str,
        user_prompt: str,
        random_seed: int,
        max_tokens,
        temperature,
        top_p,
    ):
        client = Groq()
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            stream=True,
            stop=None,
            seed=random_seed,
        )

        return completion.choices[0].message.content


class OpenAILLM:
    @staticmethod
    def get_response(
        model_name: str,
        system_prompt: str,
        user_prompt: str,
        random_seed: int,
        max_tokens,
        temperature,
        top_p,
    ):
        client = OpenAI()
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            seed=random_seed,
            frequency_penalty=0,
            presence_penalty=0,
        )

        return completion.choices[0].message.content


model_slugs = {
    "gpt-4o-mini-v1": partial(
        OpenAILLM.get_response, model_name="gpt-4o-mini-2024-07-18"
    ),
    "gpt-4o-v1": partial(OpenAILLM.get_response, model_name="gpt-4o-2024-08-06"),
    "groq-llama-3.1-70b": partial(
        GroqLLM.get_response, model_name="llama-3.1-70b-versatile"
    ),
    "groq-llama-3.1-8b": partial(
        GroqLLM.get_response, model_name="llama-3.1-8b-instant"
    ),
    "nvidia-llama-3.1-8b": partial(
        NvidiaLLM.get_response, model_name="meta/llama-3.1-8b-instruct"
    ),
    "nvidia-llama-3.1-70b": partial(
        NvidiaLLM.get_response, model_name="meta/llama-3.1-70b-instruct"
    ),
    "nvidia-llama-3.1-405b": partial(
        NvidiaLLM.get_response, model_name="meta/llama-3.1-405b-instruct"
    ),
}

system_prompts = {
    "bash-v1": "You're an assistant who provides bash script commands for Linux and MacOS. Output the command as per user's request with no additional explanations. Don't format in markdown.",
    "define-v1": "You're an assistant who helps to define and explain words/terms/persons to the user like a dictionary or wikipedia. It's important to keep it short and brief.",
    "vim-v1": "You're an assistant who helps with vim/neovim commands. User may ask about a shortcut or command in vim/neovim to do a particular thing.",
    "stat-v1": "You're an assistant who help user with statistics and machine learning questions.",
}


def cli_entrypoint(system_prompt, description):
    parser = argparse.ArgumentParser(
        description=description,
    )

    parser.add_argument(
        "--llm",
        default="gpt-4o-mini-v1",
        choices=model_slugs.keys(),
    )
    parser.add_argument("--random_seed", type=int, default=42)
    parser.add_argument("--max_tokens", type=int, default=1024)
    parser.add_argument("--temperature", type=float, default=1)
    parser.add_argument("--top_p", type=float, default=1)
    parser.add_argument("user_prompt")

    args = parser.parse_args()

    response = model_slugs[args.llm](
        system_prompt=system_prompt,
        user_prompt=args.user_prompt,
        random_seed=args.random_seed,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
        top_p=args.top_p,
    )

    print(response)


def cli_bash():
    cli_entrypoint(system_prompts["bash-v1"], "Bash Assistant")


def cli_define():
    cli_entrypoint(system_prompts["define-v1"], "Define Assistant")


def cli_vim():
    cli_entrypoint(system_prompts["vim-v1"], "Vim Assistant")


def cli_stat():
    cli_entrypoint(system_prompts["stat-v1"], "Stat Assistant")
