from selenium import webdriver
from bs4 import BeautifulSoup
import requests as rq
import pandas as pd
from time import sleep
import re

# ----Blank Lists-----#
rating = []
review = []
comment = []
link = []

# ------ Getting info from landing page-------#
url = input('Enter URL:  ')
# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.get(url)
r1 = rq.get(url)
soup1 = BeautifulSoup(r1.text, 'html.parser')
driver.execute_script('window.scroll(0,2500)')
sleep(2)
for t in soup1.findAll('a', attrs={'href': re.compile("/product-reviews/")}):
    q = t.get('href')
    link.append(q)
# print(link)

for iu in link:
    if 'LSTSTFG7G8YN2JFY5ZFJJJWIB' in iu:
        # print(i)
        aa = iu
f_url = ('https://www.flipkart.com'+str(iu))

# # ----- Iterating through each page ----------
i = 1
while i <= 20:
    ss = driver.get(str(f_url)+"&page="+str(i))
    qq = driver.current_url
    r2 = rq.get(qq)
    soup = BeautifulSoup(r2.text, 'html.parser')
    for ra in soup.find_all('div', {'class': '_3LWZlK _1BLPMq'}):
        aa = ra.get_text()
        rating.append(aa)
    # for re in soup.find_all('p', {'class': '_2-N8zT'}):
    #     bb = re.get_text()
    #     review.append(bb)
    for co in soup.find_all('div', {'class': 't-ZTKy'}):
        cc = co.get_text()
        review.append(cc)
    sleep(1)
    i += 1

df = pd.DataFrame([rating, review, comment]).transpose()
df.to_excel(
    'F:/University/11-Semester/Research_paper/Code/File/FK_Review.xlsx')
