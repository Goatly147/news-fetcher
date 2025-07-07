import requests
import os
from datetime import datetime, timedelta

# GitHub Secrets에서 API 키를 안전하게 가져옵니다.
API_KEY = os.environ.get("NEWS_API_KEY")

# 검색할 키워드 목록
KEYWORDS = ["미국", "부동산", "비트코인"]

# 결과를 저장할 파일 이름
OUTPUT_FILE = "news_list.txt"

def fetch_top_news():
    # 검색 시작 날짜를 24시간 전으로 설정하여 더 넓은 범위의 뉴스를 포함합니다.
    start_date = (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%d')

    all_news = []
    for keyword in KEYWORDS:
        print(f"Fetching news for '{keyword}' from {start_date}...")
        # NewsAPI에 요청을 보낼 때, from 파라미터로 검색 시작 날짜를 지정합니다.
        url = (f"https://newsapi.org/v2/everything?"
               f"q={keyword}&"
               f"from={start_date}&"
               f"language=ko&"
               f"sortBy=popularity&"
               f"apiKey={API_KEY}")

        try:
            response = requests.get(url)
            response.raise_for_status()  # 오류가 있으면 예외 발생
            articles = response.json().get("articles", [])

            if articles:
                top_article = articles[0]  # 가장 인기 있는 첫 번째 기사
                all_news.append(f"주제: {keyword}")
                all_news.append(f"제목: {top_article['title']}")
                all_news.append(f"URL: {top_article['url']}\n")
                print(f"  -> Found: {top_article['title']}")
            else:
                print(f"  -> No articles found in the last 24 hours.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news for {keyword}: {e}")

    # 파일에 결과를 저장합니다.
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"뉴스 업데이트 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("\n".join(all_news))

    print(f"Successfully wrote top news to {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_top_news()
