# basic crawler/scraper

from lxml import etree
import requests

url = "https://www.1news.co.nz/"
response = requests.get(url)

if response.status_code == 200:
    dom = etree.HTML(response.text)
    news = []

    # target divs
    divs = dom.xpath(
        "//div[contains(@class, 'hidden') "
        "and contains(@class, 'md:flex') "
        "and contains(@class, 'lg:hidden') "
        "and contains(@class, 'flex-col') "
        "and contains(@class, 'gap-4')]"
    )

    for div in divs:
        # find any subStory h3s inside the divs
        elements = div.xpath(".//h3[contains(@class,'subStory')]")
        for elem in elements:
            if elem.text:
                news.append(elem.text.strip())

    if news:
        for n in news:
            print(f"\n\n{n}")
    else:
        print("No subStory elements found.")
else:
    print("Failed to fetch page.")
