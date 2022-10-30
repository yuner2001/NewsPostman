import datetime

from NewsPostman.items import NewspostmanItem


class Markdown:
    def __init__(self) -> None:
        self.content = ''

    def addLine(self, line):
        self.content += line
        self.content += "  \n"

    def getPDF(self):
        pass
    
    def clear(self):
        self.content = ""

class Paper:
    def __init__(self) -> None:
        self.head_logo = 'head.png'
        self.news_compile = dict()
        self.markdown = Markdown()
        self.date = datetime.datetime.now()

    def build(self):
        self.markdown.addLine('<img src = "head.png" align = "center">')
        for news_src in self.news_compile:
            self.markdown.addLine("## " + news_src)
            news_block = self.news_compile[news_src]
            assert type(news_block) == list, 'type error'
            for new in news_block:
                assert type(new) == NewspostmanItem, 'type error'
                self.markdown.addLine('- ' + new['title'])                

    def clear(self,):
        self.date = ''
        self.news_compile = {}
        self.markdown.clear()
