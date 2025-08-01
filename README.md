# 📰 Kenya Politics News Scraper & Summarizer

This Python script automatically scrapes the latest political news articles from [Standard Media Kenya](https://www.standardmedia.co.ke/category/3/politics). It summarizes each article and saves the summary and full text into a `.txt` file.

---

## ✅ Features

- Scrapes all new articles from the Politics section
- Extracts the title, full article text, and a 3-sentence summary
- Saves all info to a single `.txt` file with timestamps
- Uses the `newspaper3k` and `sumy` libraries for article parsing and summarization

---

## 📂 Output

The script appends to a file called `politics_summaries.txt`, which includes:

- ⏰ Scrape time
- 📰 Article title
- 🔗 Article link
- 📌 Summary (3 bullet points)
- 📝 Full article text

---

## 🛠 Requirements

Install all dependencies with:

```bash
pip install requests beautifulsoup4 newspaper3k sumy


You must also install NLTK data (done automatically if nltk_data is downloaded manually):

import nltk
nltk.download('punkt')

Or place your NLTK data in the correct path:

nltk.data.path.append('/home/your-username/nltk_data')

