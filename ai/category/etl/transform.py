import torch

def run(model,
        tokenizer,prompt):
    # Transform input tokens 
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512)
    # Model apply
    
    with torch.no_grad():
        outputs = model(**inputs)

    predicted_label_index = torch.argmax(outputs.logits, dim=1).item()
    predicted_label = model.config.id2label[predicted_label_index]

    return predicted_label