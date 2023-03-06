import requests
from bs4 import BeautifulSoup

def amazon_scrape(stri):
  url = 'https://www.amazon.in/s?k=' + '+'.join(stri.split())
  print(url)
  
  headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
  }
  

  page = requests.get(url,headers=headers)

  soup1 = BeautifulSoup(page.text, 'html.parser')

  p = soup1.find_all("div",{"data-component-type":"s-search-result"})

  d = []

  for i in range (3,min(len(p),20)):
    if p[i].find('span',class_="a-size-medium a-color-base a-text-normal") != None:
      name = p[i].find('span',class_="a-size-medium a-color-base a-text-normal").text
      if(p[i].find('span',class_="a-offscreen") != None):
        price = p[i].find('span',class_="a-offscreen").text
      image = p[i].find("img", attrs={"data-image-source-density":"1"})['src']
      
    elif p[i].find('span',class_="a-size-base-plus a-color-base") != None:
      a = p[i].find('span',class_="a-size-base-plus a-color-base").text
      b = p[i].find('span',class_="a-size-base-plus a-color-base a-text-normal").text
      name = a+" "+b
      price = p[i].find('span',class_="a-price-whole").text
      image = p[i].find("img", attrs={"class":"s-image"})['src']
      
    elif p[i].find('span',class_="a-size-base-plus a-color-base a-text-normal") != None:
      name = p[i].find('span',class_="a-size-base-plus a-color-base a-text-normal").text
      if (p[i].find('span',class_="a-price-whole") != None):
        price = p[i].find('span',class_="a-price-whole").text
      image = p[i].find("img", attrs={"class":"s-image"})['src']
    
    d.append(
      {
        'price': price,
        'name': name,
        'image': image
      }
    )
    
  return d

def flipkart(stri):
  return

def snapdeal(stri):
  return

# can add more depending on the time constraint