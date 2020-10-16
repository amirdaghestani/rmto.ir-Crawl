from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import io

base_url = 'http://www.rmto.ir/lists/list31/allitems.aspx#InplviewHash1b59108f-35d0-4156-ac7f-a34a7318327d=Paged%3DTRUE-'
r = requests.get(base_url)

soup = BeautifulSoup(r.text, "html.parser")

page_count_links = soup.find_all("a", href = re.compile(r".*javascript:goToPage.*"))

num_pages = 151

url_list = ["{}p_ID%3D{}".format(base_url, str(page)) for page in range (12332, 12392, 30)]
#16862
#print(str(url_list))

with io.open('company.csv', 'w', encoding = 'utf-8-sig') as company:
    for url_ in url_list:
        print("processing {}...".format(url_))
        r_new = requests.get(url_)
        soup_new = BeautifulSoup(r_new.text, "html.parser")
        for tr in soup_new.find_all('tr'):
            stack = []
            for td in tr.find_all('td'):
                stack.append(td.text.replace('\n', '').replace('\t', '').strip())
            company.write(", ".join(stack) + '\n')