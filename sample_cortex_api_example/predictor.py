import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


class PythonPredictor:
    def __init__(self, config):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2").to(self.device)

    def predict(self, payload):
        input_length = len(payload["text"].split())
        tokens = self.tokenizer.encode(payload["text"], return_tensors="pt").to(self.device)
        prediction = self.model.generate(tokens, max_length=input_length + 20, do_sample=True)
        return self.tokenizer.decode(prediction[0])
