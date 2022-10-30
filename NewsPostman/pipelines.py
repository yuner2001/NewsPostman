# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from NewsPostman.items import NewspostmanItem


class NewspostmanPipeline:
    def process_item(self, item, spider):
        # TODO: To store the data to json
        return item
