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
    subURL = rowData[1].a['href']
    subData = requests.get("https://www.imdb.com" + subURL)
    childSoup = BeautifulSoup(subData.content, 'html.parser')
    if childSoup.find('div',{'class':'see-more inline canwrap'}):
       genre= childSoup.find('div',{'class':'see-more inline canwrap'})
       if genre.a.text==" Documentry":
           print(rowData[1].a.text)
