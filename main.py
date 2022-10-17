import requests
import lxml
from bs4 import BeautifulSoup
import os
import json
import re

def get_url(url):
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.3.886 Yowser/2.5 Safari/537.36"
    }
    req = requests.get(url=url, headers=headers )
    with open("all_posts.html", "w", encoding="utf8") as file:
        file.write(req.text)

    with open("all_posts.html", encoding="utf8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    posts = soup.find_all(class_="feed__item l-island-round")

    post_urls = []
    for post in posts:
        post_url = post.find("div", class_="content-title content-title--short l-island-a").find("a", class_="content-header__item content-header-number").get("href")
        # print(post_url)
        post_urls.append(post_url)

    for post_url in post_urls:
        req = requests.get(post_url, headers)
        post_name = post_url.split("/")[-1]

        with open(f'data/{post_name}.html', 'w', encoding='utf8') as file:
            file.write(req.text)

        with open(f'data/{post_name}.html', encoding='utf8') as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")



get_url("https://vc.ru/")