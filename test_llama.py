import ollama

response = ollama.chat(
    model="qwen3:4b",  # replace with a name from `ollama list`
    messages=[{"role": "user", "content": "In one sentence, what is a forward deployed engineer?"}],
)
print(response["message"]["content"])