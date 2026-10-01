import ollama
model_name = "qwen3:4b"
question = "What does a SOC analyst do in Cyber security?"

response = ollama.chat(model=model_name, messages=[{"role": "user", "content": question}])
print("Question:", question)
print("Response:", response)