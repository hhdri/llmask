import argparse
import requests


def create_interaction(api_url, llm, system_prompt, user_prompt, random_seed):
    data = {
        "llm": llm,
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "random_seed": random_seed,
    }

    response = requests.post(api_url, data=data)

    if response.status_code == 201:
        print("Interaction created successfully!")
        print("Response data:", response.json())
    elif response.status_code == 200:
        print("Interaction already exists.")
        print("Response data:", response.json())
    else:
        print(f"Failed to create interaction. Status code: {response.status_code}")
        print("Error:", response.json())


def main():
    parser = argparse.ArgumentParser(
        description="Create an interaction in the Django API."
    )

    parser.add_argument(
        "--api_url",
        help="The API endpoint URL to send the POST request to.",
        default="http://localhost:8000/create_interaction/",
    )
    parser.add_argument(
        "--llm", help="The slug of the LLM.", default="gpt-4o-mini-2024-07-18"
    )
    parser.add_argument(
        "--random_seed", type=int, help="The random seed as an integer.", default=42
    )
    parser.add_argument("system_prompt", help="The name of the System Prompt.")
    parser.add_argument("user_prompt", help="The text of the User Prompt.")

    args = parser.parse_args()

    create_interaction(
        args.api_url, args.llm, args.system_prompt, args.user_prompt, args.random_seed
    )


if __name__ == "__main__":
    main()

# example usage:
# python cli.py bash "How do I list files in a directory?"
