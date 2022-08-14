from django.shortcuts import render
from bs4 import BeautifulSoup as bsp
import requests
import sys
import time
# Create your views here.
URL=''
try:
    response=requests.get(URL)
except Exception as e:
    error_type, error_valude, error_traceback=sys.exc_info()
    print('URL',URL)
    print(error_type,'error line',error_traceback.tb_lineno)
names=[]
prices=[]
images=[]
markets=[]
class ScrappedData:
    time.sleep(4)
    soup=bsp(response.text,'html.parser') 
    def product_name(self):
        for i in self.soup.find_all('div',attrs={'class':'_2B099V'}):
            name=i.find('a',attrs={'class':'IRpwTa'})
            names.append(name.text.strip())
        return names
    def product_price(self):
        for i in self.soup.find_all('div',attrs={'class':''}):
            price=i.find('a',attrs={'class':''})
            prices.append(price.text.strip())
        return prices
    def produc_ima(self):
        for i in self.soup.find_all(''):
            image=i.find('a')
            images.append(image.text.strip())
        return images
            