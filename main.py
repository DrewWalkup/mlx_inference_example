#########################
# Llama 3 MLX Example   #
# Rundown Ventures Inc  #
# May 2024              #
#########################


from mlx_lm import load, generate

# Llama-3 chat template
llama3_template = """{% set loop_messages = messages %}{% for message in loop_messages %}{% set content = '<|start_header_id|>' + message['role'] + '<|end_header_id|>\n\n'+ message['content'] | trim + '<|eot_id|>' %}{% if loop.index0 == 0 %}{% set content = bos_token + content %}{% endif %}{{ content }}{% endfor %}{{ '<|start_header_id|>assistant<|end_header_id|>\n\n' }}"""

# Load the model and tokenizer
model, tokenizer = load(
    "../llm_models/MLX/Meta-Llama-3-8B-Instruct-Rundown-8Bit",
    tokenizer_config={
        "bos_token": "<|begin_of_text|>",
        "eos_token": "<|eot_id|>",
        "chat_template": llama3_template,
    },
)

# Baisc role and dialogue example -- I like concise responses!
dialog = [
    {
        "role": "system",
        "content": "You are a helpful and concise assistant named David.",
    },
    {"role": "user", "content": "What is the capital of Croatia?"},
    {"role": "assistant", "content": "The capital city of Croatia is Zagreb."},
]


# Inference loop
def chat_inference(model, tokenizer):
    # Check if the tokenizer has a method to apply the chat template
    if (
        hasattr(tokenizer, "apply_chat_template")
        and tokenizer.chat_template is not None
    ):
        use_chat_template = True
    else:
        use_chat_template = False
        print("No chat template available, proceeding without it.")

    while True:
        user_prompt = input("\nUser: ")

        if user_prompt == "exit":
            break

        if use_chat_template:
            # Apply the chat template and ppend user input to the dialog
            dialog.append({"role": "user", "content": user_prompt})
            user_prompt = tokenizer.apply_chat_template(
                dialog, tokenize=False, add_generation_prompt=True
            )

        response = generate(
            model,
            tokenizer,
            temp=0.8,
            max_tokens=256,
            prompt=user_prompt,
            verbose=False,
        )

        print("\nDavid:", response)

        # Append model response to the dialog
        dialog.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    chat_inference(model, tokenizer)
