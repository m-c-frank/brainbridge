import argparse
import os
import json
import sys
import neuralapi

# Set the API key directly or ensure it is set as an environment variable
API_KEY = os.environ["NEURALAPI_API_KEY"]
neuralapi.api_key = API_KEY

def get_response(conversation_json):
    response = neuralapi.ChatCompletion.create(model="gpt-3.5-turbo", messages=json.loads(conversation_json))
    return response.choices[0].message["content"]

def main():
    parser = argparse.ArgumentParser(description="Get a response from the OpenAI neural API.")
    parser.add_argument("--conversation", required=True, help="JSON string representing the conversation list")
    args = parser.parse_args()

    # Get the response from the API
    response_content = get_response(args.conversation)

    # Output the response content
    print(json.dumps([{"role": "assistant", "content": response_content}]))

if __name__ == "__main__":
    main()
