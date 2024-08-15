from typing import List
import argparse
import requests

api_endpoint = "http://localhost:8000/"


def create_interaction(llm, system_prompt, user_prompt, random_seed):
    data = {
        "llm": llm,
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "random_seed": random_seed,
    }

    response = requests.post(api_endpoint + "create_interaction/", data=data)

    if response.status_code == 201:
        print("Interaction created successfully!")
        print("Response data:\n", response.json()['response'], sep="")
    elif response.status_code == 200:
        print("Interaction already exists.")
        print("Response data:\n", response.json()['response'], sep="")
    else:
        print(f"Failed to create interaction. Status code: {response.status_code}")
        print("Error:", response.json())


def get_llms() -> List[str]:
    response = requests.get(api_endpoint + "get_llms/")
    return response.json()


def get_system_prompts() -> List[str]:
    response = requests.get(api_endpoint + "get_system_prompts/")
    return response.json()


def main():
    parser = argparse.ArgumentParser(
        description="Create an interaction in the Django API."
    )

    parser.add_argument(
        "--llm",
        default="gpt-4o-mini-2024-07-18",
        choices=get_llms(),
    )
    parser.add_argument("--random_seed", type=int, default=42)
    parser.add_argument(
        "system_prompt",
        choices=get_system_prompts(),
    )
    parser.add_argument("user_prompt")

    args = parser.parse_args()

    create_interaction(args.llm, args.system_prompt, args.user_prompt, args.random_seed)


if __name__ == "__main__":
    main()

# example usage:
# python cli.py bash "How do I list files in a directory?"
