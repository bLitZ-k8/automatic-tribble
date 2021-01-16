#imports
import random
import requests
from bs4 import BeautifulSoup
from googlesearch import search

month_nums = {'january': [1, 'jan'], 'february': [2, 'feb'], 'march': [3,'mar'], 'april': [4, 'apr'], 'may':[5, 'may'], 'june': [6, 'jun'], 'july':[7, 'jul'], 'august':[8, 'aug'], 'september':[9, 'sep'], 'october':[10, 'oct'], 'november': [11, 'nov'], 'december':[12, 'dec'] }


flman_date = input().lower().split()     #the date, format is of type : sep 18
flmsites = ["http://www.myfloridamanstory.com/", "https://google.com/", "http://thefloridamantimes.com/"]

#generate random ints
#random.seed(3)
ran_in = random.randint(0, 100)
arr_idx = 0 #ran_in%(len(flmsites))

#web scraping
#case dependent variable assign
if(arr_idx==0):
    request_string = flmsites[0] + flman_date[0] + "/" + flman_date[1]
    #print(request_string)
    result = requests.get(request_string)
    target_id = "h2"
elif(arr_idx==1):
    request_string = flman_date.join()
    #search(query, tld="com", lang='en', num=10, start=0, stop='10', pause=30)
    for i in search(request_string, tld="co.in", num=10, stop=10, pause=2):
        print(i)
elif(arr_idx==2):
    request_string = flmsites[2] + "?s=" + flman_date[0] + '+' + flman_date[1]
    result = requests.get(request_string)
    target_id = "p"

#using bs4
src = result.content
soup = BeautifulSoup(src, 'lxml')
target_head = soup.find_all(target_id)

for heading in target_head:
    if "Florida Man" in heading.text:
        print('''{}
        source:{}'''.format(heading.text, flmsites[0]))

#result = requests.get(flmsites[arr_idx])

def flm_get():
    #code
    return 0