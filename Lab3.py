import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup1 = BeautifulSoup(page.content, 'html.parser')


#print (page)
#print("----------------------")
#print(soup1.prettify())

with open("../WK02_Javascript/lab2_official.html") as fp:
  soup = BeautifulSoup(fp, 'html.parser')
#print(soup.prettify())

#print("----------------------")
#print(soup.tr)
rows = soup.findAll("tr")

for row in rows:
  #print(row)
  #print("- - - - - - - - - - - -")
  dataList = []
  cols = row.findAll("td")
  for col in cols:
    dataList.append(col.text)
  print(dataList)



## PY04-testCSV.py
import csv

employee_file = open('employee_file.csv', mode='w') 
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

employee_writer.writerow(['John Smith', 'Accounting', 'November'])
employee_writer.writerow(['Erica Meyers, what', 'IT', 'March'])

employee_file.close()



## py05-readFileFinal
with open("../WK02_Javascript/lab2_official.html") as fp2:
    soup3 = BeautifulSoup(fp2,'html.parser')


employee_file = open('week02data.csv', mode='w') 
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

rows = soup3.findAll("tr")
for row in rows:
    
    cols = row.findAll("td")
    dataList = []
    for col in cols:
        dataList.append(col.text)
    employee_writer.writerow(dataList)
employee_file.close()


## py06-myhome

url2 = "https://www.myhome.ie/residential/leitrim/property-for-sale?page=1"
page2 = requests.get(url2)

soup4 = BeautifulSoup(page2.content, 'html.parser')

home_file = open('week03MyHome.csv', mode='w') 
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup4.findAll("div", class_="PropertyListingCard" )

for listing in listings:
    entryList = []
    
    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)

    home_writer.writerow(entryList)
home_file.close()