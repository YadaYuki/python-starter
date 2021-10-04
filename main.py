from typing import List

import requests
from bs4 import BeautifulSoup


# htmlのテキストデータのみを抽出する。
def parse_html(content: str) -> List[str]:
    soup = BeautifulSoup(content, "lxml")
    text_list: List[str] = []
    div_item_list = soup.find_all("div")
    for div_item in div_item_list:
        text_list.append(div_item.get_text())
    return text_list


if __name__ == "__main__":
    html_doc = requests.get(
        "https://brightech.com/products/ambience-solar-1w?variant=8038410879012"
    ).text
    # print(parse_html(html_doc))
    print(parse_html("<div>hoge</div>"))
