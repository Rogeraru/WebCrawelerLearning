import requests
from bs4 import BeautifulSoup
import os

def download_img(url, save_path):
    print(f"downloading {url}")
    response = requests.get(url)
    print("status:", response.status_code)
    print("type", response.headers.get("Content-Type"))
    with open(save_path, "wb") as f:
        f.write(response.content)
    print("-"*30)

def run():
    url = "https://www.ptt.cc/bbs/Beauty/M.1686997472.A.FDA.html"
    headers = {"Cookie": "over18=1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36", "Referer": "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FBeauty%2FM.1686997472.A.FDA.html"}
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")

    spans = soup.find_all("span", class_="article-meta-value")
    title = spans[2].text
    dir_name = f"imgs/{title}"

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    links = soup.find_all("a")
    allow_file_name = ["jpg", "png", "jpeg", "gif"]

    for link in links:
        href = link["href"]
        if not href:
            continue
        file_name = href.split("/")[-1]
        extension = href.split(".")[-1].lower()
        if extension in allow_file_name:
            print(f"file type:{extension}")
            print(f"url: {href}")
            download_img(href, f"{dir_name}/{file_name}")
        # print(href)
