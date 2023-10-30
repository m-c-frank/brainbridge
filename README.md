# BrainBridge: A Neural API CLI 🧠🌉

BrainBridge seamlessly connects you to advanced neural models directly from your command line. It's designed for single and multi-turn interactions, saving conversations as you go, allowing you to maintain the context of your chats.

## Directory Structure
```
brainbridge/
│
├── brainbridge/
│   ├── __init__.py
│   └── brainbridge.py
│
├── setup.py
└── README.md
```

## Features
1. **Command Line Interface**: Directly interact with the neural models from your terminal.
2. **Maintain Conversations**: Hold multi-turn interactions, capturing and extending from previous messages.
3. **Easy Integration**: Perfect for integrating with other tools and scripts. Easily capture outputs using standard command-line operations.

## Installation

To install BrainBridge, clone the repo and use `pip`:

```bash
git clone https://github.com/m-c-frank/brainbridge
cd brainbridge
pip install .
```

## Usage

### First Interaction

```bash
brainbridge "Who won the world series in 2020?" > conversation.json
```

This saves the entire conversation, including the system message, into `conversation.json`.

### Subsequent Interactions

Use the saved `conversation.json` for context in your following questions:

```bash
brainbridge "Where was it played?" --conversation "$(cat conversation.json)" > conversation.json
```

This appends the latest interaction to `conversation.json`, ensuring you maintain the context of your conversations.

## Configuration

Before you begin, make sure you've set up the API in your environment variable

Or just replace `'YOUR_API_KEY'` with your actual API key.

## Contributions & Feedback

We welcome contributions and feedback on how to improve BrainBridge. Please open an issue or submit a PR on our [GitHub repository](#).

## Licence

Check out the GOS licence in this project.
