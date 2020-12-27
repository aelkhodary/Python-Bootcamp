'''
web scraping
>> pip install requests
>> pip install lxml
>> pip install bs4
'''

import requests
import bs4

result = requests.get("http://www.example.com")
type(result)
#requests.models.Response
#print(result.text)
soup = bs4.BeautifulSoup(result.text,"lxml")
print(soup)
print(type(soup.select("title")[0]))
print(soup.select("title")[0].getText())
