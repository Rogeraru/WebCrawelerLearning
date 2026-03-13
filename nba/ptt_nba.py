import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ptt.cc/bbs/NBA/index.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'}
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser') #response.content vs .text
articles = soup.find_all("div", class_="r-ent")
data_list = []

def crawl_nba_info_to_excel():
    for a in articles:
        data = {}
        title = a.find("div", class_="title")
        if title and title.a:
            title = title.a.text
        else:
            title = "None"
        data["標題"] = title

        popular = a.find("div", class_="nrec")
        if popular and popular.span:
            popular = popular.span.text
        else:
            popular = "N/A"
        data["人氣"] = popular

        date = a.find("div", class_="date")
        if date:
            date = date.text
        else:
            date = "N/A"
        data["日期"] = date
        data_list.append(data)
    # with open("ptt_nba_data.json", "w", encoding="utf-8") as f:
    #     json.dump(data_list, f, ensure_ascii=False, indent=4)
    df = pd.DataFrame(data_list)
    df.to_excel("ptt_nba.xlsx", index=False, engine = "openpyxl")
    print("nba info file success")
        #print(data_list)
        #print(f"title : {title}. date : {date}. popularity : {popular}")



    # if response.status_code == 200:
    #     with open('output.html','w', encoding='utf-8') as f:
    #         f.write(response.text)
    #     print("crawel success")
    # else:
    #     print("crawel fail")