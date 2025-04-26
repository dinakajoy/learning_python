from textblob import TextBlob


class SentimentAnalyzer:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def analyze_with_textblob(text):
        blob = TextBlob(text)
        return blob.sentiment.polarity

    def analyze_sentiment(self):
        polarity = self.analyze_with_textblob(self.text)
        if polarity > 0:
            return f"Sentiment Score: {polarity} (Positive)"
        elif polarity < 0:
            return f"Sentiment Score: {polarity} (Negative)"
        else:
            return f"Sentiment Score: {polarity} (Neutral)"


text = input("Enter text: ")
sentimentAnalyzer = SentimentAnalyzer(text)
print(sentimentAnalyzer.analyze_sentiment())
