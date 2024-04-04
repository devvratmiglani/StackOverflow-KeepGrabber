from bs4 import BeautifulSoup
import requests
import time
import re

intro = r'''       ....                        _            _                                       s    
   .xH888888Hx.                   u            u                                       :8    
 .H8888888888888:                88Nu.   u.   88Nu.   u.     .u    .                  .88    
 888*"""?""*88888X        .u    '88888.o888c '88888.o888c  .d88B :@8c        u       :888ooo 
'f     d8x.   ^%88k    ud8888.   ^8888  8888  ^8888  8888 ="8888f8888r    us888u.  -*8888888 
'>    <88888X   '?8  :888'8888.   8888  8888   8888  8888   4888>'88"  .@88 "8888"   8888    
 `:..:`888888>    8> d888 '88%"   8888  8888   8888  8888   4888> '    9888  9888    8888    
        `"*88     X  8888.+"      8888  8888   8888  8888   4888>      9888  9888    8888    
   .xHHhx.."      !  8888L       .8888b.888P  .8888b.888P  .d888L .+   9888  9888   .8888Lu= 
  X88888888hx. ..!   '8888c. .+   ^Y8888*""    ^Y8888*""   ^"8888*"    9888  9888   ^%888*   
 !   "*888888888"     "88888%       `Y"          `Y"          "Y"      "888*""888"    'Y"    
        ^"***"`         "YP'                                            ^Y"   ^Y'            
                                                                                             
                                                                                             
                                                                                             '''
headline ="----------------------------------StackOverflow-KeepGrabber----------------------------------"

print(intro)
print("")
print(headline)

j=0
URL = "https://stackoverflow.com/questions?tab=active&page="
csv_headers = "title,markdown,tag1,tag2,tag3,tag4,count_answers"
stack_grab_csv = open("StackGrabTemp.csv","a",encoding='utf-8')
print(csv_headers,file=stack_grab_csv)
for i in range(1,1000):
    r = requests.get(URL+str(i),headers={"Host": "stackoverflow.com",
                                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:122.0) Gecko/20100101 Firefox/122.0",
                                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                                  "Accept-Language": "en-US,en;q=0.5",
                                  "Accept-Encoding": "gzip, deflate, br",
                                  "DNT": "1",
                                  "Sec-GPC": "1",
                                  "Connection": "keep-alive",
                                  "Referer": "https://stackoverflow.com/questions?tab=active&page=2",
                                  "Upgrade-Insecure-Requests": "1",
                                  "Sec-Fetch-Dest": "document",
                                  "Sec-Fetch-Mode": "navigate",
                                  "Sec-Fetch-Site": "same-origin",
                                  "Sec-Fetch-User": "?1",
                                  "TE": "trailers"
                                  })
    
    soup = BeautifulSoup(r.text,"html.parser")
    questions = soup.find('div',{'id':'questions'}).findAll("div",{"class":"s-post-summary"})


    for q in questions:
        question_text = ""
        question_markdown = ""
        tag1 = ""
        tag2 = ""
        tag3 = ""
        tag4 = ""
        count_answer = "0"

        question_text = re.sub(" +"," ",q.find('a',{"class":"s-link"}).text) # question text
        question_text = re.sub("\n+"," ",question_text)
        question_text = re.sub(" +"," ",question_text)

        question_markdown = re.sub(" +"," ",q.find('div',{"class":"s-post-summary--content-excerpt"}).text) # question markdown
        question_markdown = re.sub("\n+"," ",question_markdown)
        question_markdown = re.sub(" +"," ",question_markdown)

        pt = q.findAll('a',{"class":"post-tag"}) # post tags

        try:
            tag1 = pt[0].text
        except:
            tag1 = "NaN"

        try:
            tag2 = pt[1].text
        except:
            tag2 = "NaN"

        try:
            tag3 = pt[2].text
        except:
            tag3 = "NaN"

        try:
            tag4 = pt[3].text
        except:
            tag4 = "NaN"

        stat =  q.findAll('span',{'class':'s-post-summary--stats-item-number'})

        count_asnwer = stat[1].text # count_answers
        print("\""+question_text+"\""+","+"\""+question_markdown+"\""+","+tag1+","+tag2+","+tag3+","+tag4+","+count_asnwer,file=stack_grab_csv)
        j=j+1
        print("Grabbing rows:",j,'\r',end='')
    time.sleep(2)
                                                                                             