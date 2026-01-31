import requests
from BS4 import Beautifulsoup
web=requests.get("https://www.tutorialstreak.com")
print(web)
print(web.content)
print(web.url)
print(web.status_code)

x=Beautifulsoup(web.content,"html.parser")
print(x.prettify())
print(x.title)
print(x.p)
print(x.a)
print(x.h1)
print(x.select('.item.title'))
print(x.find_all('p'))
print(x.finf('p'))
class_data=x.find("button",class_ a"tf-button setup-btn exp-all-btn"
print(class_data)

id_data=x.find("title",id="c969eq-area")
print(id_data)
data=(x.find_all('p'))
for d in data:
    print(d.text)

z=x.find(name"p"class_a"fs-16 fs-400 tn-24 label-color-1 card-text")

print(z)

