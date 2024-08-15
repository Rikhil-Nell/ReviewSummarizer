from transformers import pipeline

print("initialized")
# Use a model specifically fine-tuned for zero-shot classification
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli', device=0)

print("model loaded")

res = classifier(
    "I am kinda sad today",
    candidate_labels=["happy", "sad"],
)

print(res)
