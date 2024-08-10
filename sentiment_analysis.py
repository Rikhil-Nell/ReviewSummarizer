from transformers import pipeline


class SentimentAnalyzer:
    classifier = pipeline("sentiment-analysis")

    res = classifier("Things are looking good")

    print(res)

    def sentiment_analysis(self, text):
        return self.classifier(text)
