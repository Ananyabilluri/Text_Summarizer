# Summarizes text using extractive summarization with sentence scoring

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import heapq

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = """The rapid advancement of artificial intelligence is transforming industries worldwide. 
AI technologies enable automation of repetitive tasks, improving efficiency in manufacturing. 
However, concerns about job displacement due to automation are growing. 
Researchers are exploring ways to integrate AI with human skills to create a balanced workforce. 
Ethical considerations in AI development remain a key focus for future innovations."""

# Preprocess and summarize
def summarize_text(text, n_sentences=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and word.isalnum()]
    freq_dist = FreqDist(words)
    sentence_scores = {}
    for sentence in sentences:
        for word, freq in freq_dist.items():
            if word in sentence.lower():
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = 0
                sentence_scores[sentence] += freq
    summary_sentences = heapq.nlargest(n_sentences, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)

# Generate summary
summary = summarize_text(text)
print(f"Summary: {summary}")