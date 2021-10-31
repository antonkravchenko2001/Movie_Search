import torch
from transformers import BertTokenizer, BertModel


class BertEncoder(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.tokenizer =  BertTokenizer.from_pretrained('google/bert_uncased_L-6_H-512_A-8')
        self.bert = BertModel.from_pretrained('google/bert_uncased_L-6_H-512_A-8')
 

    def forward(self, text_inputs):
        inputs = self.tokenizer(text_inputs,
                                return_tensors="pt",
                                padding=True,
                                truncation=True,
                                max_length=256)
        input_mask_expanded = inputs['attention_mask'].unsqueeze(-1)
        out = (
            torch.mean(self.bert(**inputs)['last_hidden_state'] * input_mask_expanded, 1)
            / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
        )
        return out