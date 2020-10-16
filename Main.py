import urllib
import urllib.request
from bs4 import BeautifulSoup
import io
#import os
import csv

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, "html.parser")
    return soupdata

contents = []

with open('urllist.csv', 'r') as csvf:
    reader = csv.reader(csvf)
    for row in reader:
        contents.append(row)

companydatasaved=""

for i in range(0, 3):
    url = str(contents[i][0])
    soup = make_soup(url)
    for record in soup.findAll('tr'):
        companydata = ""
        for data in record.findAll('td'):
            companydata = companydata + "," + data.text
        #if len(companydata) != 0:
        companydatasaved = companydatasaved + "\n" + companydata

#print(companydatasaved)
with io.open('company.csv', 'w', encoding = 'utf-8-sig') as company:
    company.write(companydatasaved)
#file = open(os.path.expanduser("company.csv"),"wb")
#file.write(bytes(companydatasaved, encoding="ascii", errors='ignore'))