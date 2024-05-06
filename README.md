# Llama 3 MLX Example

This codebase is designed to demonstrate the use of the Meta-Llama-3-8B-Instruct model with a focus on generating concise and contextually appropriate responses in a chatbot setting.

## Overview

This example utilizes the Llama 3 model from the MLX series to create a chatbot named David, which can answer questions and interact with users in a concise manner. The model and tokenizer are configured to handle a chat template that structures the conversation flow.

## Basics

- **Model Loading**: Load the Llama 3 model with specific tokenizer configurations.
- **Chat Template**: Utilize a custom chat template to structure messages and roles within the conversation.
- **Interactive Chat**: Run an interactive chat session where the model responds to user inputs.

## Requirements

To run this example, you will need Python 3.8 or later. Dependencies include:
- `mlx_lm` package (a fictional library for the sake of this example)

## Installation

1. Clone this repository
2. Install the required Python packages:
`pip install -r requirements.txt`

## Usage

To start the chatbot, run the `main.py` script:
`python main.py`

Interact with the chatbot by typing your questions or statements. Type `exit` to end the chat session.

## Configuration

The model and tokenizer are configured in `main.py`. You can adjust the `tokenizer_config` dictionary to change the behavior of the tokenizer, such as modifying the beginning-of-sentence or end-of-text tokens.

## License

This project is licensed under the MIT License.