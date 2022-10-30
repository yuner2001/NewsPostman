import os
import sys

if __name__ == '__main__':
    # root_path = os.path.abspath(__file__)
    # root_path = '/'.join(root_path.split('/')[:-2])
    # print('-------------------------------')
    # print(root_path)
    # sys.path.append(root_path)
    os.system('scrapy crawl baidu')
    print('=========================')
    # TODO: send the Email