import requests
from bs4 import BeautifulSoup
import time
import nltk
nltk.data.path.append('/home/philip-kasumbi/nltk_data')

from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

url = "https://www.standardmedia.co.ke/category/3/politics"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

cards = soup.find_all("div", class_="card-body")

for card in cards:
    links = card.find("a")
    if links:
        title = links.get_text(strip=True)
        href = links.get("href")

        try:
            article = Article(href)
            article.download()
            article.parse()

            parser = PlaintextParser.from_string(article.text, Tokenizer("english"))
            summarizer = LexRankSummarizer()
            summary = summarizer(parser.document, 3)

            print("\n🔍 SUMMARY:\n")
            print("Title:", article.title, "\n")
            for sentence in summary:
                print("-", str(sentence))
            print("-" * 60)

          
            with open("politics_articles_summary.txt", mode="a", encoding="utf-8") as txt_file:
                txt_file.write(f"\n📌 Title: {article.title}\n")
                txt_file.write(f"🔗 URL: {href}\n\n")
                txt_file.write("📝 Summary:\n")
                for sentence in summary:
                    txt_file.write(f"- {sentence}\n")
                txt_file.write("=" * 80 + "\n\n")

            time.sleep(1)

        except Exception as e:
            print(f"An error occurred: {e}")
