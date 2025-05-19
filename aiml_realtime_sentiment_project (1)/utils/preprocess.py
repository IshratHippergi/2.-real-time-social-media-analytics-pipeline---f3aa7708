# Simple text preprocessor
def preprocess_text(text):
    import re
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.strip()
