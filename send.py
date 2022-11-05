import os
import sys

from news_email import NewsEmail
from paper import Paper

paper = Paper()
receive_list = [
        'NewsPostman@163.com',
        'salhe@qq.com'
    ]


def reset():
    paper.clear()
    with open('news.json', 'w') as f:
        f.truncate()
        f.write('{}')
    f.close()
    with open('paper.html', 'w') as f:
        f.truncate()
    f.close()

if __name__ == '__main__':
    
    paper.build('news.json')
    print('build finished!')
    print('sending...')  
    news_email = NewsEmail(
        user = 'DaliyNews@163.com',
        pwd = 'AUBPTLDNZENUNXIU',
        send = 'DaliyNews@163.com',
        receiver_list = receive_list,
        content = paper.get_content()
    )
    news_email.send_email()
    print('sending finished!')
    reset()