# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import json

from itemadapter import ItemAdapter

#from NewsPostman.glb import paper
#from NewsPostman.items import NewspostmanItem


class NewspostmanPipeline:
    def process_item(self, item, spider):   
        '''
            the jsonm format of the paper should be:

            dict ---------------- paper
              |——List ----------- news block
                   |——dict ------ news item

            paper: the whole paper
            news block: contain the news items which from a certain news source(.e.g baidu)
            news item: a certain news
        '''
        # load news info with json format 
        def load_news_json() -> dict:
            with open('news.json', 'r') as f:
                json_str = f.read()
            f.close()
            return json.loads(json_str)
        news_dict = load_news_json()

        # add item to the paper       
        news_src = item['category']
        if news_src not in news_dict:
            news_dict[news_src] = []
        news_block = news_dict[news_src]
        item_dict = ItemAdapter(item).asdict()
        assert type(news_block) == list, 'type error'
        print('==========================')
        for news in news_block:
            if news['title'] == item_dict['title']:
                return item     
        news_block.append(item_dict)

        # store the news info with json format
        def store_news_json():
            with open('news.json', 'w') as f:
                f.truncate()
                json_str = json.dumps(news_dict)
                f.write(json_str)
            f.close()   
        store_news_json()

        return item

