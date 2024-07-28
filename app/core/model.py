import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class TroyModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("lonlo/model_troy")
        self.model = AutoModelForCausalLM.from_pretrained("lonlo/model_troy")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate_response(self, input_text: str, max_length: int = 100) -> str:
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt").to(
            self.device
        )
        attention_mask = torch.ones(input_ids.shape, device=self.device)

        output = self.model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7,
        )

        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response.strip()


troy_model = TroyModel()
