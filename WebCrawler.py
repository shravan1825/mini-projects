import requests
import bs4

url=input=("enter url")
respose=requests.get(url)
print(type(respose))
print(response.text)
