import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.imdb.com/find?s=ep&q=Thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content, 'html.parser')
soup.prettify()
movieTable = soup.find('table', {'class': 'findList'})
print(movieTable.prettify())
rows = movieTable.findAll('tr')
for row in rows:
    rowData = row.findAll('td')
    print(rowData[1].find('a').text)
