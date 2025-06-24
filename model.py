from transformers import BertTokenizer, BertForSequenceClassification
import torch

MODEL_NAME = 'bert-base-uncased'

tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
model = BertForSequenceClassification.from_pretrained(MODEL_NAME)

def predict_news(text):
    if "conspiracy" in text.lower():
        return "Fake"
    else:
        return "Real"
    