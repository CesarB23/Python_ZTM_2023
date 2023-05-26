from bs4 import BeautifulSoup
import requests

#Requests allow us to get the info via http
res = requests.get('https://news.ycombinator.com/news')
#BS allow to manipulate the info that we get from the request to the server
# print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
# print(soup.body)
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.title)
# print(soup.find(id='score_20514755'))
# print(soup.select('.score'))
# print(soup.select('#score_36038868'))
print(soup.select('.titleline')[0])
# print(soup.select('.score'))