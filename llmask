#! /Users/majid/miniconda3/envs/llm/bin/python

import os
import argparse

from groq import Groq
from openai import OpenAI


system_prompts = {
    "bash": "You're an assistant who provides bash script commands for Linux and MacOS. Output the command as per user's request with no additional explanations. Don't format in markdown.",
    "define": "You're an assistant who helps to define and explain words/terms/persons to the user like a dictionary or wikipedia. It's important to keep it short and brief.",
    "vim": "You're an assistant who helps with vim/neovim commands. User may ask about a shortcut or command in vim/neovim to do a particular thing.",
    "stat": "You're an assistant who help user with statistics and machine learning questions. User is a data scientist with a B.Sc. degree in Statistics familiar with deep learning and data engineering stuff.",
}


parser = argparse.ArgumentParser(
    description="Get bash script commands for Linux and MacOS"
)
parser.add_argument("prompt", help="The user prompt for the assistant")
parser.add_argument(
    "--seed", type=int, help="The random seed for the model", default=42
)
parser.add_argument(
    "--provider", default="openai", choices={"openai", "nvidia", "groq"}
)
parser.add_argument("--mode", default="bash", choices={"bash", "define", "vim", "stat"})
args = parser.parse_args()

system_prompt = system_prompts[args.mode]
user_prompt = args.prompt

model: str = ''

if args.provider == "openai":
    client = OpenAI()
    model = "gpt-4o"
elif args.provider == "nvidia":
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=os.environ["NVIDIA_API_KEY"],
    )
    model = "meta/llama-3.1-405b-instruct"
    # model = "meta/llama-3.1-70b-instruct"
elif args.provider == "groq":
    client = Groq()
    model = "llama-3.1-70b-versatile"
completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
    seed=args.seed,
)

print(completion.choices[0].message.content)
