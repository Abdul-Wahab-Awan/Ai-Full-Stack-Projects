import requests
from bs4 import BeautifulSoup
import csv

URL='https://www.amazon.com/b?_encoding=UTF8&node=21217035011&ref_=cct_cg_SHnav2_2a1&pf_rd_p=12b44fc7-b592-4f55-b8d7-32c20b211ef1&pf_rd_r=9Z4KFSRNJF7N2MG3RRFC'

r=requests.get(URL)

soup=BeautifulSoup(r.content,'html5lib')
itemD=[]
itemD={}
itemD['item']=
item=soup.find('div',attrs={'id':'acsProductBlockV1-0'})

filename='items.csv'
with open(filename,'w', newline='')as f:
    w=csv.DictWriter(f,[item])
    w.writeheader()