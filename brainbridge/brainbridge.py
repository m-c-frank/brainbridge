import os
import json
import argparse
import openai
import sys

# Ensure the OPENAI_API_KEY environment variable is set
API_KEY = os.environ["OPENAI_API_KEY"]
openai.api_key = API_KEY

def get_response(conversation):
    """Send the conversation to OpenAI and get a response."""
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
    return response.choices[0].message["content"]

def main():
    parser = argparse.ArgumentParser(description="Get a response from the OpenAI neural API.")
    # Assume --conversation is provided and it is valid JSON
    parser.add_argument("--conversation", required=True, help="JSON string representing the conversation list")
    args = parser.parse_args()

    # Directly load the JSON from the argument
    print(args.conversation)
    conversation = json.loads(args.conversation)

    # Get the response from the API
    response_content = get_response(conversation)

    # Output the response content
    print(json.dumps({"role": "assistant", "content": response_content}))

if __name__ == "__main__":
    main()
