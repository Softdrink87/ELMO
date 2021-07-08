from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def parsing(count,number):
  result = []
  
  for i in range(1,count+1):
    targetUrl = urlopen("https://ko.wikipedia.org/wiki/%ED%8A%B9%EC%88%98:%EC%9E%84%EC%9D%98%EB%AC%B8%EC%84%9C") if number == 1 else urlopen("https://en.wikipedia.org/wiki/Special:Random")
    bsObje = BeautifulSoup(targetUrl, 'html.parser')
    target = bsObje.select('p')
    print(str(i) + "... loading")
    for i in range(len(target)-1):
      result.append(target[i].get_text())

  for i in range(len(result)-1):
    if '\n' in result[i]:
      result[i]=result[i].replace('\n','')
      print('clear')
    
  return result

def saveParser(repeat,number):
  result = json.dumps(parsing(repeat,number),indent=4)
  with open ('data.txt','w',newline='\n') as f:
    f.write(result)
  print('완료')

print('------------------ auto parser with BeautifulSoup4 ---------------------------',end='\n')
print('1. 한국 위키피디아',end='\n')
print('2. 미국 위키피디아',end='\n')
print('선택 :',end='\n')
routeinput = int(input())
repeat = int(input('반복 횟수 선택 :'))
saveParser(repeat,routeinput)




