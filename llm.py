from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load pre-trained Mistral model tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen2.5-7B-Instruct-1M')
model = AutoModelForCausalLM.from_pretrained('Qwen/Qwen2.5-7B-Instruct-1M', force_download=True)


# Define a function to generate text
def generate_text(prompt):
    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors='pt')
    
    # Generate text
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100)
    
    # Convert generated IDs back to text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return generated_text

# Example usage
prompt = "Tell me a story about a character who learns a new skill."
generated_text = generate_text(prompt)
print(f"Generated text: {generated_text}")
