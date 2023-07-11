import re

import requests
from bs4 import BeautifulSoup


# request web page
resp = requests.get("https://pypistats.org/packages/djangorestframework")

# get the response text. in this case it is HTML
html = resp.text

# parse the HTML
soup = BeautifulSoup(html, "html.parser")

# filter all rows with Downloads word
downloads = soup(text=re.compile('Downloads last'))

# extract row text and value
for row in downloads:
    text, value = row.replace("\n", "").split(":") 
    print({text: value})


# print(soup.body.get_text().strip())
# print(soup.prettify)