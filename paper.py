import datetime
import json


class Html:
    
    def __init__(self) -> None:
        self.head = '<head> \
                        <meta charset="UTF-8"> \
                        <title>News Daliy</title> \
                    </head>'
        self.body = '<body>'
        self.content = ""
        

    def img(self, src:str):
        self.body += f'<img src = {src} align = "center">'

    def list(self, items:list):
        list_content = "<ul>"
        for i in items:
            list_content += f'<li>{i}</li>'
        list_content += '</ul>'
        self.body += list_content

    def title(self, title:str, level:int):
        self.body += f'<h{level}>{title}</h{level}>'

    def build(self):
        self.body += '</body>'
        self.content = f'<!doctype html><html>{self.head}{self.body}</html>'

    def clear(self):
        self.body = '<body>'

class Paper:
    def __init__(self) -> None:
        self.head_logo = 'head.png'
        self.html = Html()
        self.date = datetime.datetime.now()
        self.news_compile = dict()

    def build(self, news_path):
        with open(news_path, 'r') as f:
            self.news_compile = json.loads(f.read())
        f.close()
        self.html.img('https://pic2.zhimg.com/v2-db6ae9a7acf2dd7d3e12f04fefc46779_r.jpg')
        for news_src in self.news_compile:
            news_block = self.news_compile[news_src]
            news_num = len(self.news_compile[news_src])
            self.html.title(news_src + f'({news_num})', 2)
            news_list = []
            assert type(news_block) == list, 'type error'
            for new in news_block:
                assert type(new) == dict, 'type error'
                news_list.append(new['title'])
            self.html.list(items = news_list)
        self.html.build()
        with open('paper.html', 'w') as f:
            f.truncate()
            f.write(self.html.content)
        f.close()             

    def get_content(self):
        return self.html.content

    def clear(self,):
        self.date = ''
        self.news_compile = {}
        self.html.clear()

