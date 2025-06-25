from transformers import BertTokenizer, BertForSequenceClassification
import torch

MODEL_NAME = 'bert-base-uncased'

tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
model = BertForSequenceClassification.from_pretrained(MODEL_NAME)

model.eval()

def predict_news(text):
    inputs = tokenizer(text, return_tensors = 'pt', truncation = True, padding = True, max_length = 512)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits, dim = 1).item()

    if predicted_class_id == 0:
        return "This sounds kinda sus, fam.", "Fake"
    else:
        return "This is giving... factual.", "Real"