from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
import re

class Parser:

    def __init__(self,link):
        self.link = link

    def parsing(self):
        result = []

        if self.link == '':
            return ''
        # targetUrl = urlopen("https://ko.wikipedia.org/wiki/%ED%8A%B9%EC%88%98:%EC%9E%84%EC%9D%98%EB%AC%B8%EC%84%9C") if number == 1 else urlopen("https://en.wikipedia.org/wiki/Special:Random")
        targetUrl = urlopen(self.link)
        bsObje = BeautifulSoup(targetUrl, 'html.parser')
        target = bsObje.select('p')
        for i in range(len(target)-1):
            result.append(target[i].get_text())
        #result = target.get_text()

        wiki_index = [str([(i)]) for i in range(1, 1000)]

        for i in range(len(result)):
            if '\n' in result[i]:
                result[i] = result[i].replace('\n', '')
            # print('개행 문자 삭제중...')
            if '\'' in result[i]:
                result[i] = result[i].replace('\'', '')
            # print('역슬래쉬 삭제중...')
            if '/' in result[i]:
                result[i] = result[i].replace('/', '')
            # print('슬래쉬 삭제중...')

        for index in wiki_index:
        #for i in range(len(result)):
            if index in result:
                result = result.replace(wiki_index[wiki_index.index(index)], '')
        #result = [c for c in result if c]
        return result

    def saveParser(self):
        result = json.dumps(self.parsing(), indent=4)
        return json.dumps(self.remove_unicode(result),indent=4)

    def remove_unicode(self,result):
        res = []
        rst = []
        data = []

        result = re.sub(r"/[u]\S{4,10}", "", result)
        #for i in result:
        #    v = re.sub(r"/[u]\S{4,10}", "", i)
        #    res.append(v)

        #for i in res:
        #   v =  res = re.sub(r"/[u]\S{4,10}", "", i)
        #   rst.append(v)

        #for i in rst:
        if '\\' in result:
            result = result.replace('\\','/')
                #data.append(i)

        return "".join(result)


#       with open('data.txt', 'r') as d:
#            for i in d:
#                if '\\' in i:
#                    i = i.replace('\\', '/')
#                data.append(i)
#        os.remove('data.txt')

#        for i in data:
#            res = re.sub(r"/[u]\S{4,10}", "", i)
#            result.append(res)

#        with open('result.txt', 'w') as f:
#            for i in result:
#                if r'\n' in i:
#                    i = i.replace(r'\n', '')
#                if '/' in i:
#                    i = i.replace('/', '')
#                f.write(i)


#    if __name__ == "__main__":
 #       print('------------------ auto parser with BeautifulSoup4 ---------------------------', end='\n')
#        print('1. 한국 위키피디아 !!!현재 불안정한 상태! 사용 비권장 추후 고칠 예정!!!', end='\n')
#        print('2. 미국 위키피디아', end='\n')
#        print('선택 :', end='\n')
#        routeinput = int(input())
#        repeat = int(input('크롤링 할 문서 개수 선택 :'))
#        if (os.path.isfile('./data.txt') and os.path.isfile('./result.txt')):
#            os.remove('./data.txt')
#            os.remove('./result.txt')
#        saveParser(link)
#        remove_unicode()


