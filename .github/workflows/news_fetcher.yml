import requests
import os
from datetime import datetime

# GitHub Secrets에서 API 키를 안전하게 가져옵니다.
API_KEY = os.environ.get("NEWS_API_KEY")

# 검색할 키워드 목록
KEYWORDS = ["미국", "부동산", "비트코인"]

# 결과를 저장할 파일 이름
OUTPUT_FILE = "news_list.txt"

def fetch_top_news():
    # 오늘 날짜 (UTC 기준)를 YYYY-MM-DD 형식으로 가져옵니다.
    today_utc = datetime.utcnow().strftime('%Y-%m-%d')

    all_news = []
    for keyword in KEYWORDS:
        print(f"Fetching news for '{keyword}' published on {today_utc}...")
        # NewsAPI에 요청을 보낼 때, from과 to 파라미터로 날짜를 '오늘'로 고정합니다.
        url = (f"https://newsapi.org/v2/everything?"
               f"q={keyword}&"
               f"from={today_utc}&"
               f"to={today_utc}&"
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
                print(f"  -> No articles found for today.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news for {keyword}: {e}")

    # 파일에 결과를 저장합니다.
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"뉴스 업데이트 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("\n".join(all_news))

    print(f"Successfully wrote top news to {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_top_news()
