# Text Summarizer
This repository contains a Python script for performing extractive text summarization using sentence scoring based on word frequency.

## Overview
The script tokenizes text into sentences, calculates word frequencies, scores sentences, and extracts the top-scoring sentences as a summary.

## Requirements
- Python 3.x
- nltk

## Installation
```bash
pip install nltk
python -m nltk.downloader punkt
python -m nltk.downloader stopwords
```

## Usage
Run the script to generate a text summary:
```bash
python text_summarizer.py
```

## Output
- Condensed summary of the input text

## Note
Replace the sample text with real documents for practical use.
